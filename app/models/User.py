from system.core.model import *
from flask import flash, escape
import re


# ==================================================================================================================
# USER - MODEL
# ==================================================================================================================
class User(Model):
    def __init__(self):
        super(User, self).__init__()

    # ==================================================================================================================
    # CREATE_NEW: METHOD#
    # Note - make sure pw_hash is of type varchar(255)
    # Do not store the user-entered(human-readable or clear text) password in the database
    # ==================================================================================================================
    def create_new(self, info):
        password = info['password']
        # bcrypt is now an attribute of our model
        # we ill call the bcrypt functions similarly to how we did before
        # here we use generate_password_hash() to generate an encrypted password
        hashed_pw = self.bcrypt.generate_password_hash(password)
        create_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) " \
                       "VALUES (:first_name, :last_name, :email, :pw_hash, NOW()"

        create_data = {
            'first_name': info['first_name'],
            'last_name': info['last_name'],
            'email': info['email'],
            'pw_hash': hashed_pw
        }
    # ==================================================================================================================
    # LOGIN_USER: METHOD
    # ==================================================================================================================
    def login_user(self, info):
        password = info['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': info['email']}
        # same as query_db() but returns one result
        user = self.db.get_one(user_query, user_data)
        if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(user.pw_hash, password):
                return user
        # Whether we did not find the email, or if the password did not match, either way return False
        return False


    # ==================================================================================================================
    # CREATE_USER: METHOD
    # ==================================================================================================================
    def register_user(self, info):
        print info
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = {}
        password = info['password']
        pw_confirm = info['pw_confirm']

        for key in info:
            if not info[key]:
                errors[key] = '{} cannot be blank'.format(key)
            elif key == 'first_name' or key == 'last_name':
                if len(info[key]) < 2:
                    errors[key] = '{} must be at least 2 characters long'.format(key)
            elif key == 'email' and not EMAIL_REGEX.match(info[key]):
                errors[key] = "Email format must be valid"
            elif key == 'password' or key == 'pw_confirm':
                if len(info[key]) < 8:
                    errors[key] = "Password must be at least 8 character long"

        if password != pw_confirm:
            errors['password'] = "Password and confirmation must match"
            errors['pw_confirm'] = "Password and confirmation must match"


        # If we hit errors, return them, else return True
        if errors:
            return {"status": False, "errors": errors}
        else:
            # encrypt password before inserting to database
            hashed_pw = self.bcrypt.generate_password_hash(password)
            query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"

            data = {
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'email': info['email'],
                'pw_hash': hashed_pw
            }



            self.db.query_db(query, data)

            # Then retrieve the last insert users
            get_users_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_users_query)

            print users[0]

            return {"status": True, "user": users[0]}









