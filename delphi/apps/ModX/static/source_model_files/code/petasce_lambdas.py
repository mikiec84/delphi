from numbers import Real
from random import random
import delphi.translators.for2py.math_ext as math

def petasce__petasce__assign__tavg__0(tmax: Real, tmin: Real):
    return ((tmax+tmin)/2.0)

def petasce__petasce__assign__patm__0(xelev: Real):
    return (101.3*(((293.0-(0.0065*xelev))/293.0)**5.26))

def petasce__petasce__assign__psycon__0(patm: Real):
    return (0.000665*patm)

def petasce__petasce__assign__udelta__0(tavg: Real):
    return ((2503.0*math.exp(((17.27*tavg)/(tavg+237.3))))/((tavg+237.3)**2.0))

def petasce__petasce__assign__emax__0(tmax: Real):
    return (0.6108*math.exp(((17.27*tmax)/(tmax+237.3))))

def petasce__petasce__assign__emin__0(tmin: Real):
    return (0.6108*math.exp(((17.27*tmin)/(tmin+237.3))))

def petasce__petasce__assign__es__0(emax: Real, emin: Real):
    return ((emax+emin)/2.0)

def petasce__petasce__assign__ea__0(tdew: Real):
    return (0.6108*math.exp(((17.27*tdew)/(tdew+237.3))))

def petasce__petasce__assign__rhmin__0(ea: Real, emax: Real):
    return max(20.0, min(80.0, ((ea/emax)*100.0)))

def petasce__petasce__condition__IF_0__0(xhlai: Real):
    return (xhlai <= 0.0)

def petasce__petasce__assign__albedo__0(msalb: Real):
    return msalb

def petasce__petasce__assign__albedo__1():
    return 0.23

def petasce__petasce__decision__albedo__2(albedo_0: Real, albedo_1: Real, IF_0_0: bool):
    return albedo_1 if IF_0_0 else albedo_0

def petasce__petasce__assign__rns__0(albedo: Real, srad: Real):
    return ((1.0-albedo)*srad)

def petasce__petasce__assign__pie__0():
    return 3.14159265359

def petasce__petasce__assign__dr__0(pie: Real, doy: int):
    return (1.0+(0.033*math.cos((((2.0*pie)/365.0)*doy))))

def petasce__petasce__assign__ldelta__0(pie: Real, doy: int):
    return (0.409*math.sin(((((2.0*pie)/365.0)*doy)-1.39)))

def petasce__petasce__assign__ws__0(xlat: Real, pie: Real, ldelta: Real):
    return math.acos(-(((1.0*math.tan(((xlat*pie)/180.0)))*math.tan(ldelta))))

def petasce__petasce__assign__ra1__0(ws: Real, xlat: Real, pie: Real, ldelta: Real):
    return ((ws*math.sin(((xlat*pie)/180.0)))*math.sin(ldelta))

def petasce__petasce__assign__ra2__0(xlat: Real, pie: Real, ldelta: Real, ws: Real):
    return ((math.cos(((xlat*pie)/180.0))*math.cos(ldelta))*math.sin(ws))

def petasce__petasce__assign__ra__0(pie: Real, dr: Real, ra1: Real, ra2: Real):
    return ((((24.0/pie)*4.92)*dr)*(ra1+ra2))

def petasce__petasce__assign__rso__0(xelev: Real, ra: Real):
    return ((0.75+(2e-05*xelev))*ra)

def petasce__petasce__assign__ratio__0(srad: Real, rso: Real):
    return (srad/rso)

def petasce__petasce__condition__IF_1__0(ratio: Real):
    return (ratio < 0.3)

def petasce__petasce__assign__ratio__1():
    return 0.3

def petasce__petasce__decision__ratio__2(ratio_0: Real, ratio_1: Real, IF_1_0: bool):
    return ratio_1 if IF_1_0 else ratio_0

def petasce__petasce__condition__IF_1__1(ratio: Real):
    return (ratio > 1.0)

def petasce__petasce__assign__ratio__3():
    return 1.0

def petasce__petasce__decision__ratio__4(ratio_0: Real, ratio_1: Real, IF_1_1: bool):
    return ratio_1 if IF_1_1 else ratio_0

def petasce__petasce__assign__fcd__0(ratio: Real):
    return ((1.35*ratio)-0.35)

def petasce__petasce__assign__tk4__0(tmax: Real, tmin: Real):
    return ((((tmax+273.16)**4.0)+((tmin+273.16)**4.0))/2.0)

def petasce__petasce__assign__rnl__0(fcd: Real, ea: Real, tk4: Real):
    return (((4.901e-09*fcd)*(0.34-(0.14*math.sqrt(ea))))*tk4)

def petasce__petasce__assign__rn__0(rns: Real, rnl: Real):
    return (rns-rnl)

def petasce__petasce__assign__g__0():
    return 0.0

def petasce__petasce__assign__windsp__0(windrun: Real):
    return ((((windrun*1000.0)/24.0)/60.0)/60.0)

def petasce__petasce__assign__wind2m__0(windsp: Real, windht: Real):
    return (windsp*(4.87/math.log(((67.8*windht)-5.42))))

