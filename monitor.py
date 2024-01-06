from cocotb.triggers import *
from transactions import *
import cocotb
import cocotb.queue

class monitor ():
   t_monitor    = transactions()
   mon_mail_s   = cocotb.queue.Queue()
   mon_mail_su  = cocotb.queue.Queue()
   def __int__(self,name = "MONITOR"):
        self.name= name
      
   async def run_monitor (self,dut_monitor):
      cocotb.log.info("[Monitor] STARTING.")
      await RisingEdge(dut_monitor.clk)
      while(True):
        cocotb.log.info("[Monitor] waiting for item ...")
        await RisingEdge(dut_monitor.clk)
        await ReadOnly()
        self.t_monitor.rst_tb        =   int(dut_monitor.rst)
        self.t_monitor.WrEn_tb       =   int(dut_monitor.WrEn)    
        self.t_monitor.RdEn_tb       =   int(dut_monitor.RdEn.value )    
        self.t_monitor.Address_tb    =   int(dut_monitor.Address.value  )
        self.t_monitor.WrData_tb     =   int(dut_monitor.WrData.value )
        self.t_monitor.RdData_tb     =   int(dut_monitor.RdData.value  )
        self.t_monitor.display("MONITOR")  
        await self.mon_mail_s.put(self.t_monitor)  
        await self.mon_mail_su.put(self.t_monitor)
