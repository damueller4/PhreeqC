#PhreeqC_CallWithVariables.py
#Author: Daniel Richard Mueller, damueller4@github, git@lynxtech.de

"""
The function run_simulation runs a PhreeqC simulation with variable parameters and returns the specified
selected output as a Pandas framework. In the PhreeqC source file, the variable values need to be replaced
with '%s'. Function requires IPhreeqC, phreeqpy and the Pandas framework.

Input
-----
file_name:		specify full path to PhreeqC source file
dbase:			specify full path to database	
lib:			specify full path to Python shared object library (libiphreeqc.so), which is part of IPhreeqC 
params:			specify variable parameters as lists, in order of appearance in the source file 

Returns
-------
data:			full selected output
data_no_init:	selected output without initial solution	
"""

#import libraries
import phreeqpy.iphreeqc.phreeqc_dll as phreeqc_mod
import sys
import pandas

def run_simulation(file_name,dbase,lib,*params):
	
	#ensure py2 compatibility
	if sys.version_info[0] == 2:
		range = xrange
	
	#user feedback
	print "Simulation initiated. Parameters:", params
	
	#define PhreeqC input
	pqc_input_file = open(file_name, "r")
	pqc_readout = pqc_input_file.read()
	pqc_input = pqc_readout % params
	pqc_input_file.close()
	
	#run simulation
	phreeqc = phreeqc_mod.IPhreeqc(lib)
	phreeqc.load_database(dbase)
	phreeqc.run_string(pqc_input)
	
	#get output
	data = pandas.DataFrame(phreeqc.get_selected_output_array())
	data.columns = data.iloc[0]
	data = data[1:]
	data_no_init = data[data.state != "i_soln"]
	
	#return pandas frames with data and data without initial solution
	return data, data_no_init
