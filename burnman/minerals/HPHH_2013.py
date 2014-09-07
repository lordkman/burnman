# BurnMan - a lower mantle toolkit
# Copyright (C) 2012-2014, Myhill, R., Heister, T., Unterborn, C., Rose, I. and Cottaar, S.
# Released under GPL v2 or later.

"""

HPHH_2013
^^^^^^^^

Minerals from Holland et al., 2013 (2013)
The values in this document are all in S.I. units, 
unlike those in the original table (Table 1)

N.B. VERY IMPORTANT: The excess entropy term in the regular solution model has the opposite sign to the values in Holland and Powell datasets. This is consistent with its treatment as an excess entropy term (G=H-T*S+P*V), rather than a thermal correction to the interaction parameter (W=W+T*W_T+P*W_P).
"""

from burnman.mineral import Mineral
from burnman.solidsolution import SolidSolution
from burnman.processchemistry import read_masses, dictionarize_formula, formula_mass
from burnman.solutionmodel import *

atomic_masses=read_masses()

class fo (Mineral):
    def __init__(self):
       formula='Mg2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fo',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2172450.0 ,
            'S_0': 95.1 ,
            'V_0': 4.366e-05 ,
            'Cp:' [233.3, 0.001494, -603800.0, -1869.7] ,
            'a_0': 2.85e-05 ,
            'K_0': 1.285e+11 ,
            'Kprime_0': 3.84 ,
            'Kdprime_0': -3e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 530.0 }

class fa (Mineral):
    def __init__(self):
       formula='Fe2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fa',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1477740.0 ,
            'S_0': 151.0 ,
            'V_0': 4.631e-05 ,
            'Cp:' [201.1, 0.01733, -1960600.0, -900.9] ,
            'a_0': 2.82e-05 ,
            'K_0': 1.256e+11 ,
            'Kprime_0': 4.68 ,
            'Kdprime_0': -3.7e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 640.0 }

class mwd (Mineral):
    def __init__(self):
       formula='Mg2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'mwd',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2138080.0 ,
            'S_0': 93.9 ,
            'V_0': 4.051e-05 ,
            'Cp:' [208.7, 0.003942, -1709500.0, -1302.8] ,
            'a_0': 2.37e-05 ,
            'K_0': 1.726e+11 ,
            'Kprime_0': 3.84 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 620.0 }

class fwd (Mineral):
    def __init__(self):
       formula='Fe2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fwd',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1467920.0 ,
            'S_0': 146.0 ,
            'V_0': 4.321e-05 ,
            'Cp:' [201.1, 0.01733, -1960600.0, -900.9] ,
            'a_0': 2.73e-05 ,
            'K_0': 1.69e+11 ,
            'Kprime_0': 4.35 ,
            'Kdprime_0': -2.6e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 900.0 }

class mrw (Mineral):
    def __init__(self):
       formula='Mg2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'mrw',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2126840.0 ,
            'S_0': 90.0 ,
            'V_0': 3.949e-05 ,
            'Cp:' [213.3, 0.00269, -1410400.0, -1495.9] ,
            'a_0': 2.01e-05 ,
            'K_0': 1.781e+11 ,
            'Kprime_0': 4.35 ,
            'Kdprime_0': -2.4e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 630.0 }

class frw (Mineral):
    def __init__(self):
       formula='Fe2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'frw',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1471760.0 ,
            'S_0': 140.0 ,
            'V_0': 4.203e-05 ,
            'Cp:' [166.8, 0.04261, -1705400.0, -541.4] ,
            'a_0': 2.22e-05 ,
            'K_0': 1.977e+11 ,
            'Kprime_0': 4.92 ,
            'Kdprime_0': -2.5e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 710.0 }

class mpv (Mineral):
    def __init__(self):
       formula='MgSiO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'mpv',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1442310.0 ,
            'S_0': 62.6 ,
            'V_0': 2.445e-05 ,
            'Cp:' [149.3, 0.002918, -2983000.0, -799.1] ,
            'a_0': 1.87e-05 ,
            'K_0': 2.51e+11 ,
            'Kprime_0': 4.14 ,
            'Kdprime_0': -1.6e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 470.0 }

