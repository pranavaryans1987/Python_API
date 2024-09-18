import requests
from customtkinter import *
from CTkMessagebox import CTkMessagebox
root = CTk()
root.geometry("300x300")
url = "https://pranavtrivedi.in/apidiva.php"

def search():
    id = txtid.get()
    if len(id) > 0:  
        data = {"id":id,"action":"Search"}
        res = requests.post(url,data)
        ary = res.json()
        if ary['data'] != '0':
            for x,y in zip(ary['data'],ary['data1']):
                txtnm.insert(0,x)
                txtres.insert(0,y)
        else:
            CTkMessagebox(root,title="CRUD",message="No Records Found!")
            clear()
    else:
        CTkMessagebox(root,title="CRUD",message="Please Enter ID!")
        clear()

def insert():
    name = txtnm.get()
    result = txtres.get()
    if len(name) >0 or len(result) >0:
        data = {"name":name,"result":result,"action":"Insert"}
        res = requests.post(url,data)
        ary = res.json()
        if ary['data'] == '1':
            CTkMessagebox(root,title="CRUD",message="Record Inserted!")
            clear()
        else:
            CTkMessagebox(root,title="CRUD",message="There was some error!")
            clear()
    else:
        CTkMessagebox(root,title="CRUD",message="Please Enter Record!")

def update():
    id = txtid.get()
    name = txtnm.get()
    result = txtres.get()
    data = {"id":id,"name":name,"result":result,"action":"Update"}
    res = requests.post(url,data)
    ary = res.json()
    if ary['data'] == '1':
        CTkMessagebox(root,title="CRUD",message="Record Updated!")
        clear()
    else:
        CTkMessagebox(root,title="CRUD",message="Record Not Updated!")
        clear()

def delete():
    id = txtid.get()
    data = {"id":id,"action":"Delete"}
    res = requests.post(url,data)
    ary = res.json()
    if ary['data'] == '1':
        CTkMessagebox(root,title="CRUD",message="Record Deleted!")
        clear()
    else:
        CTkMessagebox(root,title="CRUD",message="Record Not Deleted!")
        clear()

def clear():
    txtid.delete(0,END)
    txtnm.delete(0,END)
    txtres.delete(0,END)

txtid = CTkEntry(root,placeholder_text="Enter ID To Search")
txtid.pack(padx="2",pady="2",fill="x")
CTkButton(root,text="Search",command=search).pack(padx="2",pady="2",fill="x")
txtnm = CTkEntry(root,placeholder_text="Enter Name")
txtnm.pack(padx="2",pady="2",fill="x")
txtres = CTkEntry(root,placeholder_text="Enter Result")
txtres.pack(padx="2",pady="2",fill="x")
CTkButton(root,text="Insert",command=insert).pack(padx="2",pady="2",fill="x")
CTkButton(root,text="Update",command=update).pack(padx="2",pady="2",fill="x")
CTkButton(root,text="Delete",command=delete).pack(padx="2",pady="2",fill="x")
root.mainloop()