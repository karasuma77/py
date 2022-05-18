from PIL import Image
import os

import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

import tkinter 
from tkinter import ANCHOR, filedialog
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
#global img
#画像を開く処理
def input_get():
    global img
    typ = [('', '*')]
    dir = 'C:\\pg'
    img_file = filedialog.askopenfilenames(filetypes = typ, initialdir = dir) 


    # リサイズ前の画像を読み込み
    img = Image.open(img_file[0])
#実行ボタンの処理
def exe():
        (width, height) = (int(txt2.get()),int(txt1.get())) 
        if(len(height)<1):
            messagebox.showerror('error', 'blank :')
        img_resized = img.resize((width, height))
        output = txt3.get()
        if(len(output)<1):
            messagebox.showerror('error', 'blank :save file as')
        if(output not in 'jpg')or(output not in 'png'):
            output = output +'.png'
        print(img)
        img_resized.save(now.strftime('%Y%m%d%H%M%S') + output, quality=90)
        messagebox.showinfo('confirm', 'Image is resized')
   
def len_insert(x):  
    a = txt1.get()

    if((a != '16')and(len(a)<2)):
        lenx = 16*x
        leny = 9*x
        txt1.insert(tkinter.END,lenx)
        txt2.insert(tkinter.END,leny)
    else:
        lenx = int(txt1.get()) + 16*x
        leny = int(txt2.get()) + 9*x
        txt1.delete(0, tkinter.END)
        txt1.insert(tkinter.END,lenx)
        txt2.delete(0,tkinter.END)
        txt2.insert(tkinter.END,leny)
def len_insert2(x,y):
    num = 0
    if txt2.get() == '':
        num = int(txt1.get()) * y / x
        txt2.delete(0, tkinter.END)
        txt2.insert(tkinter.END,int(num))
    else :
        num = int(txt2.get()) * x / y
        txt1.delete(0, tkinter.END)
        txt1.insert(tkinter.END,int(num))
        

def len_delete():
    txt1.delete(0,tkinter.END)
    txt2.delete(0,tkinter.END)

def change():
    a = txt1.get()
    txt1.delete(0, tkinter.END)
    txt1.insert(tkinter.END,txt2.get())
    txt2.delete(0,tkinter.END)
    txt2.insert(tkinter.END,a)
#ウインドウの処理
root = tkinter.Tk()
root.resizable(0,0)
root.geometry('600x300')
root.title('画像リサイズ')


lbl = tkinter.Label(text='height')
#lbl.place(anchor=tkinter.W,relx=0.0, rely=0.2,relwidth=0.25)
lbl.grid(row=0, column=1, columnspan=1, padx=5, pady=10)

txt1 = tkinter.Entry(root)
#txt1.place(anchor=tkinter.W,relx=0.35, rely=0.2, width=140, height=23)
txt1.grid(row=0, column=2, columnspan=1, padx=5, pady=5)

lbl = tkinter.Label(text='width')
#lbl.place(anchor=tkinter.W,relx=0.0,rely=0.25,relwidth=0.25)
lbl.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

txt2 = tkinter.Entry(root)
#txt2.place(anchor=tkinter.W,relx=0.35, rely=0.25, width=140, height=23)
txt2.grid(row=1, column=2, columnspan=1, padx=5, pady=5)

lbl = tkinter.Label(text='Save file as')
#lbl.place(anchor=tkinter.W,relx=0.0, rely=0.4,relwidth=0.25)
lbl.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

txt3 = tkinter.Entry(root)
#txt3.place(anchor=tkinter.W,relx=0.35, rely=0.4, width=140, height=23)
txt3.grid(row=4, column=2, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)

#Ratio adjust
lbl = tkinter.Label(text='Ratio adjust')
#lbl.place(anchor=tkinter.W,relx=0.0, rely=0.50, relwidth=0.25, relheight=0.04)
lbl.grid(row=0, column=4, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)

#1:1
btn = tkinter.Button(root, text="1:1", height = 1,width = 16,command=lambda:len_insert2(1,1))
#btn.place(anchor=tkinter.E,relx=0.5, rely=0.50, relwidth=0.25, relheight=0.04)
btn.grid(row=1, column=3, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)

#4:3
btn = tkinter.Button(root, text="4:3", height = 1,width = 16,command=lambda:len_insert2(4,3))
#btn.place(anchor=tkinter.E,relx=0.75, rely=0.50, relwidth=0.25, relheight=0.04)
btn.grid(row=1, column=4, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)

#16:9
btn = tkinter.Button(root, text="16:9", height = 1,width = 16,command=lambda:len_insert2(16,9))
#btn.place(anchor=tkinter.E,relx=1.0, rely=0.50, relwidth=0.25, relheight=0.04)
btn.grid(row=1, column=5, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)

#CHANGE
btn = tkinter.Button(root, text="h<=>w", height = 1,width = 16,command=change)
btn.grid(row=2, column=3, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)

#preset
#640:360
btn = tkinter.Button(root, text="640:360", height = 1,width = 16,command=lambda:len_insert(40))
#btn.place(anchor=tkinter.W,relx=0.0, rely=0.55, relwidth=0.5, relheight=0.04)
btn.grid(row=2, column=4, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)

#1920:1080
btn = tkinter.Button(root, text="1920:1080", height = 1,width = 16,command=lambda:len_insert(120))
#btn.place(anchor=tkinter.E,relx=1.0, rely=0.55, relwidth=0.5, relheight=0.04)
btn.grid(row=2, column=5, columnspan=1, padx=5, pady=5,sticky=tkinter.W + tkinter.E)


#RESET
btn = tkinter.Button(root, text="RESET", height = 1,width = 8,command=len_delete)
#btn.place(anchor=tkinter.E,relx=0.9, rely=0.225, relwidth=0.2, relheight=0.04)
btn.grid(row=2, column=1, columnspan=2, padx=5, pady=5,sticky=tkinter.W + tkinter.E,rowspan=1)

#画像開く
btn = tkinter.Button(root, text="Open Image", height = 2,width = 16,command=input_get)
btn.grid(row=5, column=0, columnspan=8, padx=5, pady=1,sticky=tkinter.W + tkinter.E,rowspan=1)
#btn.place(anchor=tkinter.CENTER,relx=0.5, rely=0.70, relwidth=1, height=40)
#実行ボタン
btn = tkinter.Button(root, text="Execute", height = 2,width = 16,command=exe)
btn.grid(row=6, column=0, columnspan=10, padx=5, pady=1,sticky=tkinter.W + tkinter.E,rowspan=1)

root.mainloop()

