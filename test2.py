import tkinter as tk
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
import test
import face_detecting_rec
import img002

import shutil

window = tk.Tk()
window.geometry('300x600')
window.resizable(False, False)
window.title("현대한주")


tklabel = tk.Label(window, text='AI 얼굴인식 이미지/동영상 비식별화 편집')
tklabel.pack()



def open():
    global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    window.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
    ('jpg files', '*.jpg'), ('png files', '*.png'), ('all files', '*.*')))

    # Label(window, text=window.filename).pack() # 파일경로 view
    print(window.filename)
    my_image = ImageTk.PhotoImage(Image.open(window.filename))
    # Label(image=my_image).pack() #사진 view
 



def user():
    open()
    shutil.copy(window.filename, "user_img/user.jpg")
    global label 
    userlabel.pack_forget()
    label = tkinter.Label(window, image=my_image, width=200, height=200) #사진 view
    label.place(x=50, y=370)

def deuser():
    shutil.copy("deuser/deuser.jpg", "user_img/user.jpg")
    label.place_forget()
    userlabel.pack()

label_frame = LabelFrame(window, text="편집", padx=20, pady=20)
label_frame.pack(side='top', fill='both', expand=True, padx=5, pady=5)

button0 = tk.Button(window, overrelief="solid", width=15, text='이미지 비식별화', command=img002.testimg)
button1 = tk.Button(window, overrelief="solid", width=15, text='동영상 비식별화', command=test.testavi)
button2 = tk.Button(window, overrelief="solid", width=15, text='웹 캠 비식별화', command=face_detecting_rec.testcam)
button3 = tk.Button(window, overrelief="solid", width=15, text='유저이미지 등록', command=user)
button4 = tk.Button(window, overrelief="solid", width=15, text='유저이미지 삭제', command=deuser)
button0.place(x=100, y=45)
button1.place(x=100, y=85)
button2.place(x=100, y=125)
button3.place(x=100, y=165)
button4.place(x=100, y=205)

label_frame = LabelFrame(window, text="userimg", padx=20, pady=20)
label_frame.pack(side='bottom', fill='both', expand=True, padx=5, pady=5)

userlabel = tk.Label(window, text='유저 이미지를 등록해주세요.')
userlabel.pack()

window.mainloop()