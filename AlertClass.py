import sqlite3

Database = sqlite3.connect('Identities')
items = Database.cursor()

"""Alert class used to set alerts that link to the finance department if items run low in stock

Attributes
-----------

private Attributes

---> name
---> department
---> year group

"""


class alertsetter:
    def __init__(self, name=None, department=None, yeargroup=None):
        self.name = name
        self.department = department
        self.yeargroup = yeargroup

    # Method is used to alert the finance department that an item has run low in stock

    def alertfinance(self):
        if self.yeargroup is None:
            items.execute("UPDATE None_yeargroup_specific SET resolved=1 WHERE Name_item=? AND departmentName=?",
                          (self.name, self.department))
            Database.commit()

        else:
            items.execute("UPDATE year_group_specific  SET resolved=1 WHERE Name_item=? AND year_group=? AND departmentName=?",
                          (self.name, self.yeargroup, self.department))
            Database.commit()

    # Method used to update the database about the current out of stock or low in stcok items

    def updateDatabase(self):
        items.execute("UPDATE None_yeargroup_specific SET resolved=1 WHERE currentAmount < MinimumAmount")
        items.execute("UPDATE year_group_specific SET resolved=1 WHERE currentAmount < MinimumAmount")
        Database.commit()
