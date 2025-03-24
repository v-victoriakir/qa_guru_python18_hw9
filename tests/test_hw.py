from model.pages.practice_form import RegistrationPage


def test_form_submitted():
    practice_form = RegistrationPage()
    (practice_form.open()
    .fill_first_name("Maria")
    .fill_last_name("Lopez")
    .fill_email("MLopez@gmail.com")
    .select_gender("Female")
    .fill_mobile_number("0123456789")
    .fill_date_of_birth(9, 1996, 10)
    .fill_subject('Biology')
    .upload_avatar("unnamed.jpg")
    .select_hobbies("Reading")
    .select_hobbies("Music")
    .fill_current_address("Main street, 55 bld, 10 apt.")
    .select_state("Rajasthan")
    .select_city("Jaipur")
    .submit_form()
    .registered_user_should_have(
        "Maria", "Lopez", "MLopez@gmail.com", "Female", "0123456789", "10 October,1996", "Biology", "Reading, Music",
        "unnamed.jpg", "Main street, 55 bld, 10 apt.", "Rajasthan", "Jaipur"
    ))


def test_form_required_fields_only(today_date):
    practice_form = RegistrationPage()
    (practice_form.open()
    .fill_first_name("Maria")
    .fill_last_name("Lopez")
    .select_gender("Female")
    .fill_mobile_number("0123456789")
    .submit_form()
    .registered_user_should_have(
        "Maria", "Lopez", "", "Female", "0123456789", f"c", "", "",
        "", "", "", ""
    ))


def test_form_error_required_fields_not_filled():
    practice_form = RegistrationPage()
    (practice_form.open()
     .fill_first_name("Maria")
     .select_gender("Female")
     .submit_form()
     .check_if_required_fields_not_filled())


def test_form_required_fields_but_wrong_number():
    practice_form = RegistrationPage()
    (practice_form.open()
     .fill_first_name("Maria")
     .fill_last_name("Lopez")
     .select_gender("Female")
     .fill_mobile_number("123456789")
     .submit_form()
     .check_if_required_fields_not_filled())
