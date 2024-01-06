from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue


class generator() :
   
    def __init__(self ,join_any,name = "GENERATOR"): 
       self.name             = name
       self.t_gen            = transactions()
       self.gen_mail         = cocotb.queue.Queue()
       self.gen_handover     = Event(name=None) 
       self.join_any         = join_any

    async def run_generator (self,dut_generator) : 
        iteration_number = 5000 ; 
        for i in range(iteration_number): 
            self.gen_handover.clear() 
            if (i == 0 ) :
                await self.reset_sequence()


            else :
                await self.write_sequence()
                await self.read_sequence()

        await FallingEdge(dut_generator.clk)
        self.join_any.set()

    """ ************* **************** Sequence Generation ****************** ***************"""
    async def reset_sequence (self):
        self.t_gen = transactions()
        self.t_gen.randomize_with(lambda rst_tb: rst_tb == 0  )
        self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ") 
        await self.gen_mail.put(self.t_gen)  
        await self.gen_handover.wait()      

    async def write_sequence(self) :
        for i in range(16) :
            self.gen_handover.clear() 
            self.t_gen = transactions()
            self.t_gen.randomize_with(lambda rst_tb :rst_tb == 1 ,lambda WrEn_tb :WrEn_tb  == 1 )
            self.t_gen.display("GENERATOR")
            cocotb.log.info("[Generator] Sending To The Driver..... ")
            await self.gen_mail.put(self.t_gen) 
            await self.gen_handover.wait()

    async def read_sequence(self) :
        for i in range(16) :
            self.gen_handover.clear() 
            self.t_gen = transactions()
            self.t_gen.randomize_with(lambda rst_tb :rst_tb == 1 ,lambda RdEn_tb :RdEn_tb  == 1 )
            self.t_gen.display("GENERATOR")
            cocotb.log.info("[Generator] Sending To The Driver..... ")
            await self.gen_mail.put(self.t_gen) 
            await self.gen_handover.wait()
                