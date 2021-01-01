import hashlib

"""Class used to hash user password inputs using sha256"""


class hash_password:
    # Constructor used to instantiate each class
    def __init__(self, password):
        self.password = password  # Attribute is passed during the instatiation of the class

    def hashed(self):
        return hashlib.sha256(str.encode(self.password)).hexdigest()
