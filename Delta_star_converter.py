#import everything from tkinter
from tkinter import *
#creating a blank window
root = Tk() 
root.title("Delta Star converter")
root.geometry("900x550")
#create a label put it in the root window and put text in it
#theTitle = Label(root, text = "Delta Star converter") 
#theTitle.pack(fill=X) # put the label in the first empty place you find 

#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side = BOTTOM )


#DeltaCheckBox = Checkbutton(root,text="Delta")
#DeltaCheckBox.grid(row = 0)
#StarCheckBox = Checkbutton(root,text="Star")
#StarCheckBox.grid(row = 0,column=1)
TitleLabel = Label(root,text="Delta Star converter",fg="red",font=("Helvetica",20,"bold"),width=50)
TitleLabel.grid(row = 0,columnspan=2)
QuestionLabel = Label(root,text="If you want to calculate Delta press Delta, If you want to calculate Star press Star",font=(30),width=80,height = 2)
QuestionLabel.grid(row =1 ,columnspan=2)
DeltaButton = Button(root,text = "Delta",fg="black",font=(20),width = 20 ,bg="lightblue")
StarButton = Button(root,text = "Star",fg="black",font=(20),width = 20 ,bg="lightblue")
DeltaButton.grid(row = 2,column = 0)
StarButton.grid(row = 2,column = 1)


###star to Delta Labels and Entry###
#R1 reading
R1Label = Label(root,text="Please enter R1: ",font=(18),width=25,height = 2)
R1 = Entry(root,width=25,font=(20))
#R2 reading
R2Label = Label(root,text="Please enter R2: ",font=(18),width=25,height = 2)
R2 = Entry(root,width=25,font=(20))
#R3 reading
R3Label = Label(root,text="Please enter R3:",font=(18),width=25,height = 2)
R3 = Entry(root,width=25,font=(20))
###Delta to star Labels and Entry###
#R12 reading
R12Label = Label(root,text="Please enter R12: ",font=(18),width=25,height = 2)
R12 = Entry(root,width=25,font=(20))
#R2 reading
R13Label = Label(root,text="Please enter R13: ",font=(18),width=25,height = 2)
R13 = Entry(root,width=25,font=(20))
#R3 reading
R23Label = Label(root,text="Please enter R23:",font=(18),width=25,height = 2)
R23 = Entry(root,width=25,font=(20))

def CalculateDelta(event):
    R1input =R1.get()
    R2input =R2.get()
    R3input =R3.get()
    ResultLabel = Label(root,font=(25))
    R12ResultLabel = Label(root,font=(30),fg="red")
    R13ResultLabel = Label(root,font=(30),fg="red")
    R23ResultLabel = Label(root,font=(30),fg="red")
    ResultLabel.grid(row=9)
    R12ResultLabel.grid(row=10,columnspan=2)
    R13ResultLabel.grid(row=11,columnspan=2)
    R23ResultLabel.grid(row=12,columnspan=2)
    try :
        CheckResistance =(float(R1input) > 0 and float(R2input) >0 and float(R3input)>0)


        R12ResultLabel.grid(row=10,columnspan=2)
        R13ResultLabel.grid(row=11,columnspan=2)
        R23ResultLabel.grid(row=12,columnspan=2)
        ResultLabel.grid(row=9)
        if(CheckResistance):
            ResultLabel.config(text = "Value of Delta resistances is :-",width = 35,font=("Helvetica",15,"bold"))
            R12ResultLabel.config(text = " R12 = "+str( ( float(R1input) + float(R2input) + (( float(R1input) * float(R2input) ))/(float(R3input))))[:10]+" Ohm(s)",width=20,font=("Helvetica",12,"bold"))
            R13ResultLabel.config(text = " R13 = "+str( ( float(R1input) + float(R3input) + (( float(R1input) * float(R3input) ))/(float(R2input))))[:10]+" Ohm(s)",width=20,font=("Helvetica",12,"bold"))
            R23ResultLabel.config(text = " R23 = "+str( ( float(R2input) + float(R3input) + (( float(R2input) * float(R3input) ))/(float(R1input))))[:10]+" Ohm(s)",width=20,font=("Helvetica",12,"bold"))
        else:
            ResultLabel.config(text = "Please enter valid values for resistances",fg="red",font=("Helvetica",15,"bold"))
            R12ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
            R13ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
            R23ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
            #R1.delete(0,END)
            #R2.delete(0,END)
            #R3.delete(0,END)
            #ResultLabel = Label(root,text="Please enter valid values for resistances")
            #ResultLabel.grid(row=7)
    except:
        ResultLabel.config(text = "Please enter valid values for resistances",fg="red",font=("Helvetica",15,"bold"))
        R12ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold")) 
        R13ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
        R23ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
        
        #R1.delete(0,END)
        #R2.delete(0,END)
        #R3.delete(0,END)
        #ResultLabel = Label(root,text="Please enter valid values for resistances")
        #ResultLabel.grid(row=7)

