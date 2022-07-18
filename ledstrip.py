import machine
from machine import Pin
from ws2812 import WS2812
import utime


ws = WS2812(machine.Pin(0),8)
pir = Pin(14, Pin.IN, Pin.PULL_DOWN)
buzzer = machine.Pin(15, machine.Pin.OUT)


def ausgabe():
    ws.write()
    utime.sleep_ms(30)
    print(ws[x])
    

for x in range(0,8,1):
    ws[x]= [0,0,0]
    ws.write()
    
pir.value()==0
    

while True:
           
    if pir.value()==1:
        print("Movement detected")
        
        for x in range(0,8,1):
            ws[x]= [255,0,0]
            ausgabe()
            buzzer.toggle()
            
         
        for x in range(0,8,1):
           ws[x]= [170,85,0]
           ausgabe()
           buzzer.toggle()
           
           
        for x in range(0,8,1):
            ws[x]= [85,170,0]
            ausgabe()
            buzzer.toggle()
            
            
        for x in range(0,8,1):
            ws[x]= [0,255,0]
            ausgabe()
            buzzer.toggle()
        
                   
        for x in range(0,8,1):
            ws[x]= [0,170,85]
            ausgabe()
            buzzer.toggle()
            
            
        for x in range(0,8,1):
            ws[x]= [0,85,170]
            ausgabe()
            buzzer.toggle()
            
    
        for x in range(0,8,1):
            ws[x]= [0,0,255]
            ausgabe()
            buzzer.toggle()
            
            
        for x in range(0,8,1):
            ws[x]= [85,0,170]
            ausgabe()
            buzzer.toggle()
            
        for x in range(0,8,1):
            ws[x]= [170,0,85]
            ausgabe()
            buzzer.toggle()
            
    
        for x in range(0,8,1):
            ws[x]= [0,0,0]
            ausgabe()
            buzzer.toggle()
            
        
        utime.sleep_ms(1000)
             
        
    else:
        print("Waiting for movement")
        utime.sleep_ms(1000)
            
    
        
    
            
