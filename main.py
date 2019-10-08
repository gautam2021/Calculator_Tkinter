from tkinter import *
import time

root=Tk()
root.configure(bg='#ffffff')
blank_space=' '
root.iconbitmap('title.ico')
root.geometry('300x300+800+200')
root.title(20*blank_space+"Calculator")
root.resizable(0,0)    # can't change the size of main window


# all functions are going to be declared here which was called by command ,

def enter_number(x):
    if entry_box.get()=='0':
        if x=='.':
            entry_box.insert(1,'.')
        else:
            entry_box.delete(0,END)
            entry_box.insert(0,str(x))
    else:
        length=len(entry_box.get())
        entry_box.insert(length,str(x))









result=0
history=[]    # we will store the last few calculation 
def equal_btn():
    content=entry_box.get()
    result=eval(content)
    entry_box.delete(0,END)
    entry_box.insert(0,result)
    history.append(content)
    history.reverse()  

    status.configure(text='History ' + '| '.join(history[:4]) ,bg='#5c94bd',font='verdana 10 bold')

def clear_btn():
    entry_box.delete(0,END)
    entry_box.insert(0,'0')



def delete_btn():
    length=len(entry_box.get())
    entry_box.delete((length-1),'end')
    if length==1:
        entry_box.insert(0,'0')

def enter_operator(x):
    if entry_box.get()!='0':
        length=len(entry_box.get())
        all_text=entry_box.get()
        last_char=all_text[-1:]
        if last_char in ['+','-','/','%'] or all_text[-2:]=='**':
            pass
        else:
            entry_box.insert(length,btn_operation[x]['text'])


def get_time():
    t=time.localtime()
    current_time=time.strftime('%H:%M:%S',t)
    entry_box.delete(0,END)
    entry_box.insert(0,current_time)

status=Label(root,bg='orange',text='History ',anchor=W,font='times 13 ')
status.pack(side=BOTTOM,fill=X)


##--------------Entry box-----------------------##

# all calculation will be here

entry_box=Entry(width=17,font='verdana 20 ',justify=RIGHT,relief=FLAT,bd=0,bg='#5c94bd',fg='white')
entry_box.insert(0,'0')
entry_box.place(x=0,y=1)





###------------------- Button creation using for loop---------------------#

# using for loop we can create all buttons from 0,1,2,3,4,5,6,7,8,9
# and it's operation can solve by anonymous function that is Lambda



btn_number=[] # all buttons are stored in this list

for i in range(10):
    btn_number.append(Button(width=5,bg='#ffffff',font='times 20 ',text=str(i),relief=FLAT,bd=0,command=lambda x=i:enter_number(x)))





##---------------Button position using for loop-----------------##
                ##------after button creation---------##
# we can place all buttons in root window by using
# matrix method row and columns
# we have required 10 buttons from 0-9
# and each row will be contain 3 buttons at a time
# so we have to iterate our loop till 3 times
btn_text=1          #varible
for i in range(3):
    for j in range(3):
        btn_number[btn_text].place(x=j*70,y=40+i*40)
        btn_text+=1


#all operator will be here
# similar to 0-9 numbers we can easily get
# * - + / operator

btn_operation=[]

for i in range(5):
    btn_operation.append(Button(width=5,bg='#ffffff',fg='red',font='times 20 bold ',text=str(i),relief=FLAT,bd=0,command =lambda x=i:enter_operator(x)))

btn_operation[0]['text']='+'
btn_operation[1]['text']='-'
btn_operation[2]['text']='*'
btn_operation[3]['text']='/'
btn_operation[4]['text']='%'

for i in range(5):
    btn_operation[i].place(x=210,y=40+i*40)

zero_btn=Button(width=5,font='times 20  ',text='0',bg='#ffffff',relief=FLAT,bd=0,command=lambda x=0:enter_number(x))
zero_btn.place(x=0,y=160)

equal_btn=Button(width=5,font='times 20 bold ',fg='red',bg='#ffffff',text='=',relief=FLAT,bd=0,command=equal_btn)
equal_btn.place(x=67,y=160)



dot_btn=Button(width=5,font='times 20 bold',fg='red',bg='#ffffff',text='.',relief=FLAT,bd=0,command=lambda x='.':enter_number(x))
dot_btn.place(x=134,y=160)


time_btn=Button(width=5,font='times 20 ',bg='#ffffff',fg='red',text='Time',relief=FLAT,bd=0,command=get_time)
time_btn.place(x=0,y=200)


clear_btn=Button(width=5,font='times 20 ',bg='#ffffff',fg='red',text='C',relief=FLAT,bd=0,command=clear_btn)
clear_btn.place(x=67,y=200)


del_btn=Button(width=5,font='times 20 ',bg='#ffffff',fg='red',text='Del',relief=FLAT,bd=0,command=delete_btn)
del_btn.place(x=134,y=200)






root.mainloop()
