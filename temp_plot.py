#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:42:40 2019

@author: pi
"""

# Import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

with open('envfile.data', 'rb') as filehandle:  
    # read the data as binary data stream
    temp_list = pickle.load(filehandle)
    hum_list = pickle.load(filehandle)
#temp_list = [10,10,10,13]
#hum_list = [5,5,5,5,8]
print(f"Lhum = {len(hum_list)},  ltemp = {len(temp_list)}")

#print(temp_list)
#print(hum_list)
#xarr = [0,65,68,69,234,65,65,70,67,68,69,56,5,40,98,65,65,68,69,65,65,70,67,68,69,56,5,40,98,65]

temp_elements = np.array(temp_list)
temp_mean = np.mean(temp_elements, axis=0)
temp_sd = np.std(temp_elements, axis=0)
print(f"******TEMP mean = {temp_mean}   dev={temp_sd} x = x={temp_mean + 1 * temp_sd}")
temp_final_list = [x for x in temp_list if (x < (temp_mean+.5) + (1 * temp_sd))]
print(f"******TEMP mean = {temp_mean}   dev={temp_sd} x = x={temp_mean - (1 * temp_sd)}")
temp_final_list = [x for x in temp_final_list if (x > (temp_mean-.5) - (1 * temp_sd))]
yarr1 = list(range(len(temp_final_list)))

hum_elements = np.array(hum_list)
hum_mean = np.mean(hum_elements, axis=0)
hum_sd = np.std(hum_elements, axis=0)
print(f"******HUM mean = {hum_mean}   dev={hum_sd} x={hum_mean + 2 * hum_sd}")
hum_final_list = [x for x in hum_list if (x < hum_mean + 2 * hum_sd)]
print(f"******HUM mean = {hum_mean}   dev={hum_sd} x={hum_mean - 2 * hum_sd}")
hum_final_list = [x for x in hum_final_list if (x > hum_mean - 2 * hum_sd)]
yarr = list(range(len(hum_final_list)))
print(f"Lhum = {len(hum_final_list)},  ltemp = {len(temp_final_list)}")


plt.xlabel("Time (s)")
plt.ylabel("Temp (F)")
plt.plot(yarr, hum_final_list, yarr1, temp_final_list)
plt.draw()
print("---Plot graph finish---")
plt.ion()
plt.show()
plt.pause(1)
input("Press Enter")