class fpv (Mineral):
    def __init__(self):
       formula='FeSiO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fpv',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1082910.0 ,
            'S_0': 95.0 ,
            'V_0': 2.534e-05 ,
            'Cp:' [133.2, 0.01083, -3661400.0, -314.7] ,
            'a_0': 1.87e-05 ,
            'K_0': 2.81e+11 ,
            'Kprime_0': 4.14 ,
            'Kdprime_0': -1.6e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 760.0 }

class apv (Mineral):
    def __init__(self):
       formula='AlAlO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'apv',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1619990.0 ,
            'S_0': 51.8 ,
            'V_0': 2.54e-05 ,
            'Cp:' [139.5, 0.00589, -2460600.0, -589.2] ,
            'a_0': 1.8e-05 ,
            'K_0': 2.03e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 770.0 }

class npv (Mineral):
    def __init__(self):
       formula='Na0.5Al0.5SiO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'npv',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1365000.0 ,
            'S_0': 63.0 ,
            'V_0': 2.334e-05 ,
            'Cp:' [135.0, 0.00846, -1850300.0, -600.8] ,
            'a_0': 1.8e-05 ,
            'K_0': 2.03e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 10240.0 }

class cpv (Mineral):
    def __init__(self):
       formula='CaSiO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'cpv',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1533590.0 ,
            'S_0': 74.5 ,
            'V_0': 2.745e-05 ,
            'Cp:' [159.3, 0.0, -967300.0, -1075.4] ,
            'a_0': 2e-05 ,
            'K_0': 2.36e+11 ,
            'Kprime_0': 3.9 ,
            'Kdprime_0': -1.6e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 1090.0 }

class mak (Mineral):
    def __init__(self):
       formula='MgSiO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'mak',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1489610.0 ,
            'S_0': 59.3 ,
            'V_0': 2.635e-05 ,
            'Cp:' [147.8, 0.002015, -2395000.0, -801.8] ,
            'a_0': 2.12e-05 ,
            'K_0': 2.11e+11 ,
            'Kprime_0': 4.55 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 420.0 }

class fak (Mineral):
    def __init__(self):
       formula='FeSiO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fak',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1142130.0 ,
            'S_0': 91.5 ,
            'V_0': 2.76e-05 ,
            'Cp:' [100.3, 0.013328, -4364900.0, 419.8] ,
            'a_0': 2.12e-05 ,
            'K_0': 2.18e+11 ,
            'Kprime_0': 4.55 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 9630.0 }

class maj (Mineral):
    def __init__(self):
       formula='Mg4Si4O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'maj',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -6041550.0 ,
            'S_0': 260.2 ,
            'V_0': 0.00011457 ,
            'Cp:' [713.6, -0.000997, -1158200.0, -6622.3] ,
            'a_0': 1.83e-05 ,
            'K_0': 1.6e+11 ,
            'Kprime_0': 4.56 ,
            'Kdprime_0': -2.8e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 2260.0 }

class nagt (Mineral):
    def __init__(self):
       formula='Mg2NaAlSiSi3O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'nagt',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -5985000.0 ,
            'S_0': 260.6 ,
            'V_0': 0.0001109 ,
            'Cp:' [620.8, 0.0112, -3755900.0, -4421.3] ,
            'a_0': 2.1e-05 ,
            'K_0': 1.7e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2.3e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 5120.0 }

class py (Mineral):
    def __init__(self):
       formula='Mg3Al2Si3O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'py',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -6281770.0 ,
            'S_0': 269.5 ,
            'V_0': 0.00011313 ,
            'Cp:' [633.5, 0.0, -5196100.0, -4315.2] ,
            'a_0': 2.37e-05 ,
            'K_0': 1.743e+11 ,
            'Kprime_0': 4.05 ,
            'Kdprime_0': -2.3e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 990.0 }

