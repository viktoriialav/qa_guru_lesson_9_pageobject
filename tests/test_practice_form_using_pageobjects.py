from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Olga')
    registration_page.fill_last_name('YA')
    registration_page.fill_user_email('name@example.com')
    registration_page.select_gender('Female')
    registration_page.fill_user_number('1234567891')

    registration_page.fill_date_of_birth(year='1999', month='May', day='11')

    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies('Reading')

    registration_page.upload_picture('foto.jpg')

    registration_page.fill_current_address('Moscowskaya Street 18')

    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')

    registration_page.press_submit()

    # THEN
    registration_page.should_successful_registration()
    registration_page.should_registered_user_with(
        'Olga YA',
        'name@example.com',
        'Female',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi',
    )

    '''
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )
    '''
