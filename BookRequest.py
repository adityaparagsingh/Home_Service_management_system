from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class BookRequestWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Aditya's Home Service Provider:)")
        self.root.geometry("1134x564+306+258")

        #-------------------------Variables----------------------------
        self.variable_referenceID=StringVar()
        x=random.randint(10000,99999)
        self.variable_referenceID.set(str(x))
        self.variable_name=StringVar()
        self.variable_age=StringVar()
        self.variable_gender=StringVar()
        self.variable_phone=StringVar()
        self.variable_email=StringVar()
        self.variable_state=StringVar()
        self.variable_city=StringVar()
        self.variable_area=StringVar()
        self.variable_pincode=StringVar()
        self.variable_service=StringVar()
        self.variable_tradesman=StringVar()


        #----------------------------TITLE-----------------------------
        lbl_title=Label(self.root,text="Aditya's Home Services",font=("times new roman",35,"bold"),bg="black",fg="gold",bd=4,relief=RAISED,cursor="circle")
        lbl_title.place(x=0,y=0,width=1134,height=50)

        lbl_title2=Label(self.root,text="Book A New Request",font=("times new roman",30,),bg="black",fg="gold",bd=4,relief=RAISED,cursor="circle")
        lbl_title2.place(x=0,y=50,width=1134,height=50)


         #-----------------------------LOGO----------------------------
        img2=Image.open("/Users/pankajsingh/Desktop/HomeService/2.jpeg")
        img2=img2.resize((370,140),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE,cursor="circle")
        lblimg.place(x=0,y=0,width=175,height=100)

        #-----------------------Label Frame Left----------------------
        labelframe1=LabelFrame(self.root,bd=2,relief=RIDGE,text="Book A New Request Below👇🏻",font=("Comic Sans MS",15,"bold","underline"),padx=3,cursor="circle")
        labelframe1.place(x=5,y=100,width=460,height=460)


        #-----------------------Label And Entries----------------------
        #Reference ID
        lbl_refID=Label(labelframe1,text="Reference ID👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_refID.grid(row=0,column=0,sticky=W)

        entry_refID=ttk.Entry(labelframe1,textvariable=self.variable_referenceID,width=30,font=("times new roman",15,"bold"),cursor="dot",state="readonly")
        entry_refID.grid(row=0,column=1)

        #Name
        lbl_name=Label(labelframe1,text="Enter Name👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(labelframe1,textvariable=self.variable_name,width=30,font=("times new roman",15,"bold"),cursor="dot")
        entry_name.grid(row=1,column=1)

        #Age
        lbl_age=Label(labelframe1,text="Age👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_age.grid(row=2,column=0,sticky=W)

        combo_age=ttk.Combobox(labelframe1,textvariable=self.variable_age,font=("times new roman",15,"bold"),width=27,cursor="dot",state="readonly")
        combo_age["value"]=tuple(range(1,100))
        combo_age.grid(row=2,column=1)
        #Gender
        lbl_gender=Label(labelframe1,text="Gender👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframe1,textvariable=self.variable_gender,font=("times new roman",15,"bold"),width=27,cursor="dot",state="readonly")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.grid(row=3,column=1)


        #Mobile No
        lbl_mobile=Label(labelframe1,text="Phone Number👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_mobile.grid(row=4,column=0,sticky=W)

        entry_mobile=ttk.Entry(labelframe1,textvariable=self.variable_phone,width=30,font=("times new roman",15,"bold"),cursor="dot")
        entry_mobile.grid(row=4,column=1)


        #Email
        lbl_email=Label(labelframe1,text="Email ID👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_email.grid(row=5,column=0,sticky=W)

        entry_email=ttk.Entry(labelframe1,textvariable=self.variable_email,width=30,font=("times new roman",15,"bold"),cursor="dot")
        entry_email.grid(row=5,column=1)

        
        #State
        lbl_state=Label(labelframe1,text="State👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_state.grid(row=6,column=0,sticky=W)

        combo_state=ttk.Combobox(labelframe1,textvariable=self.variable_state,font=("times new roman",15,"bold"),width=27,state="readonly",cursor="dot")
        combo_state["value"]=("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")
        combo_state.grid(row=6,column=1)
        
        #City
        lbl_city=Label(labelframe1,text="City👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_city.grid(row=7,column=0,sticky=W)

        entry_city=ttk.Entry(labelframe1,textvariable=self.variable_city,width=30,font=("times new roman",15,"bold"),cursor="dot")
        entry_city.grid(row=7,column=1)

        #Location
        lbl_location=Label(labelframe1,text="Area (Location)👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_location.grid(row=8,column=0,sticky=W)

        entry_location=ttk.Entry(labelframe1,textvariable=self.variable_area,width=30,font=("times new roman",15,"bold"),cursor="dot")
        entry_location.grid(row=8,column=1)

        #Pin Code
        lbl_pincode=Label(labelframe1,text="Area Pin Code👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_pincode.grid(row=9,column=0,sticky=W)

        entry_pincode=ttk.Entry(labelframe1,textvariable=self.variable_pincode,width=30,font=("times new roman",15,"bold"),cursor="dot")
        entry_pincode.grid(row=9,column=1)

        #Request Type
        lbl_request=Label(labelframe1,text="Service Required👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_request.grid(row=10,column=0,sticky=W)

        combo_request=ttk.Combobox(labelframe1,textvariable=self.variable_service,font=("times new roman",15,"bold"),width=27,cursor="dot")
        combo_request["value"]=("Deep house cleaning","Garden services","Pest control","Babysitting","Painting","Cementing","Bathroom cleaning","Chimney Repair","Washing Machine Repair","Geyser Repair","AC Repair","Seepage Repair","Drain Blockage","Sink Repair","Window and Doors Repair","LED Replacement","Tubelight Replacement","Ceiling Fan Repair","Exhaust Fan Repair","Socket Repair","Overhead Tank Cleaning","Saloon for Women","Saloon for Men","Hair,Skin,Nails Care","Pest Control","Sofa Cleaning","Disinfection Services","Carpet,Mat,Rug Cleaning","Furniture Repair","Bathroom Fitting","Wiring Work","Water Purifier Repair","Car Cleaning","Other(Type)")
        combo_request.grid(row=10,column=1)

        #Tradesman Required
        lbl_tradesman=Label(labelframe1,text="Tradesman Required👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_tradesman.grid(row=11,column=0,sticky=W)

        combo_tradesman=ttk.Combobox(labelframe1,textvariable=self.variable_tradesman,font=("times new roman",15,"bold"),width=27,cursor="dot")
        combo_tradesman["value"]=("Carpenter","Plumber","Painter","Mason","Electrician","Sweeper","Repair Mechanics","Cleaning Agents","Furniture Polisher","Barber","Massage Therapist","Makeover Artist","BabySitters","Homelook","Home Caretaker","Other(Type)")
        combo_tradesman.grid(row=11,column=1)


        #---------------------------Buttons----------------------------
        btn_frame=Frame(labelframe1,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=393,width=440,height=40)      

        btn_add=Button(btn_frame,text="Add Request",command=self.add_data,font=("times new roman",18,"bold"),bg="white",fg="#0000FF",cursor="dot")
        btn_add.grid(row=0,column=0,padx=5,pady=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("times new roman",18,"bold"),bg="white",fg="#0000FF",cursor="dot")
        btn_update.grid(row=0,column=1,padx=5,pady=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.booking_delete,font=("times new roman",18,"bold"),bg="white",fg="#FF0000",cursor="dot")
        btn_delete.grid(row=0,column=2,padx=5,pady=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",18,"bold"),bg="white",fg="#FF0000",cursor="dot")
        btn_reset.grid(row=0,column=3,padx=5,pady=1)


        #-------------------------Table frame--------------------------
        labelframe2=LabelFrame(self.root,bd=2,relief=RIDGE,text="All requests and Details",font=("Comic Sans MS",15,"bold","underline"),padx=3,cursor="circle")
        labelframe2.place(x=465,y=100,width=660,height=460)


        lbl_searchby=Label(labelframe2,text="Search By :-",font=("times new roman",15,"bold"),cursor="dot",bg="#F3E3C3",fg="#4B0082")
        lbl_searchby.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(labelframe2,textvariable=self.search_var,font=("times new roman",15,"bold"),width=15,cursor="dot",state="readonly")
        combo_searchby["value"]=("ReferenceID","PhoneNumber","Name","Email","Age","Gender","State","City","ServiceRequired","Tradesman")
        combo_searchby.grid(row=0,column=1,padx=5)

        self.text_search=StringVar()
        entry_searchby=ttk.Entry(labelframe2,textvariable=self.text_search,width=25,font=("times new roman",15,"bold"),cursor="dot")
        entry_searchby.grid(row=0,column=2)

        btn_search=Button(labelframe2,text="Search",command=self.search,font=("times new roman",18,"bold"),bg="white",fg="#008000",cursor="dot")
        btn_search.grid(row=0,column=3)

        btn_showall=Button(labelframe2,text="Show All",command=self.fetch_data,font=("times new roman",18,"bold"),bg="white",fg="#810541",cursor="dot")
        btn_showall.grid(row=0,column=4)

        #------------------------Show Data Table-----------------------
        table_frame=Frame(labelframe2,bd=2,relief=RIDGE,cursor="dot")
        table_frame.place(x=0,y=35,width=650,height=395)

        Xscorll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Yscorll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.details_table=ttk.Treeview(table_frame,columns=("ReferenceID","Name","Age","Gender","PhoneNumber","Email","State","City","Area","PinCode","ServiceRequired","Tradesman"),xscrollcommand=Xscorll.set,yscrollcommand=Yscorll.set)

        Xscorll.pack(side=BOTTOM,fill=X)
        Yscorll.pack(side=RIGHT,fill=Y)

        Xscorll.config(command=self.details_table.xview)
        Yscorll.config(command=self.details_table.yview)

        self.details_table.heading("ReferenceID",text="ReferenceID")
        self.details_table.heading("Name",text="Name")
        self.details_table.heading("Age",text="Age")
        self.details_table.heading("Gender",text="Gender")
        self.details_table.heading("PhoneNumber",text="PhoneNumber")
        self.details_table.heading("Email",text="Email")
        self.details_table.heading("State",text="State")
        self.details_table.heading("City",text="City")
        self.details_table.heading("Area",text="Area")
        self.details_table.heading("PinCode",text="PinCode")
        self.details_table.heading("ServiceRequired",text="ServiceRequired")
        self.details_table.heading("Tradesman",text="Tradesman")

        self.details_table["show"]="headings"
        self.details_table.column("ReferenceID",width=100)
        self.details_table.column("Name",width=100)
        self.details_table.column("Age",width=100)
        self.details_table.column("Gender",width=100)
        self.details_table.column("PhoneNumber",width=100)
        self.details_table.column("Email",width=100)
        self.details_table.column("State",width=100)
        self.details_table.column("City",width=100)
        self.details_table.column("Area",width=100)
        self.details_table.column("PinCode",width=100)
        self.details_table.column("ServiceRequired",width=100)
        self.details_table.column("Tradesman",width=100)

        self.details_table.pack(fill=BOTH,expand=1)
        self.details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    def add_data(self):
        if self.variable_age.get()=="" or self.variable_name.get()=="" or self.variable_gender.get()=="" or self.variable_area.get()=="" or self.variable_state.get()=="" or self.variable_city.get()=="" or self.variable_phone.get()=="" or self.variable_pincode.get()=="" or self.variable_email.get()=="" or self.variable_service.get()=="" or self.variable_tradesman.get()=="":
            messagebox.showerror("❌Error❌","❌Please Enter All The Fields❌",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host="localhost",username="root",password="helloworld",database="home_services")
                cursor1=connection.cursor()
                cursor1.execute("insert into bookings values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.variable_referenceID.get(),
                                                                        self.variable_name.get(),
                                                                        self.variable_age.get(),
                                                                        self.variable_gender.get(),
                                                                        self.variable_phone.get(),
                                                                        self.variable_email.get(),
                                                                        self.variable_state.get(),
                                                                        self.variable_city.get(),
                                                                        self.variable_area.get(),
                                                                        self.variable_pincode.get(),
                                                                        self.variable_service.get(),
                                                                        self.variable_tradesman.get()
                                                                        ))
                                                                                                    
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Done","✅Booking Has Been Done✅",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"!Something Went Wrong!:{str(es)}",parent=self.root)

    def fetch_data(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="helloworld",database="home_services")
        cursor1=connection.cursor()
        cursor1.execute("Select * from bookings")
        table=cursor1.fetchall()
        if len(table)!=0:
            self.details_table.delete(*self.details_table.get_children())
            for i in table:
                self.details_table.insert("",END,values=i)
            connection.commit()
        connection.close()


    def get_cursor(self,event=""):
        cursor_table=self.details_table.focus()
        bookings=self.details_table.item(cursor_table)
        row=bookings["values"]

        self.variable_referenceID.set(row[0]),
        self.variable_name.set(row[1]),
        self.variable_age.set(row[2]),
        self.variable_gender.set(row[3]),
        self.variable_phone.set(row[4]),
        self.variable_email.set(row[5]),
        self.variable_state.set(row[6]),
        self.variable_city.set(row[7]),
        self.variable_area.set(row[8]),
        self.variable_pincode.set(row[9]),
        self.variable_service.set(row[10]),
        self.variable_tradesman.set(row[11])

    
    def update(self):
        if self.variable_age.get()=="" or self.variable_name.get()=="" or self.variable_gender.get()=="" or self.variable_area.get()=="" or self.variable_state.get()=="" or self.variable_city.get()=="" or self.variable_phone.get()=="" or self.variable_pincode.get()=="" or self.variable_email.get()=="" or self.variable_service.get()=="" or self.variable_tradesman.get()=="":
            messagebox.showerror("❌Error❌","❌Please Enter All The Fields❌",parent=self.root)
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="helloworld",database="home_services")
            cursor1=connection.cursor()
            cursor1.execute("UPDATE bookings SET Name=%s,Age=%s,Gender=%s,PhoneNumber=%s,Email=%s,State=%s,City=%s,Area=%s,PinCode=%s,ServiceRequired=%s,Tradesman=%s where ReferenceID=%s",(
                                                                                                                                                                    self.variable_name.get(),
                                                                                                                                                                    self.variable_age.get(),
                                                                                                                                                                    self.variable_gender.get(),
                                                                                                                                                                    self.variable_phone.get(),
                                                                                                                                                                    self.variable_email.get(),
                                                                                                                                                                    self.variable_state.get(),
                                                                                                                                                                    self.variable_city.get(),
                                                                                                                                                                    self.variable_area.get(),
                                                                                                                                                                    self.variable_pincode.get(),
                                                                                                                                                                    self.variable_service.get(),
                                                                                                                                                                    self.variable_tradesman.get(),
                                                                                                                                                                    self.variable_referenceID.get()
                                                                                                                                                                                                ))
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Update Done","✅Update is Done✅",parent=self.root)
        
    
    def booking_delete(self):
        booking_delete=messagebox.askyesno("Aditya's Home Services","Do you want to delete this Booking???(This action cannot be undo!!!)",parent=self.root)
        if booking_delete>0:
            connection=mysql.connector.connect(host="localhost",username="root",password="helloworld",database="home_services")
            cursor1=connection.cursor()
            query="DELETE from bookings where ReferenceID=%s"
            value=(self.variable_referenceID.get(),)
            cursor1.execute(query,value)
        else:
            if not booking_delete:
                return


        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Deleted","✅Booking is Deleted✅",parent=self.root)


    def reset(self):
        #self.variable_referenceID.set(""),
        self.variable_name.set(""),
        self.variable_age.set(""),
        self.variable_gender.set(""),
        self.variable_phone.set(""),
        self.variable_email.set(""),
        self.variable_state.set(""),
        self.variable_city.set(""),
        self.variable_area.set(""),
        self.variable_pincode.set(""),
        self.variable_service.set(""),
        self.variable_tradesman.set("")

        x=random.randint(10000,99999)
        self.variable_referenceID.set(str(x))


    def search(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="helloworld",database="home_services")
        cursor1=connection.cursor()
        cursor1.execute("SELECT * FROM bookings WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.text_search.get()) + "%'")

        rows=cursor1.fetchall()
        if len (rows)!=0:
            self.details_table.delete(*self.details_table.get_children())
            for i in rows:
                self.details_table.insert("",END,values=i)
            connection.commit()
        connection.close()
            

if __name__ == "__main__":
    root = Tk()
    obj=BookRequestWindow(root)
    root.mainloop()