class alm (Mineral):
    def __init__(self):
       formula='Fe3Al2Si3O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'alm',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -5260750.0 ,
            'S_0': 342.0 ,
            'V_0': 0.00011525 ,
            'Cp:' [677.3, 0.0, -3772700.0, -5044.0] ,
            'a_0': 2.12e-05 ,
            'K_0': 1.9e+11 ,
            'Kprime_0': 2.98 ,
            'Kdprime_0': -1.6e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 1200.0 }

class gr (Mineral):
    def __init__(self):
       formula='Ca3Al2Si3O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'gr',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -6643050.0 ,
            'S_0': 255.0 ,
            'V_0': 0.00012535 ,
            'Cp:' [626.0, 0.0, -5779200.0, -4002.9] ,
            'a_0': 2.2e-05 ,
            'K_0': 1.72e+11 ,
            'Kprime_0': 5.53 ,
            'Kdprime_0': -3.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 1370.0 }

class en (Mineral):
    def __init__(self):
       formula='Mg2Si2O6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'en',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -3090100.0 ,
            'S_0': 132.5 ,
            'V_0': 6.262e-05 ,
            'Cp:' [356.2, -0.00299, -596900.0, -3185.3] ,
            'a_0': 2.27e-05 ,
            'K_0': 1.059e+11 ,
            'Kprime_0': 8.65 ,
            'Kdprime_0': -8.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 620.0 }

class cen (Mineral):
    def __init__(self):
       formula='Mg2Si2O6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'cen',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -3090990.0 ,
            'S_0': 132.0 ,
            'V_0': 6.264e-05 ,
            'Cp:' [306.0, -0.003793, -3041700.0, -1852.1] ,
            'a_0': 2.11e-05 ,
            'K_0': 1.059e+11 ,
            'Kprime_0': 8.65 ,
            'Kdprime_0': -8.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 620.0 }

class hen (Mineral):
    def __init__(self):
       formula='Mg2Si2O6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'hen',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -3082610.0 ,
            'S_0': 131.7 ,
            'V_0': 6.099e-05 ,
            'Cp:' [356.2, -0.00299, -596900.0, -3185.3] ,
            'a_0': 2.26e-05 ,
            'K_0': 1.5e+11 ,
            'Kprime_0': 5.5 ,
            'Kdprime_0': -3.6e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 620.0 }

class hfs (Mineral):
    def __init__(self):
       formula='Fe2Si2O6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'hfs',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2380810.0 ,
            'S_0': 189.0 ,
            'V_0': 6.405e-05 ,
            'Cp:' [398.7, -0.006579, 1290100.0, -4058.0] ,
            'a_0': 2.37e-05 ,
            'K_0': 1.5e+11 ,
            'Kprime_0': 5.5 ,
            'Kdprime_0': -3.6e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 790.0 }

class fs (Mineral):
    def __init__(self):
       formula='Fe2Si2O6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fs',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2388760.0 ,
            'S_0': 189.9 ,
            'V_0': 6.592e-05 ,
            'Cp:' [398.7, -0.006579, 1290100.0, -4058.0] ,
            'a_0': 3.26e-05 ,
            'K_0': 1.01e+11 ,
            'Kprime_0': 4.08 ,
            'Kdprime_0': -4e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 750.0 }

class mgts (Mineral):
    def __init__(self):
       formula='MgAl2SiO6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'mgts',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -3196600.0 ,
            'S_0': 131.0 ,
            'V_0': 6.05e-05 ,
            'Cp:' [371.4, -0.004082, -398400.0, -3547.1] ,
            'a_0': 2.17e-05 ,
            'K_0': 1.028e+11 ,
            'Kprime_0': 8.55 ,
            'Kdprime_0': -8.3e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 690.0 }

class di (Mineral):
    def __init__(self):
       formula='CaMgSi2O6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'di',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -3201820.0 ,
            'S_0': 142.9 ,
            'V_0': 6.619e-05 ,
            'Cp:' [314.5, 4.1e-05, -2745900.0, -2020.1] ,
            'a_0': 2.73e-05 ,
            'K_0': 1.192e+11 ,
            'Kprime_0': 5.19 ,
            'Kdprime_0': -4.4e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 580.0 }

