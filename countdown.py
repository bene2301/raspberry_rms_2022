import machine
from machine import Pin
import utime
from ws2812 import WS2812

display_list = [17,16,14,13,12,18,19]
dotPin=15
display_obj = []

button = machine.Pin(10, machine.Pin.IN)
ws = WS2812(machine.Pin(0),8)


for seg in display_list:
    display_obj.append(Pin(seg, Pin.OUT))

dot_obj=Pin(dotPin, Pin.OUT)


arrSeg = [[1,1,1,1,1,1,0],\
          [0,1,1,0,0,0,0],\
          [1,1,0,1,1,0,1],\
          [1,1,1,1,0,0,1],\
          [0,1,1,0,0,1,1],\
          [1,0,1,1,0,1,1],\
          [1,0,1,1,1,1,1],\
          [1,1,1,0,0,0,0],\
          [1,1,1,1,1,1,1],\
          [1,1,1,1,0,1,1],\
          [0,0,0,0,0,0,0]]

def SegDisplay(toDisplay):
    numDisplay = int(toDisplay.replace(".", ""))
    for a in range(7):
        display_obj[a].value(arrSeg[numDisplay][a])
    
    if toDisplay.count(".") == 1:
        dot_obj.value(1)
    else:
        dot_obj.value(0)


def ausgabe():
    ws.write()
    utime.sleep_ms(300)
    print(ws[x])

while True:    
    if button.value() == 0:
        for i in range(9,-1,-1):
            utime.sleep_ms(1000)
            SegDisplay(str(i))
            print(i)
            if i == 0:
                for x in range(0,8,1):
                    ws[x]= [255,0,0]
                    ausgabe()
                
                
                for x in range(0,8,1):
                   ws[x]= [170,85,0]
                   ausgabe()
                              
                   
                for x in range(0,8,1):
                    ws[x]= [85,170,0]
                    ausgabe()
                    
                          
                for x in range(0,8,1):
                    ws[x]= [0,255,0]
                    ausgabe()
                
                    
                for x in range(0,8,1):
                    ws[x]= [0,170,85]
                    ausgabe() 
                
                    
                for x in range(0,8,1):
                    ws[x]= [0,85,170]
                    ausgabe()
                    
            
                for x in range(0,8,1):
                    ws[x]= [0,0,255]
                    ausgabe()
                    
                            
                for x in range(0,8,1):
                    ws[x]= [85,0,170]
                    ausgabe()
                    
                            
                for x in range(0,8,1):
                    ws[x]= [170,0,85]
                    ausgabe()
                    
                     
                for x in range(0,8,1):
                    ws[x]= [0,0,0]
                    ausgabe()

