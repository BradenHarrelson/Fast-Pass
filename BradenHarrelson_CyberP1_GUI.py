#####################################################################
# Braden Harrelson
# Password Project
# CMPS 4663 Cyber Security
# Dr Halverson
# This program is designed to either check or generate passwords that
# meet the specifications of the user.
#####################################################################

#import Tkinter for gui interface
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#import modules for utility purposes
import string
import random

class FastPass(tk.Tk):
    """This class will drive the overall application.

    This class inherits from the Tkinter library and controls the multiple
    pages of the GUI. Calling this class will create a single instance of the
    application.

    """
    def __init__(self):
        """Initializes the applications basic settings and pages."""
        #call tkinter's init function
        tk.Tk.__init__(self)
        #give some basic settings to our tkinter windows
        tk.Tk.wm_title(self, "FastPass Client")
        tk.Tk.geometry(self, "500x800+500+50")
        #more settings for our tkinter frames
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        #dictionary to hold our frames(pages)
        self.frames = {}
        #load all of our pages so they are avaliable to switch between
        for F in (HomePage, CheckPage, GeneratePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        #start with viewing the homepage
        self.show_frame(HomePage)

    def show_frame(self, cont):
        """Method to bring a window to the visible front of the application"""
        #gets the pages from the page dictionary
        frame = self.frames[cont]
        #raises the page to the top to be viewed
        frame.tkraise()

class HomePage(tk.Frame):
    """This class controls the home page screen for the GUI.

    This class creates the home page and inherits frame properties from
    the FastPass class. This class will be the first page the user sees
    and will direct them to the proper task.

    """
    def __init__(self, parent, controller):
        """Initializes the HomePage's settings and buttons"""
        #call tkinters init function for the page
        tk.Frame.__init__(self, parent, bg = "gray")
        #setup a style for tkinter buttons
        style = ttk.Style()
        style.configure("TButton", foreground="black", background="gray", font = ("None", 12), padding = 10)
        #create labels which are just a way to display text
        label1 = tk.Label(self, text = "Welcome to FastPass!", font = ("None", 24), bg = "gray")
        #the pack function places the element within the window by stuffing it in essentially
        label1.pack(pady = 10, padx = 10)
        label2 = tk.Label(self, text = "Which would you like to do?", font = ("None", 15), bg = "gray")
        label2.pack(pady = 10, padx = 10)
        #creating the buttons that take user to other pages
        b1 = ttk.Button(self, text = "Check a Password", command = lambda: controller.show_frame(CheckPage))
        b1.pack(pady = 10, padx = 10)
        b2 = ttk.Button(self, text = "Generate a Password", command = lambda: controller.show_frame(GeneratePage))
        b2.pack(pady = 10, padx = 10)
        b3 = ttk.Button(self, text = "Quit", command = self.closeProgram)
        b3.pack(pady = 10, padx = 10)
        #some text saying I made this
        label3 = tk.Label(self, text = "Made by Braden Harrelson", font = ("None", 12), bg = "gray")
        label3.pack(pady = 10, padx = 10)
    def closeProgram(self):
        """Method to close the application"""
        #simply closes the application
        exit()

class CheckPage(tk.Frame):
    """This class controls the check page screen for the GUI.

    This class creates the check page and inherits frame properties from
    the FastPass class. This class will be the page that directs the user
    on checking a password.

    """
    def __init__(self, parent, controller):
        """Initializes the CheckPage's settings and buttons"""
        #call tkinters init function for the page
        tk.Frame.__init__(self, parent, bg = "gray")
        #tkinter style for buttons
        style = ttk.Style()
        style.configure("TButton", foreground="black", background="gray")
        #titling page
        label = tk.Label(self, text = "Set Password Specifications", font = ("None", 24), bg = "gray")
        label.pack(pady = 10, padx = 10)
        #creating the length entry field
        label2 = tk.Label(self, text = "Required length of password", font = ("None", 12), bg = "gray")
        label2.pack()
        self.lengthField = tk.Entry(self, width = 3, bg = "white")
        self.lengthField.pack()
        #creating the uppercase letter entry field
        label3 = tk.Label(self, text = "Number of uppercase letters", font = ("None", 12), bg = "gray")
        label3.pack()
        self.upperField = tk.Entry(self, width = 3, bg = "white")
        self.upperField.pack()
        #creating the lowercase letter entry field
        label4 = tk.Label(self, text = "Number of lowercase letters", font = ("None", 12), bg = "gray")
        label4.pack()
        self.lowerField = tk.Entry(self, width = 3, bg = "white")
        self.lowerField.pack()
        #creating the digit entry field
        label5 = tk.Label(self, text = "Number of digits", font = ("None", 12), bg = "gray")
        label5.pack()
        self.digitsField = tk.Entry(self, width = 3, bg = "white")
        self.digitsField.pack()
        #creating the special character entry field
        label6 = tk.Label(self, text = "Number of special characters", font = ("None", 12), bg = "gray")
        label6.pack()
        self.spclField = tk.Entry(self, width = 3, bg = "white")
        self.spclField.pack()
        #creating the exclude dictionary checkbox
        self.excDict = tk.IntVar()
        dictBox = tk.Checkbutton(self, text = "Exclude dictionary words", variable = self.excDict, font = ("None", 12), bg = "gray")
        dictBox.pack()
        #creating the exlude name checkbox
        self.excName = tk.IntVar()
        nameBox = tk.Checkbutton(self, text = "Exclude your name", variable = self.excName, font = ("None", 12), bg = "gray")
        nameBox.pack()
        #creating the exclude email checkbox
        self.excEmail = tk.IntVar()
        emailBox = tk.Checkbutton(self, text = "Exclude your email", variable = self.excEmail, font = ("None", 12), bg = "gray")
        emailBox.pack()
        #empty label for some spacing
        emptyLabel = tk.Label(self, text = " ", font = ("None", 12), bg = "gray")
        emptyLabel.pack()
        #creating the first name entry field
        label7 = tk.Label(self, text = "First Name", font = ("None", 12), bg = "gray")
        label7.pack()
        self.firstField = tk.Entry(self, width = 15, bg = "white")
        self.firstField.pack()
        #creating the last name entry field
        label8 = tk.Label(self, text = "Last Name", font = ("None", 12), bg = "gray")
        label8.pack()
        self.lastField = tk.Entry(self, width = 15, bg = "white")
        self.lastField.pack()
        #creating the email entry field
        label9 = tk.Label(self, text = "Email", font = ("None", 12), bg = "gray")
        label9.pack()
        self.emailField = tk.Entry(self, width = 20, bg = "white")
        self.emailField.pack()
        #creating the password entry field
        label10 = tk.Label(self, text = "Password to Test", font = ("None", 12), bg = "gray")
        label10.pack()
        self.passField = tk.Entry(self, width = 20, bg = "white")
        self.passField.pack()
        #some spacing
        emptyLabel = tk.Label(self, text = " ", font = ("None", 12), bg = "gray")
        emptyLabel.pack(pady = 10, padx = 10)
        #creating the check button which calls the check method
        b1 = ttk.Button(self, text = "Check", command = lambda: self.check())
        b1.pack(pady = 10, padx = 10)
        #creating the finish button which takes you back to the main page
        b2 = ttk.Button(self, text = "Finish", command = lambda: controller.show_frame(HomePage))
        b2.pack(pady = 10, padx = 10)

    def check(self):
        """Method used to collect the parameters and compare them to the password."""
        #bool used to ensure valid input
        validInput = True
        #retrieving all the information from the the entry fields
        length = self.lengthField.get()
        upper = self.upperField.get()
        lower = self.lowerField.get()
        dicAllow = self.excDict.get()
        nameAllow = self.excName.get()
        emailAllow = self.excEmail.get()
        digits = self.digitsField.get()
        spclChars = self.spclField.get()
        firstName = self.firstField.get()
        lastName = self.lastField.get()
        email = self.emailField.get()
        password = self.passField.get()
        #now we check if the input was valid
        #first we check the length
        if not(length.isdigit()):
            validInput = False
            #this displays an error box indicating invalid input
            messagebox.showerror("Invalid Input", "Please enter a valid length.")
        #check the uppercase field
        elif not(upper.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of uppercase letters.")
        #check the lowercase field
        elif not(lower.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of lowercase letters.")
        #check the digits field
        elif not(digits.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of digits.")
        #check the special characters field
        elif not(spclChars.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of special characters.")
        #check the email field
        elif not("@" in email):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid email")
        #if all input is good, we proceed to checkint the password
        if validInput:
            #check length of password
            isLength = len(password) >= int(length)
            #check number of uppcase letters
            isUpper = sum(1 for i in password if i.isupper()) >= int(upper)
            #check number of lowercase letters
            isLower = sum(1 for i in password if i.islower()) >= int(lower)
            #set some flags bc these dont have to be checked always
            isDicAllow = True
            isNameAllow = True
            isEmailAllow = True
            #check number of digits
            isDigits = sum(1 for i in password if i.isdigit()) >= int(digits)
            #check number of special characters
            isSpclChars = sum(1 for i in password if i in string.punctuation) >= int(spclChars)
            #if we are supposed to check it with the dictionary
            if dicAllow == 1:
                #open the dictionary
                inf = open("NewDict.txt")
                #loop through and ensure password does not contain words from dictionary
                for word in inf:
                    word = word.strip()
                    #if the word is in password, set flag to false
                    if word in password.lower():
                        isDicAllow = False
                #close the file
                inf.close()
            #if we are supposed to check the name
            if nameAllow == 1:
                #ensure first and last name are not in the password
                isNameAllow = not(firstName.lower() in password.lower() or lastName.lower() in password.lower())
            #if we are supposed to check the email
            if emailAllow == 1:
                #ensure email is not in the password
                isEmailAllow = not(email.split("@")[0].lower() in password.lower())
            #open the output file that is used to diplay results to be turned in
            outf = open("CheckOutput.txt", "a")
            #display who is using and specifications
            outf.write(firstName + " " + lastName + " " + email + ":\n")
            outf.write("length: " + str(length) + ", upper: " + str(upper) + ", lower: " + str(lower) + ", dictionary: ")
            outf.write(str(bool(dicAllow)) + "\nname: " + str(bool(nameAllow)) + ", email: " + str(bool(emailAllow)))
            outf.write(", digits: " + str(digits) + ", special chars: " + str(spclChars) + "\n")
            outf.write("---------------------------------------------------------------------\n")
            #check the flags in order to display messages to user about invalid standards
            if not(isLength):
                messagebox.showinfo("Standard Not Met", "Password is too short.") 
            elif not(isUpper):
                messagebox.showinfo("Standard Not Met", "Your password doesn't have enough uppercase letters.")
            elif not(isLower):
                messagebox.showinfo("Standard Not Met", "Your password doesn't have enough lowercase letters.")
            elif not(isDicAllow):
                messagebox.showinfo("Standard Not Met", "Your password must not contain a 5+ letter word from the dictionary.")
            elif not(isNameAllow):
                messagebox.showinfo("Standard Not Met", "Your password must not use your name.")
            elif not(isEmailAllow):
                messagebox.showinfo("Standard Not Met", "Your password must not use your email.")
            elif not(isDigits):
                messagebox.showinfo("Standard Not Met", "Your password doesn't have enough digits.")
            elif not(isSpclChars):
                messagebox.showinfo("Standard Not Met", "Your password doesn't have enough special characters.")
            #if all flags are good, display this to the user
            else:
                messagebox.showinfo("Great Password!", "Your password meets all of the standards!")
                #write to file showing accepted
                outf.write("ACCEPTED: ")
                outf.write(password + "\n\n")
                #close file and return bc dont need to write whats wrong to a file
                outf.close()
                return
            #Recheck all of the flags in order to output to a file without breaking the functionality of the GUI
            #display that the pass was rejected and why it was rejected
            outf.write("Rejected: ")
            outf.write(password + "\n")
            #check flags and write to file
            if not(isLength):
                outf.write("Password is too short.\n") 
            if not(isUpper):
                outf.write("Your password doesn't have enough uppercase letters.\n")
            if not(isLower):
                outf.write("Your password doesn't have enough lowercase letters.\n")
            if not(isDicAllow):
                outf.write("Your password must not contain a 5+ letter word from the dictionary.\n")
            if not(isNameAllow):
                outf.write("Your password must not use your name.\n")
            if not(isEmailAllow):
                outf.write("Your password must not use your email.\n")
            if not(isDigits):
                outf.write("Your password doesn't have enough digits.\n")
            if not(isSpclChars):
                outf.write("Your password doesn't have enough special characters.\n")
            outf.write("\n")
            #close the file
            outf.close()

class GeneratePage(tk.Frame):
    """This class controls the generate page screen for the GUI.

    This class creates the generate page and inherits frame properties from
    the FastPass class. This class will be the page that directs the user
    on generating a password.

    """
    def __init__(self, parent, controller):
        """Initializes the GeneratePage's settings and buttons"""
        #call tkinter init function for the page
        tk.Frame.__init__(self, parent, bg = "gray")
        #creating tkinter style for the buttons
        style = ttk.Style()
        style.configure("TButton", foreground="black", background="gray")
        #title for the page
        label = tk.Label(self, text = "Generate a Password", font = ("None", 24), bg = "gray")
        label.pack(pady = 10, padx = 10)
        #creating the length entry field
        label2 = tk.Label(self, text = "Required length of password", font = ("None", 12), bg = "gray")
        label2.pack()
        self.lengthField = tk.Entry(self, width = 3, bg = "white")
        self.lengthField.pack()
        #creating the uppercase letter entry field
        label3 = tk.Label(self, text = "Number of uppercase letters", font = ("None", 12), bg = "gray")
        label3.pack()
        self.upperField = tk.Entry(self, width = 3, bg = "white")
        self.upperField.pack()
        #creating the lowercase letter entry field
        label4 = tk.Label(self, text = "Number of lowercase letters", font = ("None", 12), bg = "gray")
        label4.pack()
        self.lowerField = tk.Entry(self, width = 3, bg = "white")
        self.lowerField.pack()
        #creating the digit entry field
        label5 = tk.Label(self, text = "Number of digits", font = ("None", 12), bg = "gray")
        label5.pack()
        self.digitsField = tk.Entry(self, width = 3, bg = "white")
        self.digitsField.pack()
        #creating the special character entry field
        label6 = tk.Label(self, text = "Number of special characters", font = ("None", 12), bg = "gray")
        label6.pack()
        self.spclField = tk.Entry(self, width = 3, bg = "white")
        self.spclField.pack()
        #creating the exclude dictionary words checkbox
        self.excDict = tk.IntVar()
        dictBox = tk.Checkbutton(self, text = "Exclude dictionary words", variable = self.excDict, font = ("None", 12), bg = "gray")
        dictBox.pack()
        #creating the exclude name checkbox
        self.excName = tk.IntVar()
        nameBox = tk.Checkbutton(self, text = "Exclude your name", variable = self.excName, font = ("None", 12), bg = "gray")
        nameBox.pack()
        #creating the exclude email checkbox
        self.excEmail = tk.IntVar()
        emailBox = tk.Checkbutton(self, text = "Exclude your email", variable = self.excEmail, font = ("None", 12), bg = "gray")
        emailBox.pack()
        #spacing label
        emptyLabel = tk.Label(self, text = " ", font = ("None", 12), bg = "gray")
        emptyLabel.pack()
        #creating first name entry field
        label7 = tk.Label(self, text = "First Name", font = ("None", 12), bg = "gray")
        label7.pack()
        self.firstField = tk.Entry(self, width = 15, bg = "white")
        self.firstField.pack()
        #creating last name entry field
        label8 = tk.Label(self, text = "Last Name", font = ("None", 12), bg = "gray")
        label8.pack()
        self.lastField = tk.Entry(self, width = 15, bg = "white")
        self.lastField.pack()
        #creating email entry field
        label9 = tk.Label(self, text = "Email", font = ("None", 12), bg = "gray")
        label9.pack()
        self.emailField = tk.Entry(self, width = 20, bg = "white")
        self.emailField.pack()
        #spacing label
        emptyLabel = tk.Label(self, text = " ", font = ("None", 12), bg = "gray")
        emptyLabel.pack(pady = 10, padx = 10)
        #button to call the generate method
        b1 = ttk.Button(self, text = "Generate", command = lambda: self.generate())
        b1.pack(pady = 10, padx = 10)
        #button to take the user back to the home page
        b2 = ttk.Button(self, text = "Finish", command = lambda: controller.show_frame(HomePage))
        b2.pack(pady = 10, padx = 10)

    def generate(self):
        """Method used to collect the parameters and generate a password."""
        #bool to ensure valid input
        validInput = True
        #retrieve all the information from the input fields
        length = self.lengthField.get()
        upper = self.upperField.get()
        lower = self.lowerField.get()
        dicAllow = self.excDict.get()
        nameAllow = self.excName.get()
        emailAllow = self.excEmail.get()
        digits = self.digitsField.get()
        spclChars = self.spclField.get()
        firstName = self.firstField.get()
        lastName = self.lastField.get()
        email = self.emailField.get()
        #input checking on all of the input
        if not(length.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid length.")
        elif not(upper.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of uppercase letters.")
        elif not(lower.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of lowercase letters.")
        elif not(digits.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of digits.")
        elif not(spclChars.isdigit()):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid number of special characters.")
        elif not("@" in email):
            validInput = False
            messagebox.showerror("Invalid Input", "Please enter a valid email")
        #if all of the input is valid
        if validInput:
            #create a list of upercase letter of the amount required
            randUpper = random.choices(string.ascii_uppercase, k = int(upper))
            #create a list of lowercase letter of the amount required
            randLower = random.choices(string.ascii_lowercase, k = int(lower))
            #create a list of digits of the amount required
            randDigits = random.choices(string.digits, k = int(digits))
            #create a list of special character of the amount required
            randSpcl = random.choices(string.punctuation, k = int(spclChars))
            #convert the lists into strings
            randUpperStr = "".join(randUpper)
            randLowerStr = "".join(randLower)
            randDigitsStr = "".join(randDigits)
            randSpclStr = "".join(randSpcl)
            #combine the strings
            newPass = "".join([randUpperStr, randLowerStr, randDigitsStr, randSpclStr])
            #ensure the length requirement is met, if not add the difference as lowercase letters
            if int(upper) + int(lower) + int(digits) + int(spclChars) < int(length):
                #find the difference
                dif = int(length) - (int(upper) + int(lower) + int(digits) + int(spclChars))
                intDif = int(dif)
                #generate some more letters
                pad = random.choices(string.ascii_lowercase, k = intDif)
                padStr = "".join(pad)
                #add the new letters onto the newpass string
                newPass += padStr
            #convert the newpass into a list so we can shuffle it
            newPassList = list(newPass)
            #randomizes the newPass
            random.shuffle(newPassList)
            #convert back into a string
            newPass = "".join(newPassList)
            #if excluding dictionary, ensure no words in newPass
            if dicAllow == 1:
                inf = open("NewDict.txt")
                for word in inf:
                    word = word.strip()
                    if word in newPass.lower():
                        #if in dictionary, regenerate
                        self.generate()
                        inf.close()
                        #return to prevent the password from outputting
                        return
                inf.close()
            #check if new pass is equal to name
            if nameAllow == 1:
                if newPass.lower() == firstName.lower() or newPass.lower() == lastName.lower():
                    self.generate()
                    return
            #check if new pass is equal to email
            if emailAllow == 1:
                if newPass.lower() == email.split("@")[0].lower():
                    self.generate()
                    return
            #get file ready for output
            outf = open("GenerateOutput.txt", "a")
            #print out users info and specifications
            outf.write(firstName + " " + lastName + " " + email + ":\n")
            outf.write("length: " + str(length) + ", upper: " + str(upper) + ", lower: " + str(lower) + ", dictionary: ")
            outf.write(str(bool(dicAllow)) + "\nname: " + str(bool(nameAllow)) + ", email: " + str(bool(emailAllow)))
            outf.write(", digits: " + str(digits) + ", special chars: " + str(spclChars) + "\n")
            outf.write("---------------------------------------------------------------------\n")
            outf.write("Generated Pass: " + newPass + "\n\n")
            outf.close()
            #display to the gui
            message = "Your new Password is: \n" + newPass
            messagebox.showinfo("Your New Password", message)


if __name__=='__main__':
    #This main function is run when this module is ran directly
    #create instance of the app running class
    app = FastPass()
    #Tkinter method used to run the gui
    app.mainloop()
    