class hed (Mineral):
    def __init__(self):
       formula='CaFeSi2O6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'hed',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2842120.0 ,
            'S_0': 175.0 ,
            'V_0': 6.795e-05 ,
            'Cp:' [340.2, 0.000812, -1047800.0, -2646.7] ,
            'a_0': 2.38e-05 ,
            'K_0': 1.192e+11 ,
            'Kprime_0': 3.97 ,
            'Kdprime_0': -3.3e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 880.0 }

class jd (Mineral):
    def __init__(self):
       formula='NaAlSiO6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'jd',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -3025290.0 ,
            'S_0': 133.5 ,
            'V_0': 6.04e-05 ,
            'Cp:' [319.4, 0.003616, -1173900.0, -2469.5] ,
            'a_0': 2.1e-05 ,
            'K_0': 1.281e+11 ,
            'Kprime_0': 3.81 ,
            'Kdprime_0': -3e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 1520.0 }

class cats (Mineral):
    def __init__(self):
       formula='CaAl2SiO6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'cats',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -3310110.0 ,
            'S_0': 135.0 ,
            'V_0': 6.356e-05 ,
            'Cp:' [347.6, -0.006974, -1781600.0, -2757.5] ,
            'a_0': 2.08e-05 ,
            'K_0': 1.192e+11 ,
            'Kprime_0': 5.19 ,
            'Kdprime_0': -4.4e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 750.0 }

class stv (Mineral):
    def __init__(self):
       formula='SiO2'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'stv',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -876820.0 ,
            'S_0': 24.0 ,
            'V_0': 1.401e-05 ,
            'Cp:' [68.1, 0.00601, -1978200.0, -82.1] ,
            'a_0': 1.58e-05 ,
            'K_0': 3.09e+11 ,
            'Kprime_0': 4.6 ,
            'Kdprime_0': -1.5e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 420.0 }

class macf (Mineral):
    def __init__(self):
       formula='MgAl2O4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'macf',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2246420.0 ,
            'S_0': 80.0 ,
            'V_0': 3.614e-05 ,
            'Cp:' [200.0, 0.006252, -2996400.0, -888.4] ,
            'a_0': 1.93e-05 ,
            'K_0': 2.12e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -1.7e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 1080.0 }

class mscf (Mineral):
    def __init__(self):
       formula='Mg2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'mscf',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2061130.0 ,
            'S_0': 87.5 ,
            'V_0': 3.649e-05 ,
            'Cp:' [213.3, 0.00269, -1410400.0, -1495.9] ,
            'a_0': 2.01e-05 ,
            'K_0': 1.85e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -1.7e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 1340.0 }

class fscf (Mineral):
    def __init__(self):
       formula='Fe2SiO4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fscf',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1405500.0 ,
            'S_0': 143.4 ,
            'V_0': 3.914e-05 ,
            'Cp:' [181.1, 0.018526, -2767200.0, -527.1] ,
            'a_0': 2.01e-05 ,
            'K_0': 1.85e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -1.7e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 10240.0 }

class nacf (Mineral):
    def __init__(self):
       formula='NaAlSiO6'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'nacf',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1965550.0 ,
            'S_0': 110.0 ,
            'V_0': 3.631e-05 ,
            'Cp:' [272.7, -0.012398, 0.0, -2763.1] ,
            'a_0': 2.1e-05 ,
            'K_0': 1.85e+11 ,
            'Kprime_0': 4.6 ,
            'Kdprime_0': -2.5e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 3440.0 }

class cacf (Mineral):
    def __init__(self):
       formula='CaAl2O4'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'cacf',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -2325600.0 ,
            'S_0': 87.6 ,
            'V_0': 3.976e-05 ,
            'Cp:' [191.9, 0.009563, -3211300.0, -640.2] ,
            'a_0': 1.93e-05 ,
            'K_0': 1.9e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2.1e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 10240.0 }

