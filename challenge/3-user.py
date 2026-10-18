#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """

    __password = None

    def __init__(self):
        """
        Initialize a new user:
        - assigned an unique `id`
        """
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """
        Password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - `None` if `pwd` is `None`
        - `None` if `pwd` is not a string
        - Hash `pwd` in MD5 before assign to `__password`
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        Valid password:
        - `False` if `pwd` is `None`
        - `False` if `pwd` is not a string
        - `False` if `__password` is `None`
        - Compare `__password` and the MD5 value of `pwd`
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password


if __name__ == '__main__':
    u = User()
    if u.password is not None:
        print("Password should be None by default")

    u.password = "Test"
    if u.password != "0cbc6611f5540bd0809a388dc95a615b":
        print("Password should be hashed in MD5")

    if not u.is_valid_password("Test"):
        print("is_valid_password should return True if it's the right password")

    if u.is_valid_password("Wrong"):
        print("is_valid_password should return False if it's a wrong password")

    u.password = None
    if u.password is not None:
        print("Password should be None if set to None")
