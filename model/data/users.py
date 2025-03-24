import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    year: str
    month: str
    day: str
    subject: str
    hobbies: str
    avatar: str
    address: str
    state: str
    city: str


user = User(first_name="Maria", last_name="Lopez", email="MLopez@gmail.com",
            gender="Female", mobile_number="0123456789", year="1996", month="9", day="10",
            subject="Biology",
            hobbies="Reading", avatar="unnamed.jpg", address="Main street, 55 bld, 10 apt.", state="Rajasthan",
            city="Jaipur")
