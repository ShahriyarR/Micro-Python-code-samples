### RGB Led (common katod) with Micro Python ###

### Blinking RGB Led ###

import pyb

LEDx1 = pyb.Pin('X1', pyb.Pin.OUT_PP, pyb.Pin.PULL_UP)
LEDx2 = pyb.Pin('X2', pyb.Pin.OUT_PP, pyb.Pin.PULL_UP)
LEDx3 = pyb.Pin('X3', pyb.Pin.OUT_PP, pyb.Pin.PULL_UP)


LEDx1.low()
LEDx2.low()
LEDx3.low()

try:
    while True:    
        
        LEDx1.value(False)
        pyb.delay(100)
        LEDx2.value(False)
        pyb.delay(100)
        LEDx3.value(False)
        pyb.delay(100)
        
        LEDx1.value(True)
        pyb.delay(100)
        LEDx2.value(True)
        pyb.delay(100)
        LEDx3.value(True)
        pyb.delay(100)
        

except:
    LEDx1.value(False)
    LEDx2.value(False)
    LEDx3.value(False)