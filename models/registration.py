from faker import Faker
import logging

faker = Faker()


class RegisterUserModel:
    """
    User generator.
    """

    def __init__(self, username: str = None, password_1: str = None,
                 password_2: str = None, firstname: str = None, email: str = None):
        self.username = username
        self.firstname = firstname
        self.password_1 = password_1
        self.password_2 = password_2
        self.email = email

    @staticmethod
    def random():
        username = faker.first_name_female() + faker.last_name_nonbinary()
        firstname = faker.first_name()
        email = faker.email()
        password = faker.password()
        logging.info(f"user: {username}, email: {email}, pass: {password}, firstname: {firstname}")
        return RegisterUserModel(email=email, password_1=password,
                                 password_2=password, firstname=firstname, username=username)
