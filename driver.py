from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue

class driver ():

   def __int__(self,name = "DRIVER"):
      self.name = name
      self.driv_mail      = cocotb.queue.Queue()
      self.t_drive        = transactions()
      self.driv_handover  = Event(name=None) 
      
   async def run_driver (self,dut_driver):
      cocotb.log.info("[Driver] STARTING.")
      while(True):
         cocotb.log.info("[Driver] waiting for item ...")
         self.t_drive = await self.driv_mail.get()
         cocotb.log.info("[Driver] Recieved items is  ...")
         await FallingEdge(dut_driver.clk)
         self.t_drive.display("DRIVER")
         dut_driver.rst.value      = self.t_drive.rst_tb
         dut_driver.WrEn.value     = self.t_drive.WrEn_tb
         dut_driver.RdEn.value     = self.t_drive.RdEn_tb
         dut_driver.Address.value  = self.t_drive.Address_tb
         dut_driver.WrData.value   = self.t_drive.WrData_tb  
         self.driv_handover.set() 
