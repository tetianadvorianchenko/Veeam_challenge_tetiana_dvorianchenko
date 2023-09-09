from pytest_bdd import scenario, given, when, then, parsers, scenarios

from Tests.Pages.VacanciesPage import VacanciesPage


@scenario('../Features/Vacancies.feature', 'User filters vacancies')
def test_publish():
    pass


@given('Vacancies page is open', target_fixture="vacancies_page")
def open_vacancies_page(init_driver):
    vacancies_page = VacanciesPage(init_driver)
    vacancies_page.open_vacancies_page()
    vacancies_page.accept_cookies()
    return vacancies_page


@when(parsers.parse('user fills keyword with "{keyword}"'))
def fill_keyword(vacancies_page: VacanciesPage, keyword: str):
    if keyword != "''":
        vacancies_page.fill_keyword(keyword)


@when(parsers.parse('user selects department "{department}"'))
def select_department(vacancies_page: VacanciesPage, department: str):
    if department != "''":
        vacancies_page.select_department(department)


@when(parsers.parse('user selects language "{language}"'))
def select_language(vacancies_page: VacanciesPage, language: str):
    langs = language.split(",")
    if len(langs) > 0:
        vacancies_page.open_language_dropdown()
        for lang in langs:
            vacancies_page.select_language(lang)
        vacancies_page.submit_filters()


@when(parsers.parse('user selects experience "{experience}"'))
def select_experience(vacancies_page: VacanciesPage, experience: str):
    if experience != "''":
        vacancies_page.select_experience(experience)


@then(parsers.parse('{num} vacancies are shown'))
def check_vacancies_number(vacancies_page: VacanciesPage, num: int):
    assert (int(num) == vacancies_page.count_vacancies_shown()), \
        f"Actual is {vacancies_page.count_vacancies_shown()} , expected is {num}"


@then(parsers.parse('{num} matches Vacancies open number'))
def check_vacancies_number(vacancies_page: VacanciesPage, num: int):
    assert (int(num) == vacancies_page.get_vacancies_open_num()), \
        f"Actual is {vacancies_page.get_vacancies_open_num()} , expected is {num}"
