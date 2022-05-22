class RegisterMessages:
    LOG_IN = "Log in"
    SIMILAR_PASS = "The password is too similar to the username."
    REGISTER = "Register new user"
    ALREADY_EXISTS = "A user with that username already exists."
    ERROR_USERNAME = (
        "Enter a valid username. This value may contain "
        "only letters, numbers, and @/./+/-/_ characters."
    )
    PASS_DIDNT_MATCH = "The two password fields didn’t match."
    ERROR_SHORT_PASS = (
        "This password is too short. It must contain at least 8 characters."
    )
    ERROR_COMMON_PASS = "This password is too common."
    ERROR_NUMERIC_PASS = "This password is entirely numeric."
    ERROR_INVALID_EMAIL = "Enter a valid email address."
    ERROR_AGE = "You are young!"


class LoginMessages:
    LOGIN = "Aleppo"
    PASSWORD = "qwerqwerqwerqwer"
    LOG_IN = "Log in"
    ERROR_USERNAME_OR_PASS = (
        "Please enter a correct username and password. "
        "Note that both fields may be case-sensitive."
    )


class OrderMessages:
    LOGIN = "Aleppo"
    PASSWORD = "qwerqwerqwerqwer"
    BASKETS_HEADER = "Your booking: Aleppo"
    CUSTOMER = "customer: Aleppo"
    YOUR_ORDER = "Ваши заказы, Aleppo"
    INFO_HOTEL_IN_BASKET_COUNTRY = "Country:"
    INFO_HOTEL_IN_BASKET_ACCOMMODATION = "Accommodation:"
    INFO_HOTEL_IN_BASKET_PRICE = "Cost per day:"
    INFO_HOTEL_IN_BASKET_COUNT_NIGHTS = "Number of nights:"
    STATUS_ORDER = "формируется"
