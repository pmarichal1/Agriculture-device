import os
import sys
import numpy as np
import pickle
import time
#import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

     
class Std_redirector(object):
    def __init__(self,widget):
        self.widget = widget

    def write(self,string):
        self.widget.insert(END,string)
        self.widget.see(END)
    def flush(self):
        pass
   
 
def get_data(label_dict):
    lock_hit=0
    def get_data_loop():
        if os.path.isfile('lock.txt'):
            time.sleep(1)
            lock_hit+=1
        else:
            with open('envfile.data', 'rb') as filehandle:  
                # read the data as binary data stream
                temp_list = pickle.load(filehandle)
                hum_list = pickle.load(filehandle)
            print(f"TEMP {temp_list[-15:]}")
            print(f"Humidity {hum_list[-15:]}")
            temp_elements = np.array(temp_list)
            temp_mean = np.mean(temp_elements, axis=0)
            temp_sd = np.std(temp_elements, axis=0)
            
            hum_elements = np.array(hum_list)
            hum_mean = np.mean(hum_elements, axis=0)
            hum_sd = np.std(hum_elements, axis=0)
    
            print("*****Len Humidity = {:<03.2f},  Len Temp = {:<3.2f}".format(len(hum_list),len(temp_list)))
            print("*****MinH = {:<03.2f},  MinT  = {:<3.2f}".format(min(hum_list), min(temp_list)))
            print('\n')
            label_dict['hum_max_val'].config(text=str(f"{max(hum_list):3.2f}"))
            label_dict['hum_mean_val'].config(text=str(f"{hum_mean:3.2f}"))
            label_dict['hum_sd_val'].config(text=str(f"{hum_sd:3.2f}"))
            label_dict['hum_x_val'].config(text=str(f"{hum_mean + (.5 * hum_sd):2.2f}"))
            label_dict['hum_y_val'].config(text=str(f"{hum_mean - (.5 * hum_sd):2.2f}"))
            label_dict['temp_max_val'].config(text=str(f"{max(temp_list):3.2f}"))
            label_dict['temp_mean_val'].config(text=str(f"{temp_mean:2.2f}"))
            label_dict['temp_sd_val'].config(text=str(f"{temp_sd:3.2f}"))
            label_dict['temp_x_val'].config(text=str(f"{temp_mean + (.5 * temp_sd):2.2f}"))
            label_dict['temp_y_val'].config(text=str(f"{temp_mean - (.5 * temp_sd):2.2f}"))
            label_dict['temp_y_val'].after(3000, get_data_loop)
    get_data_loop()
            
root = Tk()
root.title("Counting Seconds")
label_dict = {}
canvas = Canvas(root, height=800, width=800, bg='#cccccc')
canvas.pack()
frame1 = Frame(root, highlightbackground="black", highlightthickness=4, bd=2)
frame1.place(relx=0.5, rely=0.02, relwidth=0.95, relheight=0.47, anchor='n')

env_stats = Label(frame1, font=("Calibri", 14), bd=3,  text="Environmental Statistics")
env_stats.place(relx=0.5, rely=0.02, relwidth=0.3, relheight=0.05, anchor='n')

hum_max_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Humidity max")
hum_max_txt.place(relx=0.1, rely=0.1, relwidth=0.15, relheight=0.06, anchor='n')
hum_max_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
hum_max_val.place(relx=0.1, rely=0.15, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'hum_max_val' : hum_max_val})

hum_mean_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Humidity Mean")
hum_mean_txt.place(relx=0.3, rely=0.1, relwidth=0.15, relheight=0.06, anchor='n')
hum_mean_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
hum_mean_val.place(relx=0.3, rely=0.15, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'hum_mean_val' : hum_mean_val})

hum_sd_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Humidity SD")
hum_sd_txt.place(relx=0.5, rely=0.1, relwidth=0.15, relheight=0.06, anchor='n')
hum_sd_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
hum_sd_val.place(relx=0.5, rely=0.15, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'hum_sd_val' : hum_sd_val})

hum_x_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Humidity +")
hum_x_txt.place(relx=0.7, rely=0.1, relwidth=0.15, relheight=0.06, anchor='n')
hum_x_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
hum_x_val.place(relx=0.7, rely=0.15, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'hum_x_val' : hum_x_val})

hum_y_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Humidity -")
hum_y_txt.place(relx=0.9, rely=0.1, relwidth=0.15, relheight=0.06, anchor='n')
hum_y_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
hum_y_val.place(relx=0.9, rely=0.15, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'hum_y_val' : hum_y_val})

temp_max_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Temp max")
temp_max_txt.place(relx=0.1, rely=0.3, relwidth=0.15, relheight=0.06, anchor='n')
temp_max_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
temp_max_val.place(relx=0.1, rely=0.35, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'temp_max_val' : temp_max_val})

temp_mean_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Temp Mean")
temp_mean_txt.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.06, anchor='n')
temp_mean_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
temp_mean_val.place(relx=0.3, rely=0.35, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'temp_mean_val' : temp_mean_val})

temp_sd_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Temp SD")
temp_sd_txt.place(relx=0.5, rely=0.3, relwidth=0.15, relheight=0.06, anchor='n')
temp_sd_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
temp_sd_val.place(relx=0.5, rely=0.35, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'temp_sd_val' : temp_sd_val})

temp_x_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Temp +")
temp_x_txt.place(relx=0.7, rely=0.3, relwidth=0.15, relheight=0.06, anchor='n')
temp_x_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
temp_x_val.place(relx=0.7, rely=0.35, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'temp_x_val' : temp_x_val})

temp_y_txt = Label(frame1, font=("Calibri", 12), bd=3,  text="Temp -")
temp_y_txt.place(relx=0.9, rely=0.3, relwidth=0.15, relheight=0.06, anchor='n')
temp_y_val = Label(frame1, font=("Calibri", 12), width=8, relief=SUNKEN, fg="green")
temp_y_val.place(relx=0.9, rely=0.35, relwidth=0.15, relheight=0.06, anchor='n')
label_dict.update({'temp_y_val' : temp_y_val})

button = Button(frame1, font=("Calibri", 12), text='Stop', width=25, command=root.destroy)
button.place(relx=0.5, rely=0.9, relwidth=0.3, relheight=0.1, anchor='n')
        # create a Scrollbar and associate it with txt
frame2 = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=4)
frame2.place(relx=0.5, rely=0.5, relwidth=.95, relheight=0.48, anchor='n')
scrollb2 = Scrollbar(frame2)
scrollb2.pack(side='right', fill='y')

        # create a Text widget
txt2 = Text(frame2, font=("Calibri", 12), borderwidth=3, wrap='word', undo=True, yscrollcommand=scrollb2.set)
txt2.place(relx=0.01, rely=0.07, relwidth=.95, relheight=0.9)
scrollb2.config(command=txt2.yview)
sys.stdout = Std_redirector(txt2)
get_data(label_dict)

root.mainloop()