import csv
from test_GrFN import petpt_grfn
import delphi.translators.for2py.f2grfn as f2grfn


def test_PETPT_GrFN_wiring(petpt_grfn):
    with open("tests/data/GrFN/petpt_grfn_edges.txt", newline="") as csvfile:
        reader = csv.reader(csvfile)
        edges = {tuple(r) for r in reader}
    assert edges == set(petpt_grfn[0].edges())
    f2grfn.cleanup_files(petpt_grfn[1])


def test_PETPT_CAG_wiring(petpt_grfn):
    with open("tests/data/GrFN/petpt_cag_edges.txt", newline="") as csvfile:
        reader = csv.reader(csvfile)
        edges = {tuple(r) for r in reader}
    assert edges == set(petpt_grfn[0].to_CAG().edges())
    f2grfn.cleanup_files(petpt_grfn[1])
