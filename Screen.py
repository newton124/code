from tkinter import *
from Validatelogin import validate_login_entries
from AddingItem import validate_adding_item_none_yeargroup_specfic, valdidate_adding_yeargroup_specfic
from retrieveItems import retrieveItem
from Retrieveclass import retrieve_items_none_year_group_specific


"""Class used to call the tkinter main screen"""


class screenCall:
    def main():
        root = Tk()
        mainMenu(root)
        root.mainloop()


"""
Tkinter main menu screen

"""


class mainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Main menu")
        self.master.geometry("400x450")

        self.mathsbtnn = Button(self.master, text="Maths department", height="2", width="30", fg="green", command=self.loginMaths)
        self.mathsbtnn.grid(row=0, column=0)

        self.geographybtn = Button(self.master, text="Geography department", height="2", width="30", fg="green", command=self.loginGeography)
        self.geographybtn.grid(row=1, column=0)

        self.historybtn = Button(self.master, text="History department", height="2", width="30", fg="green", command=self.loginHistory)
        self.historybtn.grid(row=2, column=0)

        self.Englishbtn = Button(self.master, text="English department", height="2", width="30", fg="green", command=self.loginEnglish)
        self.Englishbtn.grid(row=3, column=0)

        self.Admin = Button(self.master, text="Admin", height="2", width="30", fg="green", command=self.loginAdmin)
        self.Admin.grid(row=4, column=0)

        self.FinanceDepartment = Button(self.master, text="Finance department", height="2", width="30", fg="green", command=self.loginFinanceDepartment)
        self.FinanceDepartment.grid(row=5, column=0)

        self.Headmaster = Button(self.master, text="Headmaster", height="2", width="30", fg="green", command=self.loginHeadmaster)
        self.Headmaster.grid(row=6, column=0)

    # Methods used to create a login screen object

    def loginMaths(self):
        self.newWindowMaths = Toplevel(self.master)
        self.app1 = loginScreen(self.newWindowMaths, "Maths department")

    def loginGeography(self):
        self.newWindowGeography = Toplevel(self.master)
        self.app2 = loginScreen(self.newWindowGeography, "Geography department")

    def loginHistory(self):
        self.newWindowHistory = Toplevel(self.master)
        self.app3 = loginScreen(self.newWindowHistory, "History department")

    def loginEnglish(self):
        self.newWindowEnglish = Toplevel(self.master)
        self.app4 = loginScreen(self.newWindowEnglish, "English department")

    def loginAdmin(self):
        self.newWindowAdmin = Toplevel(self.master)
        self.app5 = loginScreen(self.newWindowAdmin, "Admin")

    def loginFinanceDepartment(self):
        self.newWindowFinanceDepartment = Toplevel(self.master)
        self.app6 = loginScreen(self.newWindowFinanceDepartment, "Finance Department")

    def loginHeadmaster(self):
        self.newWindowHeadmaster = Toplevel(self.master)
        self.app7 = loginScreen(self.newWindowHeadmaster, "Headmaster")


""" Tkinter login screen

"""


class loginScreen:
    def __init__(self, master, department):
        self.master = master
        self.department = department
        self.master.title("Login Screen " + self.department)
        self.master.geometry("300x250")

        self.username = StringVar()
        self.password = StringVar()

        self.labelUsername = Label(self.master, text="Username *").grid(row=2, column=0)
        self.usernameEntry = Entry(self.master, textvariable=self.username)
        self.usernameEntry.grid(row=3, column=0)

        self.labelPassword = Label(self.master, text="Password *").grid(row=5, column=0)
        self.passwordEntry = Entry(self.master, textvariable=self.password, show="*")
        self.passwordEntry.grid(row=6, column=0)

        self.validatebtn = Button(self.master, text="login", width=10, height=1, command=self.validatelogin)
        self.validatebtn.grid(row=8, column=0)

    def validatelogin(self):
        object1 = validate_login_entries(self.username.get(), self.password.get(), self.department)
        if object1.check_identity_exsists():
            self.homeScreen = Toplevel(self.master)
            self.home = departmentMainScreen(self.homeScreen, self.department)
        else:
            self.usernameEntry.delete(0, END)
            self.passwordEntry.delete(0, END)

    def departmentMainScreen(self):
        # Instantiating a new screen object
        self.newDepartmentWindow = Toplevel(self.master)
        self.new = departmentMainScreen(self.newDepartmentWindow, self.department)


""" Tkinter department Screen

"""


