
module RegFile #(parameter WIDTH = 32, DEPTH = 16, ADDR = 4 )

(
input wire             clk,
input wire             rst,
input wire             WrEn,
input wire             RdEn,
input wire [ADDR-1:0]  Address,
input wire [WIDTH-1:0] WrData,
output reg [WIDTH-1:0] RdData

);

integer I ; 
  
// register file of 8 registers each of 16 bits width
reg [WIDTH-1:0] regArr [DEPTH-1:0] ;    

always @(posedge clk or negedge rst)
 begin
   if(!rst)  // Asynchronous active low reset 
    begin
      for (I=0 ; I < DEPTH ; I = I +1)
        begin
          regArr[I] <= 0 ;
        end
      RdData <= 0 ; 
      /*
      regArr[0] <= 0 ;
      regArr[1] <= 0 ;
      regArr[2] <= 0 ;
      regArr[3] <= 0 ;
      regArr[4] <= 0 ;
      regArr[5] <= 0 ;
      regArr[6] <= 0 ;
      regArr[7] <= 0 ;
      */
     end
   else if (WrEn && !RdEn) // Register Write Operation
     begin
      regArr[Address] <= WrData ;
     end
   else if (RdEn && !WrEn) // Register Read Operation
     begin    
       RdData <= regArr[Address] ;
     end        
  end
endmodule