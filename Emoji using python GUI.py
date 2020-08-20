# importing the necessary modules needed

from tkinter import *

import emojis

# creating a main GUI window

Display = Tk()

Display.title("Emoji Creator...")

Display.geometry("600x600")

Display.configure(bg='blue')

# Giving the display details with attributes of font , colour etc.

Label(Display, text= "Mini Project for Creating Emoji using Python GUI", font =("Times", 15, "bold italic"), fg="black", bg = "blue").pack()

Label(Display, text="1) Smile",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=80, y = 50)

Label(Display, text="2) Relaxed",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=380, y = 50)

Label(Display, text="3) Laughing",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=80, y = 100)

Label(Display, text="4) Flushed",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=380, y = 100)

Label(Display, text="5) Wink",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=80, y = 150)

Label(Display, text="6) Sleeping ",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=380, y = 150)

Label(Display, text="7) Sweat",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=80, y = 200)

Label(Display, text="8) Weary",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=380, y = 200)

Label(Display, text="9) Sob",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=80, y = 250)

Label(Display, text="10) Joy",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=370, y = 250)

Label(Display, text="11) Hushed",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=70, y = 300)

Label(Display, text="12) Unamused",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=370, y = 300)

Label(Display, text="13) Rage",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=70, y = 350)

Label(Display, text="14) Mask",font =("Verdana", 12, "bold"), fg="white", bg = "blue").place(x=370, y = 350)

# Creating a entry box to get user choice.

EntryDis = Label(Display, text="Enter your choice of emoji from the above list", font=("Times", 15, "bold italic"), fg="black", bg = "blue").place(x= 100, y = 400)

value = IntVar()

TextBox = Entry(Display, textvariable=value, width = 30).place(x= 200, y = 450)

# Creeating function for creating the emoji.

def onClick():

    # Creating second windows for displaying the emoji.

    nWin = Toplevel(Display)

    nWin.title("Emoji Created...")
    
    nWin.geometry("600x600")

    nWin.configure(bg='blue')

    iValue = int(value.get())

    Label(nWin,text="EMOJI HAS BEEN CREATED BASED ON USER CHOICE", font =("Times", 15, "bold italic"), fg="White", bg = "blue").place(x=50, y= 460)

    # Based on the user choice the condition is checked using elif
      
    if iValue == 1:

        Label(nWin,text=emojis.encode(":smile:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Smile Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 2:
        
        Label(nWin,text=emojis.encode(":relaxed:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Relaxed Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=230, y = 370)

    elif iValue == 3:
        
        Label(nWin,text=emojis.encode(":laughing:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Laughing Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=260, y = 400)

    elif iValue == 4:
        
        Label(nWin,text=emojis.encode(":flushed:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Flushed Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=260, y = 400)

    elif iValue == 5:
        
        Label(nWin,text=emojis.encode(":wink:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Wink Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 6:
        
        Label(nWin,text=emojis.encode(":sleeping:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Sleeping Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=260, y = 400)

    elif iValue == 7:
        
        Label(nWin,text=emojis.encode(":sweat:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Sweat Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 8:
        
        Label(nWin,text=emojis.encode(":weary:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Weary Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=260, y = 400)

    elif iValue == 9:
        
        Label(nWin,text=emojis.encode(":sob:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Sob Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 10:
        
        Label(nWin,text=emojis.encode(":joy:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Joy Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 11:
        
        Label(nWin,text=emojis.encode(":hushed:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Hushed Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 12:
        
        Label(nWin,text=emojis.encode(":unamused:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Unamused Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 13:
        
        Label(nWin,text=emojis.encode(":rage:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Rage Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    elif iValue == 14:
        
        Label(nWin,text=emojis.encode(":mask:"), font =("Verdana", 150, "bold"), bg="blue").place(x=200, y = 120)

        Label(nWin,text="Mask Emoji", font =("Verdana", 10, "bold"), bg="blue").place(x=270, y = 400)

    # Else is excuted when the user choise is out of range and it destory both main and secondary window completely.

    else:

        nWin.destroy()

        Display.destroy()

# Button to access the function onClick

Submit = Button(Display, text="Submit", command =onClick, fg="White", bg="black").place(x=270, y=500)

Display.mainloop()

