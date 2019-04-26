import pytest
import inspect
import importlib
import json
import sys

from delphi.GrFN.networks import GroundedFunctionNetwork
from delphi.GrFN.sensitivity import FAST_analysis, RBD_FAST_analysis
import delphi.GrFN.analysis as analysis
from test_GrFN import petpt_grfn, petasce_grfn


sys.path.insert(0, "tests/data/program_analysis")


def test_regular_PETPT(petpt_grfn):
    args = petpt_grfn.inputs
    bounds = {
        "petpt::msalb_-1": [0, 1],
        "petpt::srad_-1": [1, 20],
        "petpt::tmax_-1": [-30, 60],
        "petpt::tmin_-1": [-30, 60],
        "petpt::xhlai_-1": [0, 20],
    }

    problem = {
        'num_vars': len(args),
        'names': args,
        'bounds': [bounds[arg] for arg in args]
    }

    Ns = 1000 # TODO: Khan, experiment with this value
    Si = petpt_grfn.sobol_analysis(Ns, problem)
    assert len(Si.keys()) == 6
    assert len(Si["S1"]) == len(args)


@pytest.mark.skip("Need to update to latest JSON")
def test_PETPT_with_torch():
    lambdas = importlib.__import__("PETPT_torch_lambdas")
    pgm = json.load(open("tests/data/program_analysis/PETPT.json", "r"))
    G = GroundedFunctionNetwork.from_dict(pgm, lambdas)

    args = G.inputs
    bounds = {
        "petpt::msalb_-1": [0, 1],
        "petpt::srad_-1": [1, 20],
        "petpt::tmax_-1": [-30, 60],
        "petpt::tmin_-1": [-30, 60],
        "petpt::xhlai_-1": [0, 20],
    }

    problem = {
        'num_vars': len(args),
        'names': args,
        'bounds': [bounds[arg] for arg in args]
    }

    Ns = 1000                      # TODO: Khan, experiment with this value
    Si = G.sobol_analysis(Ns, problem, use_torch=True)
    assert len(Si.keys()) == 6
    assert len(Si["S1"]) == len(args)

    Si = FAST_analysis(G, Ns, problem)
    assert len(Si.keys()) == 3
    assert len(Si["S1"]) == len(args)

    Si = RBD_FAST_analysis(G, Ns, problem)
    assert len(Si.keys()) == 2
    assert len(Si["S1"]) == len(args)


def test_PETASCE_sobol_analysis(petasce_grfn):
    bounds = {
        "petasce::doy_-1": [1, 365],
        "petasce::meevp_-1": [0, 1],
        "petasce::msalb_-1": [0, 1],
        "petasce::srad_-1": [1, 30],
        "petasce::tmax_-1": [-30, 60],
        "petasce::tmin_-1": [-30, 60],
        "petasce::xhlai_-1": [0, 20],
        "petasce::tdew_-1": [-30, 60],
        "petasce::windht_-1": [0.1, 10],  # HACK: has a hole in 0 < x < 1 for petasce__assign__wind2m_1
        "petasce::windrun_-1": [0, 900],
        "petasce::xlat_-1": [3, 12],     # HACK: south sudan lats
        "petasce::xelev_-1": [0, 6000],
        "petasce::canht_-1": [0.001, 3],
    }

    type_info = {
        "petasce::doy_-1": (int, list(range(1, 366))),
        "petasce::meevp_-1": (str, ["A", "W"]),
        "petasce::msalb_-1": (float, [0.0]),
        "petasce::srad_-1": (float, [0.0]),
        "petasce::tmax_-1": (float, [0.0]),
        "petasce::tmin_-1": (float, [0.0]),
        "petasce::xhlai_-1": (float, [0.0]),
        "petasce::tdew_-1": (float, [0.0]),
        "petasce::windht_-1": (float, [0.0]),
        "petasce::windrun_-1": (float, [0.0]),
        "petasce::xlat_-1": (float, [0.0]),
        "petasce::xelev_-1": (float, [0.0]),
        "petasce::canht_-1": (float, [0.0]),
    }

    args = petasce_grfn.inputs
    problem = {
        'num_vars': len(args),
        'names': args,
        'bounds': [bounds[arg] for arg in args]
    }

    Si = petasce_grfn.sobol_analysis(100, problem, var_types=type_info)
    assert len(Si["S1"]) == len(petasce_grfn.inputs)
    assert len(Si["S2"][0]) == len(petasce_grfn.inputs)


