from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class FeedbackWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Aditya's Home Service Provider:)")
        self.root.geometry("1134x564+306+258")

        #---------------------------Variables Names--------------------
        self.variable_name=StringVar()
        self.variable_feedback=StringVar()


        #----------------------------TITLE-----------------------------
        lbl_title=Label(self.root,text="Aditya's Home Services",font=("times new roman",35,"bold"),bg="black",fg="gold",bd=4,relief=RAISED,cursor="circle")
        lbl_title.place(x=0,y=0,width=1134,height=50)

        lbl_title2=Label(self.root,text="Feedbacks",font=("times new roman",30,),bg="black",fg="gold",bd=4,relief=RAISED,cursor="circle")
        lbl_title2.place(x=0,y=50,width=1134,height=50)


         #-----------------------------LOGO-----------------------------
        img2=Image.open("/Users/pankajsingh/Desktop/HomeService/2.jpeg")
        img2=img2.resize((370,140),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE,cursor="circle")
        lblimg.place(x=0,y=0,width=175,height=100)


        #------------------------Wtitten Part--------------------------
        lbl_title2=Label(self.root,text="Aditya ~ Great and easy Interface to get your issue solved in mins \n Mahee ~ Its a great think that we can list our complaints in ample of time very quickly \n Akshat ~ Nice :) \n Anushka ~ 5 stars no doubt great interface also",font=("times new roman",30,),bg="black",fg="gold",bd=4,relief=RAISED,cursor="circle")
        lbl_title2.place(x=0,y=100,width=1134,height=465)
        
        
        #-----------------------feedback data Frame---------------------------
        labelframe1=LabelFrame(self.root,bd=2,relief=RIDGE,text="We Would Love to have your feedbacks HERE!!!",font=("Comic Sans MS",15,"bold","underline"),padx=3,cursor="circle")
        labelframe1.place(x=5,y=100,width=1120,height=120)

        #Name
        lbl_name=Label(labelframe1,text="Enter Name👉🏻",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_name.grid(row=1,column=0,sticky=W)     

        entry_name=ttk.Entry(labelframe1,textvariable=self.variable_name,width=100,font=("times new roman",15,"bold"),cursor="dot")
        entry_name.grid(row=1,column=1)

        #Feedback
        lbl_feedback=Label(labelframe1,text="Feedback/Comment:)",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_feedback.grid(row=2,column=0,sticky=W)  

        entry_feedback=ttk.Entry(labelframe1,textvariable=self.variable_feedback,width=100,font=("times new roman",15,"bold"),cursor="dot")
        entry_feedback.grid(row=2,column=1)

        #Stars(rating)
        lbl_feedback=Label(labelframe1,text="Rating",font=("times new roman",15,"bold"),padx=5,pady=6,cursor="dot")
        lbl_feedback.grid(row=3,column=0,sticky=W)  

        combo_gender=ttk.Combobox(labelframe1,textvariable=self.variable_gender,font=("times new roman",15,"bold"),width=27,cursor="dot",state="readonly")
        combo_gender["value"]=("⭐️","⭐️⭐️","O⭐️⭐️⭐️","⭐️⭐️⭐️⭐️","⭐️⭐️⭐️⭐️⭐️")
        combo_gender.grid(row=3,column=1)

       #---------------------------Buttons----------------------------
        btn_frame=Frame(labelframe1,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=393,width=440,height=40)      

        btn_add=Button(btn_frame,text="Add Comment",command=self.add_data,font=("times new roman",18,"bold"),bg="white",fg="#0000FF",cursor="dot")
        btn_add.grid(row=0,column=0,padx=5,pady=1)
                     


    def add_data(self):
        if self.variable_age.get()=="" or self.variable_name.get()=="" or self.variable_gender.get()=="" or self.variable_area.get()=="" or self.variable_state.get()=="" or self.variable_city.get()=="" or self.variable_phone.get()=="" or self.variable_pincode.get()=="" or self.variable_email.get()=="" or self.variable_service.get()=="" or self.variable_tradesman.get()=="":
            messagebox.showerror("❌Error❌","❌Please Enter All The Fields❌",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host="localhost",username="root",password="helloworld",database="home_services")
                cursor1=connection.cursor()
                cursor1.execute("insert into bookings values(%s)",(self.variable_name.get()))
                                                                                                    
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Done","✅Booking Has Been Done✅",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"!Something Went Wrong!:{str(es)}",parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj=FeedbackWindow(root)
    root.mainloop()
