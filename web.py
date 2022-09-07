#!/usr/bin/env python
# coding: utf-8

# In[11]:


import socket,ipaddress,threading
import struct
import array
import pickle
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import pandas as pd


# In[2]:


#import h2o
#h2o.init()


# In[19]:


window = Tk()
window.resizable(0,0)
window.title("Pharmaquick DRS")
window.geometry('420x550')
Label(window, text="Drug Recommendation System",font=("Arial", 16,"bold")).pack()
width = 420
height = 190
img = Image.open("drugs2.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
Label(image=photoImg).pack()
Label(window, text="Select Gender of patient",font=("Arial", 12,"bold")).place(relx = 0.0, rely = 0.405)
pos = 0.45
sex = StringVar()
sex.set("")

bp = StringVar()
bp.set("")

cl = StringVar()
cl.set("")



rb = Radiobutton(window, text='Male',font=("Arial", 12), variable = sex, value='M')
rb.select()
rb.place(relx = 0.0, rely = pos)

Radiobutton(window, text='Female', font=("Arial", 12), variable = sex, value='F').place(relx = 0.2, rely = pos)
selected_gender = sex.get()

Label(window, text="Enter Age of patient",font=("Arial", 12,"bold")).place(relx = 0.0, rely = pos+0.08)
txt = Entry(window, width = 10)
txt.place(relx = 0.0, rely = pos + 0.13)
age = 0
def clicked():
    age = txt.get()
bt = Button(window, text = 'Enter', command = clicked).place(relx = 0.15, rely = pos + 0.125)

Label(window, text="Select Blood Pressure level of patient",font=("Arial", 12,"bold")).place(relx = 0.0, rely = pos+0.2)

rb = Radiobutton(window, text='Low',font=("Arial", 12), variable = bp, value='LOW')
rb.select()
rb.place(relx = 0.0, rely = pos+0.24)

Radiobutton(window, text='Medium', font=("Arial", 12), variable = bp, value='MEDIUM').place(relx = 0.2, rely = pos+ 0.24)

Radiobutton(window, text='High', font=("Arial", 12), variable = bp, value='HIGH').place(relx = 0.5, rely = pos+ 0.24)
selected_bp = bp.get()

Label(window, text="Select cholesterol level of patient",font=("Arial", 12,"bold")).place(relx = 0.0, rely = pos+0.29)

rb = Radiobutton(window, text='Normal',font=("Arial", 12), variable = cl, value='NORMAL')
rb.select()
rb.place(relx = 0.0, rely = pos+0.33)

Radiobutton(window, text='High', font=("Arial", 12), variable = cl, value='HIGH').place(relx = 0.2, rely = pos+ 0.33)

selected_bp = cl.get()

Label(window, text="Enter Na to K ratio of patient",font=("Arial", 12,"bold")).place(relx = 0.0, rely = pos+0.38)
txt1 = Entry(window, width = 10)
txt1.place(relx = 0.0, rely = pos + 0.42)
natok = 0
def clicked1():
    natok = txt1.get()
bt = Button(window, text = 'Enter', command = clicked1).place(relx = 0.15, rely = pos + 0.415)


def clicked3():
    #model = h2o.load_model('gbm-model')
    filename = 'gc-model.sav'
    model = pickle.load(open(filename, 'rb'))

    data = {'Age': [txt.get()],
        'Sex': [sex.get()],
        'BP': [bp.get()],
        'Cholesterol': [cl.get()],
        'Na_to_K': [txt1.get()]}
    label_dic = {'M': 1, 'F': 2, 'LOW': 1, 'MEDIUM': 2, 'HIGH': 3, 'NORMAL': 2}
    
    df = pd.DataFrame(data)
    df = df.replace({'Sex': label_dic})
    df = df.replace({'BP': label_dic})
    df = df.replace({'Cholesterol': label_dic})
    #print(df.head())
    #pred = model.predict(h2o.H2OFrame(df))
    pred = model.predict(df)
    messagebox.showinfo('Recommendation', 'The recommended drug for this patient is '+ str(pred))
Button(text = 'Recommend a drug!', command = clicked3).pack(side = 'bottom')

window.mainloop()


# In[ ]:





# In[ ]:




