import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import PyBoolNet.BooleanExpressions

#print PyBoolNet.BooleanExpressions.minimize_espresso("/home/sarah/Schreibtisch/Bachelorarbeit/Erste_Schritte/dahlhaus_neuroplastoma_output_4")
#PyBoolNet.BooleanExpressions.minimize_MCOutput("test.txt")
#PyBoolNet.BooleanExpressions.minimize_many_boolean("Test = TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis | (CentrosomeMat | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex))))))) | !TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !Cytokinesis & (CentrosomeMat & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !CentrosomeMat & (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex))))))); Test2 =TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis | (CentrosomeMat | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex))))))) | !TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !Cytokinesis & (CentrosomeMat & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !CentrosomeMat & (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex)))))));")
#PyBoolNet.BooleanExpressions.minimize_many_boolean("erk = mek & raf; erk = mek & raf;")

PyBoolNet.Tests.Modules.run()

#fname_in = "/home/sarah/Schreibtisch/Bachelorarbeit/Git/PyBoolNet/PyBoolNet/Tests/Files/Input/minimize_boolean_input.bnet"
#primes = PyBoolNet.FileExchange.bnet2primes(fname_in)
#update = "asynchronous"
#init = "INIT TRUE"
#spec = "CTLSPEC AF(EF(AURKAActive))"
#answer, accepting = (PyBoolNet.ModelChecking.check_primes_with_acceptingstates(primes, update, init, spec))
#equation = "Test = " + str(accepting["INITACCEPTING"]) + ";"
#print(equation)
#answer = PyBoolNet.BooleanExpressions.minimize_boolean(equation)


#PyBoolNet.BooleanExpressions.minimize_MCOutput("(False, {'ACCEPTING_SIZE': 16252500.0, 'INIT': 'TRUE', 'INIT_SIZE': 16777200.0, 'INITACCEPTING_SIZE': 16252500.0, 'INITACCEPTING': 'TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis | (CentrosomeMat | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex))))))) | !TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !Cytokinesis & (CentrosomeMat & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !CentrosomeMat & (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex)))))))', 'ACCEPTING': 'TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis | (CentrosomeMat | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex))))))) | !TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !Cytokinesis & (CentrosomeMat & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !CentrosomeMat & (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex)))))))'}), (False, {'ACCEPTING_SIZE': 16252500.0, 'INIT': 'TRUE', 'INIT_SIZE': 16777200.0, 'INITACCEPTING_SIZE': 16252500.0, 'INITACCEPTING': 'TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis | (CentrosomeMat | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex))))))) | !TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !Cytokinesis & (CentrosomeMat & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !CentrosomeMat & (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex)))))))', 'ACCEPTING': 'TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis | (CentrosomeMat | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex))))))) | !TPX2 & (STMNCanAct | (PLK1 | (Cytokinesis & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !Cytokinesis & (CentrosomeMat & (GSK3B | (((AURKAPresent | (PP1 | (AURKAActive | (HCPEB & (GWL_MASTL & (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !GWL_MASTL & ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B)) | !HCPEB & (WEE1 | (CDK1CCNBComplex | ((SpindleAssembly | (AJUBA | (NEDD9 | (hCPEB)))) | !CDC25B))))))) | !MT) | !MTCanAct)) | !CentrosomeMat & (HCPEB & (GWL_MASTL & (CDK1CCNBComplex)) | !HCPEB & (WEE1 | (CDK1CCNBComplex)))))))'})")


#equation = "Test = STMNCanAct & (STMN & ((Cytokinesis & ((MTCanAct | (MT)) | !GSK3B) | !Cytokinesis & (((MTCanAct | (MT)) | !GSK3B) | !CentrosomeMat)) | !PLK1) | !STMN & ((((MTCanAct | (MT)) | !GSK3B) | !CentrosomeMat) | !PLK1)) | !STMNCanAct & (((((MTCanAct | (MT)) | !GSK3B) | !Cytokinesis) | !PLK1) | !STMN);"
#expected = "Test = (!Cytokinesis&!CentrosomeMat) | (!GSK3B) | (MT) | (MTCanAct) | ( !STMN&!CentrosomeMat) | (!PLK1) | (!STMNCanAct&!Cytokinesis) | (!STMNCanAct&!STMN);"
#expression = "(a & b) | a"
#expected = "(a)"
#answer = PyBoolNet.BooleanExpressions.minimize_espresso(expression, Merge=True, Equiv=True, Exact=True, Reduce=True)
#msg = "\nexpected: "+str(expected)
#msg+= "\ngot:      "+str(answer)
#print answer


"(!(ARF & (AUXINS & (IAA & (JKD | !(MGP & (SCR & (SHR & (WOX))) | !MGP & (SCR & (SHR)))) | !IAA & (JKD | (MGP | (((WOX) | !SHR) | !SCR)))) | !AUXINS & (JKD | !(MGP & (SCR & (SHR & (WOX))) | !MGP & (SCR & (SHR))))) | !ARF & (JKD | !(MGP & (SCR & (SHR & (WOX))) | !MGP & (SCR & (SHR))))))"
