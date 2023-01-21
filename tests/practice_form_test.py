from demoqa_tests.model.pages import practice_form


def test_student_registration_form():
    practice_form.given_opened()

    practice_form.required_fields('Pavel', 'Durov', 'durov@mail.ru')

    practice_form.select_gender('Male')

    practice_form.type_phone_number('9998887755')

    practice_form.click_on_datepicker()
    practice_form.pick_month('May')
    practice_form.pick_year('1985')
    practice_form.pick_day(13)

    practice_form.type_subject('English')

    practice_form.select_hobby('Sports')

    practice_form.scroll_to_address()
    practice_form.type_address('Some address')

    practice_form.upload_picture('resources/durov.jpg')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    practice_form.assert_fields(
        'Pavel Durov',
        'durov@mail.ru',
        'Male',
        '9998887755',
        '13 May,1985',
        'English',
        'Sports',
        'durov.jpg',
        'Some address',
        'NCR Delhi'
    )