class departmentMainScreen:
    def __init__(self, master, department):
        self.master = master
        self.department = department
        self.master.title(self.department + " Home Screen")
        self.master.geometry("500x500")

        self.label = Label(self.master, text="Select an Option").grid(row=0, column=3)

        self.addItembuttonNoneyeargroup = Button(self.master, text="add item none year group specific",
                                                 width=30, height=3, command=self.addItemNonespecific).grid(row=1, column=3)
        self.addItembuttonYeargroupSpecific = Button(self.master, text="add item year group specific",
                                                     width=30, height=3, command=self.addItempecific).grid(row=2, column=3)
        self.retrieveItemNoneYeargroupSpecific = Button(self.master, text="retrieve none year group specific",
                                                        width=30, height=3, command=self.retrieveItemNone).grid(row=3, column=3)
        self.retrieveItemYeargroupSpecific = Button(self.master, text="retrieve year group specific",
                                                    width=30, height=3, command=self.retriveItemSpecific).grid(row=4, column=3)

    """ Methods link buttons to screen objects
    input (The user clicks the button) --- computation performed within the method --- output ( Screen displayed to the user )

    """

    def addItemNonespecific(self):
        self.addWindow1 = Toplevel(self.master)
        self.new1 = addItemScreen(self.addWindow1, self.department)

    def addItempecific(self):
        self.addWindow2 = Toplevel(self.master)
        self.new2 = addItemScreen2(self.addWindow2, self.department)

    def retrieveItemNone(self):
        self.retrieveWindow1 = Toplevel(self.master)
        self.new3 = retrieveItemScreen(self.retrieveWindow1, self.department)

    def retriveItemSpecific(self):
        pass


"""Tkinter add item to database screen

 add item screen
 ----------------

 class used for None year group specific items

 add item screen 2
 ----------------

class used to add items to year group specific database

add item screen ( Super class ) ---- add item screen 2 ( Sub class )

Subclass inherits from the super class

"""


class addItemScreen:

    LIST_YEAR_GROUPS = [7, 8, 9, 10, 11, 12, 13]
    LIST_AVERAGE = [1, 2, 3, 4, 5]

    def __init__(self, master, department):
        self.master = master
        self.department = department
        self.master.title("Add item")
        self.master.geometry("300x250")

        self.mathsItem1 = StringVar()
        self.mathsAmountNone1 = StringVar()
        self.mathsAmountNone2 = StringVar()
        self.mathsAmountNone3 = StringVar()

        self.label1 = Label(self.master, text="Enter the name of the item").grid(row=0, column=0)
        self.nameItem = Entry(self.master, textvariable=self.mathsItem1)
        self.nameItem.grid(row=1, column=0)

        self.label2 = Label(self.master, text="Enter the avergae amount consumed").grid(row=2, column=0)
        self.average1Entry = OptionMenu(self.master, self.mathsAmountNone1, *addItemScreen.LIST_AVERAGE)
        self.average1Entry.grid(row=3, column=0)
        self.average2Entry = OptionMenu(self.master, self.mathsAmountNone2, *addItemScreen.LIST_AVERAGE)
        self.average2Entry.grid(row=4, column=0)
        self.average3Entry = OptionMenu(self.master, self.mathsAmountNone3, *addItemScreen.LIST_AVERAGE)
        self.average3Entry.grid(row=5, column=0)

        self.button = Button(self.master, text="Add", width=10, height=1, command=self.addItemMethod).grid(row=8, column=0)

    # Mehod used to validate the users input if correct the item is added to the database

    def addItemMethod(self):
        try:
            sum = float(self.mathsAmountNone1.get()) + float(self.mathsAmountNone2.get()) + float(self.mathsAmountNone3.get())
            result = round(float(sum / 3))
            itemObject = validate_adding_item_none_yeargroup_specfic(self.mathsItem1.get(), result, self.department)

            if itemObject.inputItem():
                self.nameItem.delete(0, END)
                self.resultLabel1 = Label(self.master, text="Success", fg="green").grid(row=9, column=0)
            else:
                self.nameItem.delete(0, END)
                self.resultLabel2 = Label(self.master, text="Not Successful", fg="Red").grid(row=9, column=0)
        except ValueError:
            self.nameItem.delete(0, END)
            self.resultLabel1 = Label(self.master, text="select a value", fg="red").grid(row=9, column=0)


class addItemScreen2(addItemScreen):

    def __init__(self, master, department):
        super().__init__(master, department)

        self.departmentNone1 = StringVar()
        self.label3 = Label(self.master, text="Select the Year Group").grid(row=6, column=0)
        self.departmentSelect = OptionMenu(self.master, self.departmentNone1, *addItemScreen.LIST_YEAR_GROUPS)
        self.departmentSelect.grid(row=7, column=0)

        # Inherited attribute is overidden from the inherited class attribute

        self.button = Button(self.master, text="Add", width=10, height=1, command=self.addItemMethod).grid(row=8, column=0)

    """ This method is overidden from the inherited class method
    Polyphorism is used allowing this method to behave differently to the subclass

    """

    def addItemMethod(self):
        try:
            sum = float(self.mathsAmountNone1.get()) + float(self.mathsAmountNone2.get()) + float(self.mathsAmountNone3.get())
            result = round(float(sum / 3))
            itemObject = valdidate_adding_yeargroup_specfic(self.mathsItem1.get(), result, self.department, self.departmentNone1.get())

            if itemObject.inputItem():
                self.nameItem.delete(0, END)
                self.resultLabel1 = Label(self.master, text="Success", fg="green").grid(row=9, column=0)
            else:
                self.nameItem.delete(0, END)
                self.resultLabel2 = Label(self.master, text="Not Successful", fg="Red").grid(row=9, column=0)
        except ValueError:
            self.nameItem.delete(0, END)
            self.resultLabel2 = Label(self.master, text="Select a value", fg="Red").grid(row=9, column=0)


