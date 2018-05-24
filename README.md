This file runs a PhreeqC simulation with variable parameters and returns the specified selected output as a Pandas framework. The function can be called from any script, in which the ranges of the variables need to be defined. In the PhreeqC source file, the variable values need to be replaced with '%s', e.g.:

SOLUTION 1
    temp      %s
    pH        %s

Function requires:
IPhreeqC (https://wwwbrr.cr.usgs.gov/projects/GWC_coupled/phreeqc/)
Mike Mueller's phreeqpy (http://www.phreeqpy.com/)
Pandas framework (https://pandas.pydata.org/)
