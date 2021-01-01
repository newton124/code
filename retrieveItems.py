import sqlite3

Database = sqlite3.connect('Identities')
items = Database.cursor()


"""class used to retieve items from the different databases

Attributes
------------

private Attributes

---> department name
---> year group ( Set to None by deafult )
---> list ( Contains the list of items that the user would be able to choose from )

"""


class retrieveItem:
    def __init__(self, departmentName, yearGroup=None):
        self.departmentName = departmentName
        self.yearGroup = yearGroup
        self.list = []

    """retrieves the items from the different databases

    Determines which table to get the records from by observing the inputs

    year group ( private attribute  ) is  None
          retrieve items from the none year group specific table

    year group ( private attribute ) is not None
          retrieve items from the year group specific table

    """

    def retrieve(self):
        if self.yearGroup is None:
            items.execute("SELECT Name_item FROM None_yeargroup_specific WHERE departmentName=?", (self.departmentName,))
            identity = items.fetchall()
            Database.commit()
            for i in identity:
                self.list.append(i[0])
            return self.list
        else:
            items.execute("SELECT Name_item FROM year_group_specific WHERE departmentName=?", (self.departmentName,))
            identity = items.fetchall()
            Database.commit()
            for i in identity:
                self.list.append(i[0])
            return self.list
