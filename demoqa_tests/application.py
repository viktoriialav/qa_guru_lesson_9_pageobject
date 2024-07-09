from selene import browser

from demoqa_tests.components.panel import Panel
from demoqa_tests.pages.profile_page import ProfilePage
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.pages.simple_user_registration_page import SimpleUserRegistrationPage, SimpleUserRegistrationSteps


class Application:
    def __init__(self):
        self.simple_registration = SimpleUserRegistrationPage()
        self.simple_registration_steps = SimpleUserRegistrationSteps()
        self.registration_page = RegistrationPage()
        self.profile = ProfilePage()
        self.panel = Panel()

    def open(self):
        browser.open('/')
        return self


app = Application()