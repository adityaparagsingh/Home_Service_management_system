from tkinter import *
from PIL import Image,ImageTk

class DashboardWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Aditya's Home Service Provider:)")
        self.root.geometry("1134x564+306+258")


        #----------------------------TITLE-----------------------------
        lbl_title=Label(self.root,text="Aditya's Home Services",font=("times new roman",35,"bold"),bg="black",fg="gold",bd=4,relief=RAISED,cursor="circle")
        lbl_title.place(x=0,y=0,width=1134,height=50)

        lbl_title2=Label(self.root,text="Dashboard",font=("times new roman",30,),bg="black",fg="gold",bd=4,relief=RAISED,cursor="circle")
        lbl_title2.place(x=0,y=50,width=1134,height=50)


         #-----------------------------LOGO-----------------------------
        img2=Image.open("/Users/pankajsingh/Desktop/HomeService/2.jpeg")
        img2=img2.resize((370,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE,cursor="circle")
        lblimg.place(x=0,y=0,width=175,height=100)




if __name__ == "__main__":
    root = Tk()
    obj=DashboardWindow(root)
    root.mainloop()