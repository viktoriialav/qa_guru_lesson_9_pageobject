from selene import have, command, be
from selene.support.shared import browser

from demoqa_tests import resource


class RegistrationPage:
    def __init__(self):
        '''
        self.registered_user_data = browser.element('.table').all('td').even
        '''
        self.state = browser.element('#state')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def should_successful_registration(self):
        browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)

    def should_registered_user_with(
        self,
        full_name,
        user_email,
        gender,
        user_number,
        date_of_birth,
        subjects,
        hobbies,
        file_name,
        address,
        state_and_city,
    ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                user_email,
                gender,
                user_number,
                date_of_birth,
                subjects,
                hobbies,
                file_name,
                address,
                state_and_city,
            )
        )

    '''
    @property
    def registered_user_data(self):
        return browser.element('.table').all('td').even
    '''

    def fill_state(self, value):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text('Delhi')
        ).click()

    def press_submit(self):
        browser.element('#submit').perform(command.js.click)

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def upload_picture(self, value):
        browser.element('#uploadPicture').set_value(resource.path(value))