def test_PETASCE_with_torch():
    # Torch model
    sys.path.insert(0, "tests/data/GrFN")
    lambdas = importlib.__import__("PETASCE_simple_torch_lambdas")
    pgm = json.load(open("tests/data/GrFN/PETASCE_simple_torch.json", "r"))
    tG = GroundedFunctionNetwork.from_dict(pgm, lambdas)

    bounds = {
        "petasce::doy_0": [1, 365],
        "petasce::meevp_0": [0, 1],
        "petasce::msalb_0": [0, 1],
        "petasce::srad_0": [1, 30],
        "petasce::tmax_0": [-30, 60],
        "petasce::tmin_0": [-30, 60],
        "petasce::xhlai_0": [0, 20],
        "petasce::tdew_0": [-30, 60],
        "petasce::windht_0": [0.1, 10],  # HACK: has a hole in 0 < x < 1 for petasce__assign__wind2m_1
        "petasce::windrun_0": [0, 900],
        "petasce::xlat_0": [3, 12],     # HACK: south sudan lats
        "petasce::xelev_0": [0, 6000],
        "petasce::canht_0": [0.001, 3],
    }

    type_info = {
        "petasce::doy_0": (int, list(range(1, 366))),
        "petasce::meevp_0": (str, ["A", "W"]),
        "petasce::msalb_0": (float, [0.0]),
        "petasce::srad_0": (float, [0.0]),
        "petasce::tmax_0": (float, [0.0]),
        "petasce::tmin_0": (float, [0.0]),
        "petasce::xhlai_0": (float, [0.0]),
        "petasce::tdew_0": (float, [0.0]),
        "petasce::windht_0": (float, [0.0]),
        "petasce::windrun_0": (float, [0.0]),
        "petasce::xlat_0": (float, [0.0]),
        "petasce::xelev_0": (float, [0.0]),
        "petasce::canht_0": (float, [0.0]),
    }

    args = tG.inputs
    problem = {
        'num_vars': len(args),
        'names': args,
        'bounds': [bounds[arg] for arg in args]
    }

    tSi = tG.sobol_analysis(1000, problem, var_types=type_info, use_torch=True)
    assert len(tSi["S1"]) == len(tG.inputs)
    assert len(tSi["S2"][0]) == len(tG.inputs)


def test_PETPT_sensitivity_surface(petpt_grfn):
    bounds = {
        "petpt::msalb_-1": (0, 1),
        "petpt::srad_-1": (1, 20),
        "petpt::tmax_-1": (-30, 60),
        "petpt::tmin_-1": (-30, 60),
        "petpt::xhlai_-1": (0, 20),
    }
    presets = {
        "petpt::msalb_-1": 0.5,
        "petpt::srad_-1": 10,
        "petpt::tmax_-1": 20,
        "petpt::tmin_-1": 10,
        "petpt::xhlai_-1": 10,
    }

    (X, Y, Z, x_var, y_var) = petpt_grfn.S2_surface((80, 60), bounds, presets)

    assert X.shape == (80,)
    assert Y.shape == (60,)
    assert Z.shape == (80, 60)


def test_FIB_execution(petpt_grfn, petasce_grfn):
    petpt_fib = petpt_grfn.to_FIB(petasce_grfn)
    petasce_fib = petasce_grfn.to_FIB(petpt_grfn)

    A = petpt_fib.to_agraph()
    CAG = petpt_fib.to_CAG_agraph()

    A.draw("PETPT_FIB.pdf", prog="dot")
    CAG.draw("PETPT_FIB_CAG.pdf", prog="dot")

    A = petasce_fib.to_agraph()
    CAG = petasce_fib.to_CAG_agraph()

    A.draw("PETASCE_FIB.pdf", prog="dot")
    CAG.draw("PETASCE_FIB_CAG.pdf", prog="dot")

    pt_inputs = {name: 1 for name in petpt_grfn.inputs}

    asce_inputs = {
        "petasce::msalb_-1": 0.5,
        "petasce::srad_-1": 15,
        "petasce::tmax_-1": 10,
        "petasce::tmin_-1": -10,
        "petasce::xhlai_-1": 10,
    }

    asce_covers = {
        "petasce::canht_-1": 2,
        "petasce::meevp_-1": "A",
        "petasce::cht_0": 0.001,
        "petasce::cn_4": 1600.0,
        "petasce::cd_4": 0.38,
        "petasce::rso_0": 0.062320,
        "petasce::ea_0": 7007.82,
        "petasce::wind2m_0": 3.5,
        "petasce::psycon_0": 0.0665,
        "petasce::wnd_0": 3.5,
    }

    res = petpt_fib.run(pt_inputs, {})
    assert res == 0.02998371219618677

    res = petasce_fib.run(asce_inputs, asce_covers)
    assert res == 0.00012496980836348878
