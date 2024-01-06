from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue
from cocotb_coverage.coverage import *


@CoverPoint("top.RdData_tb"   , vname="RdData_tb"   , bins=list(range(0, 2 ** 16  ))) 
def sample(RdData_tb):
    pass

class subscriber() :
   
    def __init__(self ,name = "SUBSCRIBER"): 
       self.name               = name
       self.t_sub              = transactions()
       self.sub_mail           = cocotb.queue.Queue()

    async def run_subscriber (self) : 
        while(True):
            self.t_sub = transactions()
            cocotb.log.info("[subscriber] receiving from monitor..... ") 
            self.t_sub = await self.sub_mail.get() 
            self.t_sub.display("SUBSCRIBER")
            cocotb.log.info("[subscriber] receiving from monitor..... ") 
            sample(self.t_sub.RdData_tb)
 
    def coverage_report(self):
        RdData_tb       = coverage_db["top.RdData_tb"].coverage          
        RdData_tb_p     = coverage_db["top.RdData_tb"].cover_percentage  
        cocotb.log.info("The RdData_tb   coverage is : "+str(RdData_tb))
        cocotb.log.info("The RdData_tb_p coverage percentage is : "+str(RdData_tb_p))

                