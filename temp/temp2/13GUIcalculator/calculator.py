#%% import libraries
import tkinter as tk
#%% create and start main gui
gui =tk.Tk()
gui.title('My GUI calculator')
#%% define functions
def button_click(number):
    curr_num=entry_box.get()
    entry_box.delete(0,tk.END)
    entry_box.insert(0,str(curr_num)+str(number))

def button_clear():
    entry_box.delete(0,tk.END)

def button_addFn():
    first_num=entry_box.get()
    global g_first_num
    global g_operation
    g_operation='add'
    g_first_num=int(first_num)
    entry_box.delete(0,tk.END)

def button_subtract():
    first_num=entry_box.get()
    global g_first_num
    global g_operation
    g_operation='subtract'
    g_first_num=int(first_num)
    entry_box.delete(0,tk.END)

def button_multiply():
    first_num=entry_box.get()
    global g_first_num
    global g_operation
    g_operation='multiply'
    g_first_num=int(first_num)
    entry_box.delete(0,tk.END)

def button_divide():
    first_num=entry_box.get()
    global g_first_num
    global g_operation
    g_operation='divide'
    g_first_num=int(first_num)
    entry_box.delete(0,tk.END)

def button_equal():
    second_num=entry_box.get()
    entry_box.delete(0,tk.END)
    if g_operation=='add':
        result = g_first_num + int(second_num)
        entry_box.insert(0,result)
    elif g_operation=='subtract':
        result = g_first_num - int(second_num)
        entry_box.insert(0,result)
    elif g_operation=='multiply':
        result = g_first_num * int(second_num)
        entry_box.insert(0,result)
    elif g_operation=='divide':
        result = g_first_num / int(second_num)
        entry_box.insert(0,result)


#%% create entry box
entry_box=tk.Entry(gui,width=30,borderwidth=5)
entry_box.grid(row=0,column=0,columnspan=4,padx=30,pady=1)


#%% create buttons
button_1 = tk.Button(gui,text='1',padx=25,pady=15,command=lambda :button_click(1))
button_2 = tk.Button(gui,text='2',padx=25,pady=15,command=lambda :button_click(2))
button_3 = tk.Button(gui,text='3',padx=25,pady=15,command=lambda :button_click(3))
button_4 = tk.Button(gui,text='4',padx=25,pady=15,command=lambda :button_click(4))
button_5 = tk.Button(gui,text='5',padx=25,pady=15,command=lambda :button_click(5))
button_6 = tk.Button(gui,text='6',padx=25,pady=15,command=lambda :button_click(6))
button_7 = tk.Button(gui,text='7',padx=25,pady=15,command=lambda :button_click(7))
button_8 = tk.Button(gui,text='8',padx=25,pady=15,command=lambda :button_click(8))
button_9 = tk.Button(gui,text='9',padx=25,pady=15,command=lambda :button_click(9))
button_0 = tk.Button(gui,text='0',padx=25,pady=15,command=lambda :button_click(0))

button_add = tk.Button(gui,text='+',padx=25,pady=15,command=button_addFn)
button_sub = tk.Button(gui,text='-',padx=25,pady=15,command=button_subtract)
button_mul = tk.Button(gui,text='*',padx=25,pady=15,command=button_multiply)
button_div = tk.Button(gui,text='/',padx=25,pady=15,command=button_divide)

button_Clear = tk.Button(gui,text='C',padx=25,pady=15,command=button_clear)
button_Equal = tk.Button(gui,text='=',padx=25,pady=15,command=button_equal)

#place buttons in gui
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_mul.grid(row=2,column=3)

button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)
button_sub.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_Clear.grid(row=4,column=1)
button_Equal.grid(row=4,column=2)
button_add.grid(row=4,column=3)

#%% run main gui
gui.mainloop()


#%% 터미널창에서 하면 실행파일 만들수있다
#   pip list 로 라이브러리가 있는지 찾아보고
# pyinstaller --onefile calculator.py