class manal (Mineral):
    def __init__(self):
       formula='Mg3Al6O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'manal',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -6796630.0 ,
            'S_0': 250.0 ,
            'V_0': 0.00011166 ,
            'Cp:' [600.0, 0.018756, -8989200.0, -2665.2] ,
            'a_0': 1.93e-05 ,
            'K_0': 1.84e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 5120.0 }

class nanal (Mineral):
    def __init__(self):
       formula='NaMg2SiAl5O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'nanal',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -6610270.0 ,
            'S_0': 280.0 ,
            'V_0': 0.00011322 ,
            'Cp:' [672.7, 0.000106, -5992800.0, -4539.9] ,
            'a_0': 2.01e-05 ,
            'K_0': 1.84e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 5120.0 }

class msnal (Mineral):
    def __init__(self):
       formula='MgMg2Si3Mg3O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'msnal',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -6172380.0 ,
            'S_0': 272.5 ,
            'V_0': 0.00011061 ,
            'Cp:' [639.9, 0.00807, -4231200.0, -4487.7] ,
            'a_0': 2.1e-05 ,
            'K_0': 1.85e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 5120.0 }

class fsnal (Mineral):
    def __init__(self):
       formula='FeFe2Si3Fe3O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fsnal',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -4146000.0 ,
            'S_0': 440.2 ,
            'V_0': 0.00011856 ,
            'Cp:' [543.3, 0.055578, -8301600.0, -1581.3] ,
            'a_0': 2.1e-05 ,
            'K_0': 1.85e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 10240.0 }

class canal (Mineral):
    def __init__(self):
       formula='CaMg2Al6O12'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'canal',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -6840000.0 ,
            'S_0': 257.6 ,
            'V_0': 0.00011159 ,
            'Cp:' [591.9, 0.022067, -9204100.0, -2417.0] ,
            'a_0': 1.93e-05 ,
            'K_0': 1.77e+11 ,
            'Kprime_0': 4.0 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 5120.0 }

class per (Mineral):
    def __init__(self):
       formula='MgO'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'per',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -601570.0 ,
            'S_0': 26.5 ,
            'V_0': 1.125e-05 ,
            'Cp:' [60.5, 0.000362, -535800.0, -299.2] ,
            'a_0': 3.11e-05 ,
            'K_0': 1.616e+11 ,
            'Kprime_0': 3.95 ,
            'Kdprime_0': -2.4e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 260.0 }

class fper (Mineral):
    def __init__(self):
       formula='FeO'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'fper',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -262240.0 ,
            'S_0': 58.6 ,
            'V_0': 1.206e-05 ,
            'Cp:' [44.4, 0.00828, -1214200.0, 185.2] ,
            'a_0': 3.22e-05 ,
            'K_0': 1.52e+11 ,
            'Kprime_0': 4.9 ,
            'Kdprime_0': -3.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 680.0 }

class cor (Mineral):
    def __init__(self):
       formula='Al2O3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'cor',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1675250.0 ,
            'S_0': 50.9 ,
            'V_0': 2.558e-05 ,
            'Cp:' [139.5, 0.00589, -2460600.0, -589.2] ,
            'a_0': 1.8e-05 ,
            'K_0': 2.54e+11 ,
            'Kprime_0': 4.34 ,
            'Kdprime_0': -1.7e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 700.0 }

class mcor (Mineral):
    def __init__(self):
       formula='MgSiO3'
       formula = dictionarize_formula(formula)
       self.params = {
            'name': 'mcor',
            'formula': formula,
            'equation_of_state': 'mtait',
            'H_0': -1468000.0 ,
            'S_0': 59.3 ,
            'V_0': 2.635e-05 ,
            'Cp:' [147.8, 0.002015, -2395000.0, -801.8] ,
            'a_0': 2.12e-05 ,
            'K_0': 2.11e+11 ,
            'Kprime_0': 4.55 ,
            'Kdprime_0': -2.2e-11 ,
            'n': sum(formula.values()),
            'molar_mass': formula_mass(formula, atomic_masses)}

       self.uncertainties = {
            'err_H_0': 880.0 }

