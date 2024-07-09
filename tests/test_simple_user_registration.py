from demoqa_tests.data import users
from demoqa_tests.pages.simple_user_registration_page import SimpleUserRegistrationPage, SimpleUserRegistrationSteps
from demoqa_tests.application import app


def test_registration_user():
    registration_page = SimpleUserRegistrationPage()
    vika = users.User(
        full_name='Viktoriia Lav',
        email='newuser@gmail.com',
        current_address='144 Broadway, suit 12',
    )

    registration_page.open()
    registration_page.fill_full_name(vika.full_name)
    registration_page.fill_email(vika.email)
    registration_page.fill_current_address(vika.current_address)
    registration_page.submit()

    registration_page.should_have_submited(vika)


def test_registration_user_admin():
    registration_page = SimpleUserRegistrationPage()
    admin = users.admin

    registration_page.open()
    registration_page.fill_full_name(admin.full_name)
    registration_page.fill_email(admin.email)
    registration_page.fill_current_address(admin.current_address)
    registration_page.submit()

    registration_page.should_have_submited(admin)


def test_registration_user_admin_version_2():
    '''
    Если для тестовой логики не важно, какие пользователь заполняет поля, то такой вариант возможен
    Подходит для высокоуровневых end-to-end тестов, когда тест проходит через большое количество страниц
    '''
    registration_page = SimpleUserRegistrationSteps()

    registration_page.open()
    registration_page.register(users.admin)

    registration_page.should_have_submited(users.admin)


def test_registration_user_admin_with_application():
    '''
    Если для тестовой логики не важно, какие пользователь заполняет поля, то такой вариант возможен
    Подходит для высокоуровневых end-to-end тестов, когда тест проходит через большое количество страниц
    '''
    app.simple_registration_steps.open()

    app.simple_registration_steps.register(users.admin)

    app.simple_registration_steps.should_have_submited(users.admin)
