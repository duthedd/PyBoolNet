import subprocess
import glob
import os.path
import sys
import PyBoolNet
import re
import ast


BASE = os.path.abspath(os.path.join(os.path.dirname(__file__)))
BASE = os.path.normpath(BASE)
config = PyBoolNet.Utility.Misc.myconfigparser.SafeConfigParser()
config.read( os.path.join(BASE, "Dependencies", "settings.cfg") )
EQNTOTT_CMD = os.path.normpath(os.path.join( BASE, "Dependencies", config.get("Executables", "eqntott") ))
ESPRESSO_CMD = os.path.normpath(os.path.join( BASE, "Dependencies", config.get("Executables", "espresso") ))



def _eqntott_error(eqntott, eqntott_out, eqntott_err):
    """
    raises exception for eqntott
    """
    if not (eqntott.returncode == 0):
        print(eqntott_out)
        print(eqntott_err)
        print('\nCall to "eqntott" resulted in return code %i'%eqntott.returncode)
        raise Exception



def _espresso_error(espresso, espresso_out, espresso_err):
    """
    raises exception for espresso
    """
    if not (espresso.returncode == 0):
        print(espresso_out)
        print(espresso_err)
        print('\nCall to "espresso" resulted in return code %i'%espresso.returncode)
        raise Exception



def run_eqntott(eqntott_cmd, eqntott_in):
    eqntott = subprocess.Popen(eqntott_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    eqntott_out, eqntott_err = eqntott.communicate(input=eqntott_in)
    eqntott.stdin.close()
    _eqntott_error(eqntott, eqntott_out, eqntott_err)
    return(eqntott_out)



def run_espresso(espresso_cmd, eqntott_out):
    espresso = subprocess.Popen(espresso_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    espresso_out, espresso_err = espresso.communicate(input=eqntott_out.encode())
    espresso.stdin.close()
    _espresso_error(espresso, espresso_out, espresso_err)
    return(espresso_out)



def minimize_espresso(Equation, Outputfile=None, Summary=False, Merge=False, Echo=False, Equiv=False, Exact=False, Stats=False, Trace=False, Reduce=False, NoRedundancy=False):
    """
    Tries to minimize a given boolean expression utilizing the heuristic minimization algorithm
    espresso and eqntott for its input preparation. Resulting equation is saved in file if filename
    for output is specified. The argument *Equation* may be either the name of the input file containing
    the boolean expression or the string representing the expression itself.

    **arguments**:
       * *Equation*: name of file containing the expression or string contents of file
       * *Outputfile*: name of the file to write the output to
       * *summary*: provides a short summary including initial and final cost of the function
       * *Merge*: performs distance-1 merge on input, useful if very large
       * *Echo*: echoes the function to standard output
       * *Equiv*: identifies equivalent output variables
       * *Exact*: performs exact minimization algorithm, guarantees minimum number of product terms and heuristically minimizes number of literals, potentially expensive
       * *Stats*: provides simple statistics on the size of the function
       * *Trace*: produces a trace showing the program execution, including current cost of function
       * *Reduce*: :ref:`installation_eqntott` tries to reduce the size of the truth table by merging minterms
       * *NoRedundancy*: forces *eqntott* to produce a truth table with no redundant terms


    **returns**:
       * *Minimized*: minimized result

    **example**::

          >>> minimized = minimize_boolean("bool_function.txt", "minimized_function.txt" )
    """
    #file input
    if (os.path.exists(Equation)):
        with open(Equation, 'r') as fname:
            Equation = fname.read()
    assert(type(Equation) == str)
    forbidden = ["False", "FALSE", "True", "TRUE", "Zero", "ZERO", "One", "ONE"]
    assert(all(var not in Equation for var in forbidden))
    AddName = False
    AddColon = False
    if not ("=" in Equation):
        Equation = "Test = " + Equation
        AddName = True
    if not (";" in Equation):
        Equation = Equation + ";"
        AddColon = True

    eqntott_cmd = [EQNTOTT_CMD, '-f', '-l']
    espresso_cmd =[ESPRESSO_CMD, '-o', 'eqntott']
    eqntott_in = None
    espresso_out = ''
    PLA_Name = 'Standard Input'

    if Summary == True:
        espresso_cmd += ['-s']
    if Merge == True:
        espresso_cmd += ['-Dd1merge']
    if Echo == True:
        espresso_cmd += ['-Decho']
    if Equiv == True:
        espresso_cmd += ['-Dequiv']
    if Exact == True:
        espresso_cmd += ['-Dexact']
    if Stats == True:
        espresso_cmd += ['-Dstats']
    if Trace == True:
        espresso_cmd += ['-t']
    if Reduce == True:
        eqntott_cmd += ['-r']
    if NoRedundancy == True:
        eqntott_cmd += ['-R']

    eqntott_cmd += ['/dev/stdin']
    eqntott_in = Equation
    eqntott_out = run_eqntott(eqntott_cmd, eqntott_in)

    if int(re.search(r'\.i\s\d+', eqntott_out).group().strip(".i "))>1:
        espresso_out = run_espresso(espresso_cmd, eqntott_out)
        espresso_out = re.sub(r'\.na .*\n', '\n', espresso_out)
    else:
        espresso_out = Equation

    if (AddName == True):
        espresso_out = espresso_out.replace('Test = ', '')
    if (AddColon == True):
        espresso_out = espresso_out.replace(';', '')

    if (Outputfile == None):
        return(espresso_out.replace("\n", "").replace("\s", "").replace("\t", ""))
    else:
        with open(Outputfile, 'w') as results:
            results.write(espresso_out)
