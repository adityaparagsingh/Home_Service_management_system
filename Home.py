from tkinter import *                                                                              #using tkinter GUI
from PIL import Image, ImageTk
from BookRequest import BookRequestWindow
from Dashboard import DashboardWindow
from Profile import ProfileWindow
from Feedback import FeedbackWindow
from AboutOurCompany import AboutOurCompanyWindow
from ContactUS import ContactUsWindow

class HomeService:
    def __init__(self,root):
        self.root=root
        self.root.title("Aditya's Home Service Provider :)")
        self.root.geometry("1437x800+1+1")


        #--------------1st Image (Banner ~ Home service)---------------
        img1=Image.open("/Users/pankajsingh/Desktop/HomeService/1.png")
        img1=img1.resize((1500,140),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=5,relief=SUNKEN,cursor="circle")            #setting border and image
        lblimg.place(x=0,y=0,width=1500,height=150)                                                #placing image anywhere on screen


        #-----------------------------LOGO-----------------------------
        img2=Image.open("/Users/pankajsingh/Desktop/HomeService/2.jpeg")
        img2=img2.resize((370,140),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE,cursor="circle")
        lblimg.place(x=0,y=0,width=350,height=140)                     


        #----------------------------TITLE-----------------------------
        lbl_title=Label(self.root,text="Welcome To Aditya's Home Services :)",cursor="circle",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RAISED)
        lbl_title.place(x=0,y=140,width=1500,height=60)


        #--------------------------Main Frame--------------------------
        main_frame=Frame(self.root,bd=4,relief=RIDGE,cursor="circle")
        main_frame.place(x=0,y=200,width=1500,height=695)


        #--------------------------Main Menu---------------------------
        lbl_menu=Label(main_frame,text="MAIN MENU",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=300)


        #------------------------Frame(Buttons)------------------------
        button_frame=Frame(main_frame,bg="black",bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=300,height=235)

        Book_button=Button(button_frame,text="Book Request",command=self.book_window,width=20,font=("Comic Sans MS",20,"bold"),bg="black",fg="gold",bd=1,relief=RAISED,cursor="dot")
        Book_button.grid(row=0,column=0)

        Dashboard_button=Button(button_frame,text="Dashboard",command=self.dashboard_window,width=20,font=("Comic Sans MS",20,"bold"),bg="grey",fg="gold",bd=1,relief=RAISED,cursor="dot")
        Dashboard_button.grid(row=1,column=0)

        Profile_button=Button(button_frame,text="Profile",command=self.profile_window,width=20,font=("Comic Sans MS",20,"bold"),bg="grey",fg="gold",bd=1,relief=RAISED,cursor="dot")
        Profile_button.grid(row=2,column=0)

        Feedback_button=Button(button_frame,text="Feedback:)",command=self.feedback_window,width=20,font=("Comic Sans MS",20,"bold"),bg="grey",fg="gold",bd=1,relief=RAISED,cursor="dot")
        Feedback_button.grid(row=3,column=0)

        AboutUS_button=Button(button_frame,text="About Our Company",command=self.aboutus_window,width=20,font=("Comic Sans MS",20,"bold"),bg="grey",fg="gold",bd=1,relief=RAISED,cursor="dot")
        AboutUS_button.grid(row=4,column=0)
        
        Contact_button=Button(button_frame,text="Contact Us",command=self.contact_window,width=20,font=("Comic Sans MS",20,"bold"),bg="grey",fg="gold",bd=1,relief=RAISED,cursor="dot")
        Contact_button.grid(row=5,column=0)


        #------------------------Main Image----------------------------

        img3=Image.open("/Users/pankajsingh/Desktop/HomeService/3.png")
        img3=img3.resize((1200,900),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=301,y=0,width=1136,height=690 ) 


        #------------------------Extra Images--------------------------
        
        img4=Image.open("/Users/pankajsingh/Desktop/HomeService/4.jpeg")
        img4=img4.resize((330,210),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=270,width=300,height=210 )


        img5=Image.open("/Users/pankajsingh/Desktop/HomeService/5.jpeg")
        img5=img5.resize((300,250),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=460,width=300,height=250 )


    def book_window(self):
        self.new_window1=Toplevel(self.root)
        self.book=BookRequestWindow(self.new_window1)

    def dashboard_window(self):
        self.new_window2=Toplevel(self.root)
        self.dashboard=DashboardWindow(self.new_window2)

    def profile_window(self):
        self.new_window3=Toplevel(self.root)
        self.profile=ProfileWindow(self.new_window3)

    def feedback_window(self):
        self.new_window4=Toplevel(self.root)
        self.feedback=FeedbackWindow(self.new_window4)

    def aboutus_window(self):
        self.new_window5=Toplevel(self.root)
        self.about=AboutOurCompanyWindow(self.new_window5)


    def contact_window(self):
        self.new_window6=Toplevel(self.root)
        self.contact=ContactUsWindow(self.new_window6)



if __name__ == "__main__":
    root=Tk()
    obj=HomeService(root)
    root.mainloop()
    


