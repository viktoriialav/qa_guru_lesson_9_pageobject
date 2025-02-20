from selene import have
from selene.support.shared import browser

from demoqa_tests.pages.profile_page import ProfilePage


class Panel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, item):
        # update later
        self.container.all('.menu-item').element_by(have.exact_text(item)).click()

    def open_profile(self):
        self.open('Profile')
        return ProfilePage()
