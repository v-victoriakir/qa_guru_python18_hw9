import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    birth_year: str
    birth_month: str
    birth_day: str
    text_birth_month: str
    subject: str
    hobbies: str
    avatar: str
    address: str
    state: str
    city: str


user = User(first_name="Maria", last_name="Lopez", email="MLopez@gmail.com",
            gender="Female", mobile_number="0123456789", birth_year="1996", birth_month="9", birth_day="10",
            text_birth_month='October',
            subject="Biology",
            hobbies="Reading", avatar="unnamed.jpg", address="Main street, 55 bld, 10 apt.", state="Rajasthan",
            city="Jaipur")
