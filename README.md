This file runs a PhreeqC simulation with variable parameters and returns the specified selected output as a Pandas framework. The function can be called from any script, in which the ranges of the variables need to be defined. In the PhreeqC source file, the variable values need to be replaced with '%s', e.g. to vary temperature, pH, mass and reactive surface of quartz:

SOLUTION 1
    temp      %s
    pH        %s
    pe        3.3
    redox     pe
    units     mol/kgw
    density   1.014
    -water    1 # kg

KINETICS 1
-steps       31536000 in 365 steps # seconds 604800
-step_divide 1
-runge_kutta 3
-bad_step_max 1000
Quartz
     -formula  SiO2  1
     -m        %s
     -m0       0.00824
     -parms    %s 5e-11
     -tol      1e-08

Function requires:
IPhreeqC https://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/
Mike Mueller's phreeqpy http://www.phreeqpy.com/
Pandas framework https://pandas.pydata.org/
