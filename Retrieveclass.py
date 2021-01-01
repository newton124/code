import sqlite3
from AlertClass import alertsetter

# courser used to connect to the database

Database = sqlite3.connect('Identities')
items = Database.cursor()


""" retrieve class used to retrieve items from the database

retrieve class ( Superclass )  ----  retrieve class specifc ( Subclass )

Attributes
------------

private Attributs

---> name
---> amount
---> department

"""


class retrieve_items_none_year_group_specific:
    name_item_length_max = 25
    name_item_length_mini = 3
    average_upper_bound = 6

    def __init__(self, name, amount, department):
        self.name = name
        self.amount = amount
        self.department = department

    def checkinput(self):
        try:
            # check to see if the user has selected and amount and if they have selected a name
            if int(self.amount) > 0 and len(self.name) > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def checkAmount(self, amount):
        if (amount - self.amount) < 0:
            return amount
        else:
            return self.amount

    def checkAvailability(self):
        if self.checkinput():
            items.execute("SELECT currentAmount FROM None_yeargroup_specific WHERE Name_item=? AND departmentName=?",
                          (self.name, self.department))
            identity = items.fetchone()
            Database.commit()

            if self.checkAmount(identity[0]) == self.amount:  # If enough of the requested amount is available returns self.amount
                newCurrentAmount = (identity[0] - self.amount)
                items.execute("UPDATE None_yeargroup_specific SET currentAmount=? WHERE Name_item=? AND departmentName=?",
                              (newCurrentAmount, self.name, self.department))
                Database.commit()
                return True
            else:
                # Not enough resource is available set current amount to zero give them only the remaning amount
                items.execute("UPDATE None_yeargroup_specific SET currentAmount=0 WHERE Name_item=? AND departmentName=?",
                              (self.name, self.department))
                Database.commit()
                # instatiate class + apply method to alert finance
                alertsetter(self.name, self.department).alertfinance()
                return True

        else:
            return False


""" retrieve specififc class used to retieve year group specifc items

Structure
----------
                    retreieve class ( Superclass )
                            |
                            |
             retreive specifc class

Attributes
-----------

private Attributes

---> year group a
---> inherited attributes from the retieve class ( Superclass )



"""


class retrieve_items_year_group_specific(retrieve_items_none_year_group_specific):
    def __init__(self, name, amount, department, yeargroup):
        super().__init__(name, amount, department)
        self.yeargroup = yeargroup

    # Method overidding from the inheited class polyporpism

    def checkinput(self):
        try:
            if int(self.amount) > 0 and len(self.name) > 0 and len(self.yeargroup) > 0:
                return True
            else:
                return False
        except:
            return False

    def checkAvailability(self):
        if self.checkinput():
            items.execute("SELECT currentAmount FROM year_group_specific  WHERE Name_item=:name_item AND year_group=:yeargroup",
                          {"name_item": self.name, "yeargroup": self.yeargroup})
            identity = items.fetchone()
            Database.commit()
            if self.checkAmount(self.amount) == self.amount:
                # enough of the requested reasource is available update new current amount
                newCurrentAmount = (identity[0] - self.amount)
                items.execute("UPDATE year_group_specific  SET currentAmount=? WHERE Name_item=? AND year_group=?",
                              (newCurrentAmount, self.name, self.yeargroup))
                Database.commit()
                return True
            else:
                # Not enough resource is available set current amount to zero give them only the remaning amount
                items.execute("UPDATE year_group_specific  SET currentAmount=0 WHERE Name_item_1=? AND year_group=?",
                              (self.name, self.year_group))
                Database.commit()
                # instatiate class + apply method to alert finance
                alertsetter(self.name, self.department, self.yeargroup).alertfinance()
                return True

        else:
            return False