def CalculateStar(event):
    R12input =R12.get()
    R13input =R13.get()
    R23input =R23.get()
    ResultLabel = Label(root,font=(30))
    R1ResultLabel = Label(root,font=(30),fg="red")
    R2ResultLabel = Label(root,font=(30),fg="red")
    R3ResultLabel = Label(root,font=(30),fg="red")
    ResultLabel.grid(row=9)
    R1ResultLabel.grid(row=10,columnspan=2)
    R2ResultLabel.grid(row=11,columnspan=2)
    R3ResultLabel.grid(row=12,columnspan=2)
    try :
        CheckResistance =(float(R12input) > 0 and float(R13input) >0 and float(R23input)>0)

        R1ResultLabel.grid(row=10,columnspan=2)
        R2ResultLabel.grid(row=11,columnspan=2)
        R3ResultLabel.grid(row=12,columnspan=2)
        ResultLabel.grid(row=9)
        if(CheckResistance):
            ResultLabel.config(text = "Value of Star resistances is :-",width = 35,font=("Helvetica",15,"bold"))
            R1ResultLabel.config(text = " R1 = "+str((float(R12input) * float(R13input)/(float(R12input) + float(R13input) + float(R23input))))[:10]+" Ohm(s)",width=20,font=("Helvetica",12,"bold"))
            R2ResultLabel.config(text = " R2 = "+str((float(R12input) * float(R23input)/(float(R12input) + float(R13input) + float(R23input))))[:10]+" Ohm(s)",width=20,font=("Helvetica",12,"bold"))
            R3ResultLabel.config(text = " R3 = "+str((float(R13input) * float(R23input)/(float(R12input) + float(R13input) + float(R23input))))[:10]+" Ohm(s)",width=20,font=("Helvetica",12,"bold"))
        else:
            ResultLabel.config(text = "Please enter valid values for resistances",fg="red",font=("Helvetica",15,"bold"))
            R1ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold")) 
            R2ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
            R3ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
            #R12.delete(0,END) 
            #R13.delete(0,END)
            #R23.delete(0,END)
            #ResultLabel = Label(root,text="Please enter valid values for resistances")
            #ResultLabel.grid(row=7)
    except:
        ResultLabel.config(text = "Please enter valid values for resistances",fg="red",font=("Helvetica",15,"bold"))
        R1ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold")) 
        R2ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
        R3ResultLabel.config(text = "                                                     ",width=20,font=("Helvetica",12,"bold"))
        #R12.delete(0,END)
        #R13.delete(0,END)
        #R23.delete(0,END)
        #ResultLabel = Label(root,text="Please enter valid values for resistances")
        #ResultLabel.grid(row=7)
def StarToDelta(event):
    if R12Label.winfo_exists()==True:
        R12Label.grid_forget()
        R12.grid_forget()
        R13Label.grid_forget()
        R13.grid_forget()
        R23Label.grid_forget()
        R23.grid_forget()
    ChooseLabel = Label(root , text = "Enter Star resistances values to calculate Delta resistances",font=(22),width=70,height = 2)
    ChooseLabel.grid(row=3,columnspan=2)
    R1Label.grid(row = 4)
    R1.grid(row =4,column=1)
    R2Label.grid(row = 5)
    R2.grid(row = 5,column=1)
    R3Label.grid(row = 6)
    R3.grid(row = 6,column=1)
    CalculateButton = Button(root,text="Calculate Delta",bg="LightGreen",font=(20),width=20)
    CalculateButton.grid(row = 7,column = 1)
    CalculateButton.bind("<Button-1>",CalculateDelta)
    

#Delta to star#
def DeltaToStar(event):
    if R1Label.winfo_exists()==True:
        R1Label.grid_forget()
        R1.grid_forget()
        R3Label.grid_forget()
        R3.grid_forget()
        R2Label.grid_forget()
        R2.grid_forget()
    ChooseLabel = Label(root , text = "Enter Delta resistances values to calculate Star resistances",font=(22),width=70,height = 2)
    ChooseLabel.grid(row=3,columnspan=2)
    R12Label.grid(row = 4)
    R12.grid(row =4,column=1)
    R13Label.grid(row = 5)
    R13.grid(row = 5,column=1)
    R23Label.grid(row = 6)
    R23.grid(row = 6,column=1)
    CalculateButton = Button(root,text="Calculate Star",bg="LightGreen",font=(20),width=20)
    CalculateButton.grid(row =7,column = 1)
    CalculateButton.bind("<Button-1>",CalculateStar)



StarButton.bind("<Button-1>",DeltaToStar) #<Button-1> is the left mouse click <Button-2> scroll or middel click <Button-3> right click
DeltaButton.bind("<Button-1>",StarToDelta)



#def Calculate(event):
#    if  R1Label.winfo_exists()==True:
#        return CalculateDelta
    #else:
    #    return CalculateStar


QuiteButton = Button(root,text="Exit",command = root.quit,bg="Tomato",font=(20),width=20,height = 2)
QuiteButton.grid(row = 13,column=1)
InfoLabel = Label(root,text="Submitted By: Abdelrahman Mohamed Hamza Othman",fg="darkblue",font = ("Helvetica",15,"bold"))
InfoLabel.grid(row=14,columnspan = 2)
# Makes the window stay until you close it so it makes it in infinite loop
root.mainloop() 



