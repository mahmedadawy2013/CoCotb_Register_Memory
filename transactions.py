import cocotb 
import random
from cocotb_coverage.crv import *

"""***************************************************************************************************************
* Check This Important Link For Coverage And Constraints 
https://cocotb-coverage.readthedocs.io/en/latest/reference.html#cocotb_coverage.crv.Randomized.randomize_with

* This The Source Code With Examples 
https://cocotb-coverage.readthedocs.io/en/latest/_modules/cocotb_coverage/crv.html#Randomized.add_constraint

* Check This Link For Extra Information about Constraints 
https://cocotb-coverage.readthedocs.io/en/latest/introduc

tion.html#constrained-random-verification-features-in-systemverilog
* Another link but it is so important 
https://cocotb-coverage.readthedocs.io/en/latest/tutorials.html

*****************************************************************************************************************"""
class  transactions(Randomized):
    def __init__(self ,name = "TRANSACTIONS"):
        Randomized.__init__(self)
        self.name = name
        self.rst_tb      =  0  
        self.WrEn_tb     =  0
        self.RdEn_tb     =  0
        self.Address_tb  =  0
        self.WrData_tb   =  0
        self.RdData_tb   =  0

        self.add_rand("rst_tb"     , list(range(0,2)     )   ) 
        self.add_rand("WrEn_tb"    , list(range(0,2)     )   ) 
        self.add_rand("RdEn_tb"    , list(range(0,2)     )   )
        self.add_rand("Address_tb" , list(range(0,16)    )   )
        self.add_rand("WrData_tb"  , list(range(0,65536) )   )

        self.add_constraint(lambda RdEn_tb,WrEn_tb :  RdEn_tb!=WrEn_tb)

    """     Another Implementation 
        def Unique(RdEn_tb, WrEn_tb):
            if (RdEn_tb == 0) :
                return WrEn_tb == 1 
            elif (WrEn_tb==0):
                return RdEn_tb == 1 
            elif (RdEn_tb==1) :
                return WrEn_tb == 0 
            elif (WrEn_tb==1):
                return RdEn_tb == 0 
        self.add_constraint(Unique)
    
    """

    def display(self,name = "TRANSACTION"):
        cocotb.log.info("******************"+str(name)+"*******************")
        cocotb.log.info("the Value of rst        is   " + str(self.rst_tb     ))
        cocotb.log.info("the Value of WrEn       is   " + str(self.WrEn_tb    ))
        cocotb.log.info("the Value of RdEn       is   " + str(self.RdEn_tb    ))
        cocotb.log.info("the Value of Address    is   " + str(self.Address_tb ))
        cocotb.log.info("the Value of WrData     is   " + str(self.WrData_tb  ))
        cocotb.log.info("the Value of RdData_tb  is   " + str(self.RdData_tb  ))
        cocotb.log.info("**************************************************")


