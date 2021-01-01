import sqlite3
import DepartmentStudentAmounts as dsa

Database = sqlite3.connect('Identities')
items = Database.cursor()


"""class used to validate the adding none year group specific items

Attributes
-----------

private Attributes

---> name item
---> average
---> department



"""


class validate_adding_item_none_yeargroup_specfic:
    name_item_length_max = 25
    name_item_length_mini = 3
    average_upper_bound = 6
    average_lower_bound = 1
    total_students = 0
    DefaultStockAlertValue = 0

    def __init__(self, name_item, average, department):
        self.name_item = name_item
        self.average = average
        self.department = department

    # Method is used to check the user inputs

    def check(self):
        if validate_adding_item_none_yeargroup_specfic.name_item_length_mini < len(self.name_item) <= validate_adding_item_none_yeargroup_specfic.name_item_length_max and validate_adding_item_none_yeargroup_specfic.average_lower_bound <= self.average < validate_adding_item_none_yeargroup_specfic.average_upper_bound:
            return True
        else:
            return False

    # Method is used to perform claculation about the amount that should be inputted into the database

    def calculations(self):
        # Loops through the dictonary calculating the total amount of students
        for i in dsa.StudentAmounts:
            value = dsa.StudentAmounts[i][self.department]
            # Adds the value to the total students class variable
            self.total_students += value
        return self.total_students

    # Method is used to perform the final calcultaion abou the amount that would be inputted to the database

    def final_calc(self):
        TotalStudents = self.calculations()
        CurrentAmount = TotalStudents * self.average
        MinimumAmount = round((CurrentAmount * 0.1), 0)
        return CurrentAmount, MinimumAmount

    # Method is used to check if the item already exsists in the database

    def checkItem_exsist(self):
        previous = self.check()
        if previous:
            items.execute("SELECT * FROM None_yeargroup_specific WHERE Name_item=?", (self.name_item,))
            item = items.fetchone()
            Database.commit()
            if item is not None:
                return True
            else:
                return False
        else:
            return True

    # Method is used to input the item to the database

    def inputItem(self):
        previous = self.checkItem_exsist()
        if previous is False:
            CalculationResults = self.final_calc()
            CurrentAmount = CalculationResults[0]
            MinimumAmount = CalculationResults[1]
            items.execute("INSERT INTO None_yeargroup_specific VALUES (?, ?, ?, ?, ?)", (self.name_item, CurrentAmount, MinimumAmount, self.department, validate_adding_item_none_yeargroup_specfic.DefaultStockAlertValue))
            result = Database.commit()
            if result is not None:
                return False
            else:
                return True
        else:
            return False


"""Subclass used to validate entries

Subclass ( valdidate_adding_yeargroup_specfic ) inherites from Superclass ( validate_adding_item_none_yeargroup_specfic )

      subclass                                              superclass
validate_adding_item_none_yeargroup_specfic  ----->  valdidate_adding_yeargroup_specfic


Attributes
-----------
---> year group
+ the inherted attributes

"""


class valdidate_adding_yeargroup_specfic(validate_adding_item_none_yeargroup_specfic):
    def __init__(self, name_item, average, department, yeargroup):
        super().__init__(name_item, average, department)
        self.yeargroup = yeargroup

    # Polyphorism may be able to be used on this method by overriding it.

    def calculation(self):
        amount_students = dsa.StudentAmounts["Year " + self.yeargroup][self.department]
        result = self.average * amount_students
        Minimum_amount = round(result * 0.3)
        return result, Minimum_amount

    # Polyphorism used on this method by overriding it.

    def checkItem_exsist(self):
        previous = self.check()
        print(previous)
        if previous:
            items.execute("SELECT * FROM year_group_specific WHERE Name_item=? AND year_group=?", (self.name_item, self.yeargroup))
            result = Database.commit()
            if result is not None:
                return True
            else:
                return False
        else:
            return False
        # The method check would be called first if True connect to year group specific database and determine if the item exsist or not.

    # Polyphorism is used here to input the item. (Overidding)
    def inputItem(self):
        previous = self.checkItem_exsist()
        if previous is False:
            # return tuple (result, minmum amount)
            result = self.calculation()
            MinimumAmount = result[1]
            CurrentAmount = result[0]
            items.execute("INSERT INTO year_group_specific VALUES (?, ?, ?, ?, ?, ?)", (self.name_item, CurrentAmount, MinimumAmount, self.department, self.yeargroup, validate_adding_item_none_yeargroup_specfic.DefaultStockAlertValue, ))
            result = Database.commit()
            if result is not None:
                return False
            else:
                return True
        else:
            return False
