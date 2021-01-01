import sqlite3
import hashlib
from Hashclass import hash_password


Database = sqlite3.connect('Identities')
items = Database.cursor()
result = hashlib.sha256(str.encode("Watiki123")).hexdigest()


"""class used to validate the username and password entries

Attributes
---------
private attributes

--> username
--> password
--> department name

"""


class validate_login_entries:
    # class Variables used to validate the users inputs
    Minimum_username_length = 5
    Maximum_username_length = 10
    Minimum_password_length = 3
    department_name_length = 4

    def __init__(self, username, password, department_name):
        self.username = username
        self.password = password
        self.department_name = department_name
# Method used to check inputs lenght criteria returns a boolean value

    def check_inputs(self):
        if validate_login_entries.Minimum_username_length < len(self.username) < validate_login_entries.Maximum_username_length and len(self.password) > validate_login_entries.Minimum_password_length and len(self.department_name) > validate_login_entries.department_name_length:
            return True
        else:
            return False
# method used to check if identity exsists in the database returns a boolena value

    # method that checks if the idnetity exsists
    def check_identity_exsists(self):
        hashed_password = hash_password(self.password).hashed()
        # calling the previous method
        check = self.check_inputs()
        # Evaluating the previous method and seeing if it returned true or false
        if check:
            items.execute("SELECT * FROM logins WHERE Name_department=:name_department AND Username=:username AND Password_hash=:password_hashed",
                          {"name_department": self.department_name, "username": self.username, "password_hashed": hashed_password})
            identity = items.fetchone()
            Database.commit()

            if identity is None:
                return False

            else:
                return True
        else:
            return False
