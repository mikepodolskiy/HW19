# import required modules
import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


# creating class to contain logics from DAO class
class UserService:
    def __init__(self, dao: UserDAO):
        """
        creating constructor, getting dao object inside itself
        :param dao: dao object
        """
        self.dao = dao

    def get_one(self, uid):
        """
        applying get_one() method to dao object
        :param uid: id of required user
        :return:
        """
        return self.dao.get_one(uid)

    def get_all(self, filters):
        """
        checking what filter could be applied
        :param filters: possibly applied filters
        :return: users according to filters
        """
        return self.dao.get_all()

    def create(self, user_d):
        """
        applying a create() method to dao object, using data form response
        """
        return self.dao.create(user_d)

    def update(self, user_d):
        """
        applying  to dao object update() method
        :param user_d: user data
        """
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        """
        getting password as string, converted to bytes and convert to hash version using pbkdf2_hmac as
        sha256 secure hash algorithm shall be used, salt and number of iterations from constants
        :return: password hash
        """
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