def petasce__petasce__assign__cn__0():
    return 0.0

def petasce__petasce__assign__cd__0():
    return 0.0

def petasce__petasce__condition__IF_2__0(meevp: str):
    return (meevp == "A")

def petasce__petasce__assign__cn__1():
    return 1600.0

def petasce__petasce__assign__cd__1():
    return 0.38

def petasce__petasce__decision__cd__2(cd_0: Real, cd_1: Real, IF_2_0: bool):
    return cd_1 if IF_2_0 else cd_0

def petasce__petasce__decision__cn__2(cn_0: Real, cn_1: Real, IF_2_0: bool):
    return cn_1 if IF_2_0 else cn_0

def petasce__petasce__condition__IF_2__1(meevp: str):
    return (meevp == "G")

def petasce__petasce__assign__cn__3():
    return 900.0

def petasce__petasce__assign__cd__3():
    return 0.34

def petasce__petasce__decision__cd__4(cd_0: Real, cd_1: Real, IF_2_1: bool):
    return cd_1 if IF_2_1 else cd_0

def petasce__petasce__decision__cn__4(cn_0: Real, cn_1: Real, IF_2_1: bool):
    return cn_1 if IF_2_1 else cn_0

def petasce__petasce__assign__refet__0(udelta: Real, rn: Real, g: Real, psycon: Real, cn: Real, tavg: Real, wind2m: Real, es: Real, ea: Real):
    return (((0.408*udelta)*(rn-g))+(((psycon*(cn/(tavg+273.0)))*wind2m)*(es-ea)))

def petasce__petasce__assign__refet__1(refet: Real, udelta: Real, psycon: Real, cd: Real, wind2m: Real):
    return (refet/(udelta+(psycon*(1.0+(cd*wind2m)))))

def petasce__petasce__assign__refet__2(refet: Real):
    return max(0.0001, refet)

def petasce__petasce__assign__skc__0():
    return 0.8

def petasce__petasce__assign__kcbmin__0():
    return 0.3

def petasce__petasce__assign__kcbmax__0():
    return 1.2

def petasce__petasce__condition__IF_3__0(xhlai: Real):
    return (xhlai <= 0.0)

def petasce__petasce__assign__kcb__0():
    return 0.0

def petasce__petasce__assign__kcb__1(kcbmin: Real, kcbmax: Real, skc: Real, xhlai: Real):
    return max(0.0, (kcbmin+((kcbmax-kcbmin)*(1.0-math.exp(-(((1.0*skc)*xhlai)))))))

def petasce__petasce__decision__kcb__2(kcb_0: Real, kcb_1: Real, IF_3_0: bool):
    return kcb_1 if IF_3_0 else kcb_0

def petasce__petasce__assign__wnd__0(wind2m: Real):
    return max(1.0, min(wind2m, 6.0))

def petasce__petasce__assign__cht__0(canht: Real):
    return max(0.001, canht)

def petasce__petasce__assign__kcmax__0():
    return 0.5

def petasce__petasce__condition__IF_4__0(meevp: str):
    return (meevp == "A")

def petasce__petasce__assign__kcmax__1(kcb: Real):
    return max(1.0, (kcb+0.05))

def petasce__petasce__decision__kcmax__2(kcmax_0: Real, kcmax_1: Real, IF_4_0: bool):
    return kcmax_1 if IF_4_0 else kcmax_0

def petasce__petasce__condition__IF_4__1(meevp: str):
    return (meevp == "G")

def petasce__petasce__assign__kcmax__3(wnd: Real, rhmin: Real, cht: Real, kcb: Real):
    return max((1.2+(((0.04*(wnd-2.0))-(0.004*(rhmin-45.0)))*((cht/3.0)**0.3))), (kcb+0.05))

def petasce__petasce__decision__kcmax__4(kcmax_0: Real, kcmax_1: Real, IF_4_1: bool):
    return kcmax_1 if IF_4_1 else kcmax_0

def petasce__petasce__condition__IF_5__0(kcb: Real, kcbmin: Real):
    return (kcb <= kcbmin)

def petasce__petasce__assign__fc__0():
    return 0.0

def petasce__petasce__assign__fc__1(kcb: Real, kcbmin: Real, kcmax: Real, canht: Real):
    return (((kcb-kcbmin)/(kcmax-kcbmin))**(1.0+(0.5*canht)))

def petasce__petasce__decision__fc__2(fc_0: Real, fc_1: Real, IF_5_0: bool):
    return fc_1 if IF_5_0 else fc_0

def petasce__petasce__assign__fw__0():
    return 1.0

def petasce__petasce__assign__few__0(fc: Real, fw: Real):
    return min((1.0-fc), fw)

def petasce__petasce__assign__ke__0(kcmax: Real, kcb: Real, few: Real):
    return max(0.0, min((1.0*(kcmax-kcb)), (few*kcmax)))

def petasce__petasce__assign__eo__0(kcb: Real, ke: Real, refet: Real):
    return ((kcb+ke)*refet)

def petasce__petasce__assign__eo__1(eo: Real):
    return max(eo, 0.0001)

