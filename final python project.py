from tkinter import*
from tkinter import font as tkFont 
from tkinter import messagebox

orders_list = []
order_id = 1


def ordernow():
    global order_id
    mylist= [name.get(), address.get(), small.get(), medium.get(),
    large.get(), mobile.get(), email.get(), order_id]
    name.delete(0, END)
    address.delete(0, END)
    small.delete(0, END)
    medium.delete (0, END)
    large.delete(0, END)
    mobile.delete (0, END)
    email.delete (0, END)

    orders_list.append(mylist)
    messagebox.showinfo(title="Successfull",
    message='Pizza ordered successfully, Order Id : '+ str(order_id))
    order_id += 1
    print(orders_list)
def track_pizza():
    track_window = Toplevel()
    myframe =Frame(track_window)
    myframe.pack()
    for i in orders_list:
        label = Label (myframe,
        text=i[0]+" ordered a pizza" +", order id: " + str(i[7]), font=("Arial", 18)).pack()

def delete_order():
    to_del =int(id.get())
    id.delete(0, END)
    for i in  range(0,len(orders_list)):
        if orders_list[i][7]==to_del:
            orders_list.pop(i)
            break
    messagebox.showinfo(title="Deleted", message='Pizza order deleted successfully')

def cancel_order():
    cancel_window = Toplevel()
    myframe = Frame (cancel_window)
    Label (myframe, text="Enter Order Id to Delete", font=28).pack()
    global id
    id = Entry(myframe, width=20)
    id.pack()
    btn = Button(myframe, text="Delete", font=18,command=delete_order).pack()
    myframe.pack()

def order_pizza():
    new_window= Toplevel ()
    orderframe = Frame (new_window)
    orderframe.pack()
    Label (orderframe, text='Name', font=50, pady=10).grid(row =0, column =0)
    global name
    name=Entry(orderframe, width=20)
    name.grid(row=0, column=1)

    Label(orderframe, text="Address", font=50, pady=10).grid(row=1, column=0)
    global address
    address=Entry(orderframe, width=20)
    address.grid(row=1, column=1)
    Label(orderframe, text='Pizza Type', font = 50 ,pady = 10).grid (row = 2 , column = 0)
    Label(orderframe, text='Small (95 Rs)', font = 50, pady = 10).grid (row = 2 ,column = 1)
    
    global small
    small=Entry (orderframe, width=5)
    small.grid(row=2,column=2)
    Label(orderframe,text='Medium(195 Rs)',font=50,pady=10).grid(row=2,column=3)

    global medium
    medium =Entry(orderframe,width=5)
    medium.grid(row=2,column=4)
    Label(orderframe,text='Large(295 Rs)',font=50,pady=10).grid(row=2,column=5)

    global large
    large=Entry(orderframe,width=5)
    large.grid(row=2,column=6)
    Label(orderframe,text="Email Id",font=50,pady=10).grid(row=3,column=0)

    global mobile
    mobile =Entry(orderframe, width=20)
    mobile.grid(row=3, column=1)
    Label(orderframe, text='Email Id', font=50, pady = 10 ) .grid(row=4, column=0)

    global email
    email =Entry (orderframe, width = 20)
    email.grid(row=4, column=1)
    order_now_button= Button (orderframe, text="Order Now", font = 30,
    command=ordernow).grid(row=5, column=4)



window= Tk()
window.geometry ("800x400")
window.title("Pizza Tracking Project")
frame= Frame(window)
frame.pack()

button_font=tkFont.Font(family='Helvetica',size=20,weight=tkFont.BOLD)
order_pizza_button=Button(frame,text='Order Pizza',width=10, pady=8, font=button_font, 
command=order_pizza).grid(row=0, column=0)
cancel_order_button=Button(frame,text='Cancel order',width=10,pady=8,font=button_font,
command='cancal_order').grid(row=0,column=1)
track_pizza_button=Button(frame,text='Vendor Track Order',width=16,pady=8,font=button_font,command=track_pizza).grid(row=0,column=2)
window.mainloop()



