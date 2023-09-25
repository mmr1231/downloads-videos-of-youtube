from tkinter import *
from tkinter import messagebox
import pytube
pro=Tk()
        
pro.geometry('700x600+100+10')
pro.config(bg='#AFB1AF')
pro.iconbitmap('mmr.ico')
pro.title('download')
pro.resizable(False,False)

lb1=Label(pro,text='اهلا بك في برنامج تحميل الفديوهات من اليوتبوب',font="Engravers  15"
             ,bg='#000000',fg='#ffffff')
lb1.pack(fill=X )

def save():
    ge=en1.get()
    ms=messagebox.askyesno('التحميل','هل تريد فعلا التحميل')
    if ms  > 0 :
        pytube.YouTube(ge).streams.get_lowest_resolution().download("فديوهات التحميل")






lb3=Label(pro,text= 'لينك الفديو',font='Engravers 20',bg='#AFB1AF')
lb3.place(x=500,y=35,width=100,height=35)
en1=Entry(pro,bg='#AFB1AF',fg='#ffffff',font='bold 15')
en1.place(x=100,y=40,width=300,height=30,)



ph=PhotoImage(file='mmr.png')
lb2=Label(pro,image=ph,)
lb2.place(x=90,y=90,width=500,height=450)



#################################
bu1=Button(pro,text='تحميل',command=save,bg='#ffffff',fg='#000000',font='bold 15')
bu1.place(x=20,y=550,width=650,height=40)


pro.mainloop()




























