from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue


class Scoreboard() :
   
    def __init__(self ,name = "SCOREBOARD"): 
       self.name               = name
       self.t_score            = transactions()
       self.score_mail         = cocotb.queue.Queue()
       self.passed_test_cases  = 0
       self.failed_test_cases  = 0
       self.read_test_cases    = 0 
       self.write_test_cases   = 0 
       self.reset_test_cases   = 0
       self.golden_memory      = [0] * 16
       self.golgen_output      = 0



    async def run_scoreboard (self) : 
        while(True):
            self.t_score = transactions()
            cocotb.log.info("[Scoreboard] receiving from monitor..... ") 
            self.t_score = await self.score_mail.get() 
            self.t_score.display("SCOREBOARD")
            """**************************  TEST CASES **************************"""
            if self.t_score.rst_tb == 0:
                self.reset_test_case()
            elif self.t_score.WrEn_tb == 1:
                self.write_test_case()    
            elif self.t_score.RdEn_tb == 1:
                self.read_test_case()
            """******************************************************************"""


    def reset_test_case (self) :
        self.reset_test_cases +=1
        for i in range(16):
            self.golden_memory[i] = 0
        self.golgen_output = 0
        if self.t_score.RdData_tb == self.golgen_output:
            self.passed_test_cases += 1
            cocotb.log.info("Reset Test Case Passed ")
        else:
            self.failed_test_cases += 1
            cocotb.log.info("Reset Test Case Failed ")

    def write_test_case(self) :
        self.write_test_cases += 1
        self.golden_memory[self.t_score.Address_tb] = self.t_score.WrData_tb

        if self.t_score.RdData_tb == self.golgen_output:
            self.passed_test_cases += 1
            cocotb.log.info("Write Test Case Passed ")
        else:
            self.failed_test_cases += 1
            cocotb.log.info("Write Test Case Failed ")


    def read_test_case(self):
        self.read_test_cases += 1 
        self.golgen_output = self.golden_memory[self.t_score.Address_tb]

        if self.t_score.RdData_tb == self.golgen_output:
            self.passed_test_cases += 1
            cocotb.log.info("Read Test Case Passed ")
        else:
            self.failed_test_cases += 1
            cocotb.log.info("Read Test Case Failed ")


    def report_test_cases(self):
        self.total_test_cases = self.passed_test_cases + self.failed_test_cases
        cocotb.log.info("The Number Of Total  Test Cases is :  " + str(self.total_test_cases)) 
        cocotb.log.info("The Number Of Rest   Test Cases is :  " + str(self.reset_test_cases))    
        cocotb.log.info("The Number Of Read   Test Cases is :  " + str(self.read_test_cases))  
        cocotb.log.info("The Number Of Write  Test Cases is :  " + str(self.write_test_cases)) 
        cocotb.log.info("The Number Of Passed Test Cases is :  " + str(self.passed_test_cases))  
        cocotb.log.info("The Number Of Passed Test Cases is :  " + str(self.failed_test_cases))           


                