""" Tkinter retrieve item screen

Super class inherits from the subclass

add item screen ( Super class ) ---> add item screen 2 ( Subclass )


retrieve item screen
----------------

class used to retrieve items from none year group specific database

retrieve item screen2
-----------------

class used to retireve items from year group specifc databse


"""


class retrieveItemScreen:

    def __init__(self, master, department):
        self.master = master
        self.department = department
        self.master.title(self.department + " Retrieve item")
        self.master.geometry("300x250")

        self.itemsLists = retrieveItem(self.department).retrieve()

        self.itemWanted = StringVar()
        self.yearGroup = StringVar()

        self.label1 = Label(self.master, text="Retrieve item", width=10, height=1).grid(row=0, column=0)

        self.label2 = Label(self.master, text="Select the item", width=10, height=1).grid(row=2, column=0)
        self.itemsToSelect = OptionMenu(self.master, self.itemWanted, *self.itemsLists)
        self.itemsToSelect.grid(row=3, column=0)

        self.label3 = Label(self.master, text="Enter the Amount", width=10, height=1).grid(row=5, column=0)
        self.entryAmount = Entry(self.master, textvariable=self.yearGroup)
        self.entryAmount.grid(row=6, column=0)

        self.button = Button(self.master, text="Retrieve", width=12, height=1, command=self.retrieveItem).grid(row=8, column=0)

    # Method used to retrieve the item

    def retrieveItem(self):
        try:
            retrieve = retrieve_items_none_year_group_specific(self.itemWanted.get(), int(self.yearGroup.get()), self.department)
            if retrieve.checkAvailability():
                self.entryAmount.delete(0, END)
                Label(self.master, text="Sucesss", fg="green").grid(row=10, column=0)
            else:
                self.entryAmount.delete(0, END)
                Label(self.master, text="Try Again", fg="red").grid(row=10, column=0)
        except ValueError:
            self.entryAmount.delete(0, END)
            Label(self.master, text="Enter a correct Amount", fg="red").grid(row=10, column=0)


class retrieveItemScreen2(retrieveItemScreen):
    def __init__(self, master, department):
        super().__init__(master, department)


"""Tkinter Admin Screen

The main menu for the Admin

"""


class AdminScreen:
    def __init__(self, master):
        self.master = master
        self.department = department
        self.master.title(self.department + " Screen")
        self.master.geometry("500x500")

        self.label = Label(self.master, text="Select a option").grid(row=0, column=3)

        self.button1 = Button(self.master, text="Alter Username & Password", width=30, height=3, command=self.AdminChangeIdetity).grid(row=1, column=3)
        self.button2 = Button(self.master, text="Remove item from database", width=30, height=3, command=self.AdminDeleteItem).grid(row=2, column=3)

    def AdminChangeIdentity(self):
        pass

    def AdminDeleteItem(self):
        pass


"""Tkinter Admin change username and password screen

This is where the Usernames and Passwords of users can be changed

"""


class changeUserPassScreen:

    # List of departments

    LIST_DEPARTMENTS = ["Maths department", "Geography department", "English department",
                        "History department", "Finance department", "Admin", "Headmaster"]

    def __init__(self, master):
        self.master = master
        self.master.title("Change Username & Password")
        self.master.geometry("450x300")

        self.newUser = StringVar()
        self.newPass = StringVar()
        self.depart = StringVar()

        self.label1 = Label(self.master, text="select department Name").grid(row=1, column=0)
        self.departmentEntry = OptionMenu(Admin_change_idetity_screen, self.depart, *LIST_DEPARTMENTS)
        self.departmentEntry.grid(row=2, column=0)

        self.label2 = Label(self.master, text="Enter new Username").grid(row=3, column=0)
        self.newUsername = Entry(self.master, textvariable=self.newPass)
        self.newUsername.grid(row=4, column=0)

        self.label3 = Label(self.master, text="Enter new password").grid(row=5, column=0)
        self.newPassword = Entry(self.master, textvariable=self.newPass)
        self.newPassword.grid(row=6, column=0)

        self.button = Button(self.master, text="Update", command=self.updateData).grid(row=7, column=0)

    # Method called to update the username and password for the user

    def updatedata(self):
        try:
            update = update_username_password(self.newUser.get(), self.newPass.get(), self.depart.get())
            if update.updateIdentity() is True:
                self.label4 = Label(self.master, text="Success", fg="green").grid(row=8, column=0)
                self.newUsername.delete(0, END)
                self.newPassword.delete(0, END)
            else:
                self.label5 = Label(self.master, text="Try Again", fg="Red").grid(row=8, column=0)
                self.newUsername.delete(0, END)
                self.newPassword.delete(0, END)
        except ValueError:
            self.label5 = Label(self.master, text="Try Again", fg="Red").grid(row=8, column=0)
            self.newUsername.delete(0, END)
            self.newPassword.delete(0, END)


screenCall.main()
