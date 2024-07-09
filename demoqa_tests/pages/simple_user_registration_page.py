from selene import browser, have

from demoqa_tests.data.users import User


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/text-box')

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def submit(self):
        self.submit_button.click()

    def fill_current_address(self, value):
        self.current_address.type(value)

    def should_have_submited(self, user: User):
        browser.element('#output').element('#name').should(have.text(user.full_name))
        browser.element('#output').element('#email').should(have.text(user.email))
        browser.element('#output').element('#currentAddress').should(
            have.text(user.current_address)
        )


class SimpleUserRegistrationSteps:
    def __init__(self):
        self.page = SimpleUserRegistrationPage()

    def open(self):
        self.page.open()

    def register(self, user: User):
        self.page.full_name.type(user.full_name)
        self.page.email.type(user.email)
        self.page.current_address.type(user.current_address)
        self.page.submit_button.click()

    '''
    def register(self, user: User):
        self.page.fill_full_name(user.full_name)
        self.page.fill_email(user.email)
        self.page.fill_current_address(user.current_address)
        self.page.submit()
    '''

    def should_have_submited(self, user: User):
        self.page.should_have_submited(user)


class SimpleUserRegistrationSteps2(SimpleUserRegistrationPage):
    def register(self, user: User):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.submit_button.click()

    '''
    def register(self, user: User):
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.fill_current_address(user.current_address)
        self.submit()
    '''


