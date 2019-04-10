#!/usr/bin/env python3
# -*- coding: utf-8 
import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as plt
import pickle
import time

print(sys.version_info)
print(platform.python_version())
print(platform.platform())

lock_hit=0
while(1):
    # check if lock file exist since it means file is being updated and we should not access it
    if os.path.isfile('lock.txt'):
        time.sleep(1)
        lock_hit+=1
    else:
        with open('envfile.data', 'rb') as filehandle:  
            # read the data as binary data stream
            temp_list = pickle.load(filehandle)
            hum_list = pickle.load(filehandle)
        print("Lhum = %d,  ltemp = %d "%(len(hum_list), len(temp_list)))
       
        temp_elements = np.array(temp_list)
        temp_mean = np.mean(temp_elements, axis=0)
        temp_sd = np.std(temp_elements, axis=0)
        print("******TEMP mean =%0.2f   dev=%0.2f x=%0.2f"%(temp_mean, temp_sd, temp_mean + 1 * temp_sd))

        temp_final_list = [x for x in temp_list if (x < (temp_mean+.5) + (1 * temp_sd))]
        print("******TEMP mean =%0.2f   dev=%0.2f x=%0.2f"%(temp_mean, temp_sd, temp_mean - 1 * temp_sd))
        temp_final_list = [x for x in temp_final_list if (x > (temp_mean-.5) - (1 * temp_sd))]
        yarr1 = list(range(len(temp_final_list)))

        hum_elements = np.array(hum_list)
        hum_mean = np.mean(hum_elements, axis=0)
        hum_sd = np.std(hum_elements, axis=0)
        print("******HUM mean =%0.2f   dev=%0.2f x=%0.2f"%(hum_mean, hum_sd, hum_mean + 1 * hum_sd))
        hum_final_list = [x for x in hum_list if (x < hum_mean + 2 * hum_sd)]
        print("******HUM mean =%0.2f   dev=%0.2f x=%0.2f"%(hum_mean, hum_sd, hum_mean - 1 * hum_sd))
        hum_final_list = [x for x in hum_final_list if (x > hum_mean - 2 * hum_sd)]
        yarr = list(range(len(hum_final_list)))
        print("Lhum = %d,  ltemp = %d"%(len(hum_final_list), len(temp_final_list)))        
        
        plt.xlabel("Time (s)")
        plt.ylabel("Temp (F)")
        plt.plot(yarr, hum_final_list, yarr1, temp_final_list)
        plt.draw()
        print("---Plot graph finish---    Lock hit = %d" %(lock_hit))
        plt.ion()
        plt.show()
        time.sleep(3)
        plt.pause(0.0001)
        plt.clf()

