import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import cv2

def input1_clicked():
    fTyp = [("","*.png")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)

def input2_clicked():
    fTyp = [("","*.png")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file2.set(filepath)

def get_diff():
    img1 = cv2.imread(file1.get(),1)
    img2 = cv2.imread(file2.get(),1)

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

    fgmask = fgbg.apply(img1)
    fgmask = fgbg.apply(img2)

    cv2.imshow('frame',fgmask)

    bg_diff_path = 'image/diff.png'
    cv2.imwrite(bg_diff_path,fgmask)   


if __name__ == '__main__':

    root = Tk()
    root.title('ImageDiff')
    root.resizable(False, False)

    #Frame1
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    #Input Button1
    input_button1 = ttk.Button(root, text=u'Input', command=input1_clicked)
    input_button1.grid(row=0, column=3)
    #Label1
    s1 = StringVar()
    s1.set('Image1')
    label1 = ttk.Label(frame1, textvariable=s1)
    label1.grid(row=0, column=0)
    #Input1 filepath
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    #Frame2
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=1)

    #Input Button2
    input_button2 = ttk.Button(root, text=u'Input', command=input2_clicked)
    input_button2.grid(row=1, column=3)
    #Label2
    s2 = StringVar()
    s2.set('Image2')
    label2 = ttk.Label(frame2, textvariable=s2)
    label2.grid(row=1, column=0)
    #Input2 filepath
    file2 = StringVar()
    file2_entry = ttk.Entry(frame2, textvariable=file2, width=50)
    file2_entry.grid(row=1, column=2)

    #Frame3
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=2)

    #Diff button
    diff_button = ttk.Button(frame3, text='Diff', command=get_diff)
    diff_button.pack(side=LEFT)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    root.mainloop()
