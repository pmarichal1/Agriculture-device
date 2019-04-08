#!/usr/bin/env python3
#############################################################################
# Filename    : DHT11.py
# Description :	read the temperature and humidity data of DHT11
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
import Blink
import LCD
import pickle
import sonar

DHTPin = 15     #define the pin of DHT11
# main loop
def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    sonar.sonar_setup()
    sumCnt = 0              #number of reading times
    Blink.setup_led()
    temperature_list = []
    humidity_list = []
    while(True):
        sumCnt += 1         #counting number of reading times
        chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        print ("The sumCnt is : %d, \t chk    : %d"%(sumCnt,chk))
        if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            print("DHT11,OK!")
        elif(chk is dht.DHTLIB_ERROR_CHECKSUM): #data check has errors
            print("DHTLIB_ERROR_CHECKSUM!!")
        elif(chk is dht.DHTLIB_ERROR_TIMEOUT):  #reading DHT times out
            print("DHTLIB_ERROR_TIMEOUT!")
        else:               #other errors
            print("Other error!")
        dht.temperature = dht.temperature *(9/5) +32    
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
        time.sleep(2)
        Blink.flash_led()
        #print temp and humidity to LCD
        temperature = float("%.2f" % dht.temperature)

        if temperature > 0 and dht.humidity > 0:
            LCD.run_lcd("Temp ", dht.temperature,"Humidity ", dht.humidity)
            print(len(temperature_list))
            if len(temperature_list) > 200:
                temperature_list.pop(0)
                humidity_list.pop(0)
            temperature_list.extend([temperature])
            humidity_list.extend([dht.humidity])
            with open('envfile.data', 'wb') as filehandle:  
                # store the data as binary data stream
                pickle.dump(temperature_list, filehandle)
                pickle.dump(humidity_list, filehandle)

        print(temperature_list)
        print(humidity_list)
        distance = sonar.sonar()
        time.sleep(2) 
        #LCD.run_lcd("Sonar",distance, "Sonar ", distance)

        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        Blink.destroy_led()
        exit()  

