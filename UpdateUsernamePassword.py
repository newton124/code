from ValidateLogin import validate_login_entries
from Hashclass import hash_password
import sqlite3

# database connection

Database = sqlite3.connect('Identities')
items = Database.cursor()


""" update username and password class inherits from validate login entries class

Structure
----------

               validate Login entries ( SuperClass )
                            |
                            |
         update username and password


Attributes
-----------

private Attributes

---> username
---> password
---> department name


"""


class update_username_password(validate_login_entries):

    def __init__(self, username, password, department_name):
        super().__init__(username, password, department_name)

    # Method first ------> checks if the username and password entries are correct -----> checks if the user exists

    def checkExists(self):
        previous = self.check_inputs()
        if previous:
            items.execute("SELECT * FROM logins WHERE Name_department=:name", {"name": self.department_name})
            result = items.fetchone()
            Database.commit()
            if result is not None:
                return True
            else:
                return False
        else:
            return False

    # Updates the new users username and password

    def updateIdenity(self):
        previous = self.checkExists()
        hashed_password = hash_password(self.password).hashed()
        if previous:
            items.execute("UPDATE logins SET Username=?, Password_hash=? WHERE Name_department=?", (self.username, hashed_password, self.department_name))
            Database.commit()
            return True
        else:
            False
