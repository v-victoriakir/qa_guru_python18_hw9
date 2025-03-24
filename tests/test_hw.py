from model.data.users import user
from model.pages.practice_form import RegistrationPage


def test_submit_practice_form():
    practice_form = RegistrationPage()
    practice_form.open()
    practice_form.register(user)
    practice_form.registered_user_should_have(user)
