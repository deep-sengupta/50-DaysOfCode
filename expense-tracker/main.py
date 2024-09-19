import platform
from tkinter import *
from tkinter import ttk
import datetime as dt
from database import *
from tkinter import messagebox

data = Database(db='results.db')

selected_rowid = 0

def saveRecord():
    if not item_name.get() or not item_amt.get() or not transaction_date.get():
        messagebox.showwarning('Input Error', 'Please fill all fields before saving.')
        return
    try:
        float(item_amt.get())
    except ValueError:
        messagebox.showwarning('Input Error', 'Item Price must be a number.')
        return
    data.insertRecord(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=transaction_date.get())
    refreshData()
    clearEntries()

def setDate():
    date = dt.datetime.now()
    dopvar.set(f'{date:%d %B %Y}')

def clearEntries():
    item_name.delete(0, 'end')
    item_amt.delete(0, 'end')
    transaction_date.delete(0, 'end')

def fetch_records():
    f = data.fetchRecord('select rowid, * from expense_record')
    for rec in f:
        tv.insert(parent='', index='0', iid=rec[0], values=(rec[0], rec[1], rec[2], rec[3]))

def select_record(event):
    global selected_rowid
    selected = tv.focus()
    values = tv.item(selected, 'values')
    if values:
        selected_rowid = values[0]
        namevar.set(values[1])
        amtvar.set(values[2])
        dopvar.set(values[3])

def update_record():
    global selected_rowid
    if not selected_rowid:
        messagebox.showwarning('Selection Error', 'Please select a record to update.')
        return
    if not namevar.get() or not amtvar.get() or not dopvar.get():
        messagebox.showwarning('Input Error', 'Please fill all fields before updating.')
        return
    try:
        float(amtvar.get())
    except ValueError:
        messagebox.showwarning('Input Error', 'Item Price must be a number.')
        return
    data.updateRecord(namevar.get(), amtvar.get(), dopvar.get(), selected_rowid)
    refreshData()
    clearEntries()

def totalBalance():
    f = data.fetchRecord(query="Select sum(item_price) from expense_record")
    for i in f:
        for j in i:
            messagebox.showinfo('Current Balance: ', f"Total Expense: {j}\nBalance Remaining: {5000 - j}")

def refreshData():
    for item in tv.get_children():
        tv.delete(item)
    fetch_records()

def deleteRow():
    global selected_rowid
    if selected_rowid:
        data.removeRecord(selected_rowid)
        refreshData()
        selected_rowid = 0
    else:
        messagebox.showwarning('Delete Error', 'Please select a record to delete.')

ws = Tk()
ws.title('Expense Tracker')

ws.geometry('860x460')
ws.resizable(False, False)

bg_color = '#333333'
btn_color = '#D9B036'
entry_color = '#222222'
text_color = 'white'

ws.configure(bg=bg_color)

f1 = Frame(ws, bg=bg_color)
f1.pack(padx=20, pady=20)

f2 = Frame(ws, bg=bg_color)
f2.pack(padx=20, pady=20)

namevar = StringVar()
amtvar = StringVar()
dopvar = StringVar()

Label(f1, text="Item Name", bg=bg_color, fg=text_color).grid(row=0, column=0, padx=10, pady=10, sticky=W)
Label(f1, text="Item Price", bg=bg_color, fg=text_color).grid(row=1, column=0, padx=10, pady=10, sticky=W)
Label(f1, text="Purchase Date", bg=bg_color, fg=text_color).grid(row=2, column=0, padx=10, pady=10, sticky=W)

item_name = Entry(f1, width=35, textvariable=namevar, bg=entry_color, fg=text_color)
item_amt = Entry(f1, width=35, textvariable=amtvar, bg=entry_color, fg=text_color)
transaction_date = Entry(f1, width=35, textvariable=dopvar, bg=entry_color, fg=text_color)

item_name.grid(row=0, column=1, padx=10, pady=10, sticky=W)
item_amt.grid(row=1, column=1, padx=10, pady=10, sticky=W)
transaction_date.grid(row=2, column=1, padx=10, pady=10, sticky=W)

cur_date = Button(f1, text='Set Current Date', command=setDate, bg=btn_color, width=20)
submit_btn = Button(f1, text='Save Record', command=saveRecord, bg='#26B72B', width=15)
clr_btn = Button(f1, text='Clear Entry', command=clearEntries, bg=btn_color, width=15)
quit_btn = Button(f1, text='Exit', command=lambda: ws.destroy(), bg='#D33532', width=15)
total_bal = Button(f1, text='Total Balance', command=totalBalance, bg='#486966', width=15)
update_btn = Button(f1, text='Update', command=update_record, bg='#C2BB00', width=15)
del_btn = Button(f1, text='Delete', command=deleteRow, bg='#BD2A2E', width=15)

cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))

tv = ttk.Treeview(f2, columns=(1, 2, 3, 4), show='headings', height=10)
tv.pack(side="left")

tv.column(1, anchor=CENTER, stretch=NO, width=100)
tv.column(2, anchor=CENTER, stretch=YES, width=300)
tv.column(3, anchor=CENTER, stretch=YES, width=150)
tv.column(4, anchor=CENTER, stretch=YES, width=250)
tv.heading(1, text="Serial no")
tv.heading(2, text="Item Name")
tv.heading(3, text="Item Price")
tv.heading(4, text="Purchase Date")

tv.bind("<ButtonRelease-1>", select_record)

scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill="y")
tv.config(yscrollcommand=scrollbar.set)

fetch_records()

ws.mainloop()