from selene import browser, have, command

from model import resource
from model.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.element("#gender-radio-1 + .custom-control-label")
        self.mobile_number = browser.element("#userNumber")

        self.date_of_birth_input = browser.element("#dateOfBirthInput")
        self.year = browser.element(".react-datepicker__year-select")
        self.month = browser.element(".react-datepicker__month-select")

        self.subject_input = browser.element('[id="subjectsInput"]')
        self.hobbies = browser.all('[for^=hobbies-checkbox]')
        self.upload_avatar = browser.element('#uploadPicture')
        self.current_address = browser.element("#currentAddress")
        self.state = browser.element("#state")
        self.city = browser.element("#city")

    def open(self):
        browser.open("/")
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def select_gender(self, value):
        browser.element(f'[value={value}]').element('..').click()
        return self

    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.year.click().element(f'[value="{year}"]').click()
        self.month.click().element(f'[value="{month}"]').click()
        browser.element(f".react-datepicker__day--0{day}").click()
        # self.year.type(year)
        # self.month.type(month)
        return self

    def fill_subject(self, value):
        self.subject_input.type(value).element(
            f'//*[contains(text(),{value})]'
        ).click()
        return self

    def select_hobbies(self, value):
        self.hobbies.element_by(have.text(value)).click()
        return self

    def upload_avatar(self, value):
        self.upload_avatar.set_value(resource.path(value))
        # # self.upload_avatar.type(os.path.abspath(value))
        # # self.upload_avatar.set_value(path(value))
        # self.upload_avatar.set_value(os.path.abspath(f'resources/{value}'))
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def select_state(self, value):
        self.state.scroll_into_view.click().all('[id^=react-select-3-option]').element_by(
            have.exact_text(value)).click()
        return self

    def select_city(self, value):
        self.city.click().all('[id^=react-select-4-option]').element_by(have.text(value)).click()
        return self

    def submit_form(self):
        browser.element("#submit").perform(command.js.scroll_into_view).click()
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_mobile_number(user.mobile_number)
        self.fill_date_of_birth(user.year, user.month, user.day)
        self.fill_subject(user.subject)
        self.upload_avatar(user.avatar)
        self.select_hobbies(user.hobbies)
        self.fill_current_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit_form()
        return self

    def registered_user_should_have(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.mobile_number,
                f'{user.day} {user.month} {user.year}',
                user.subject,
                user.avatar,
                user.hobbies,
                user.address,
                f'{user.state} {user.city}')
        )
        return self
