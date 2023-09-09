from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.drivers.chrome import ChromeDriver

from Tests.Pages.BasePage import BasePage


class VacanciesPage(BasePage):
    def __init__(self, driver: ChromeDriver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.page_url = "https://cz.careers.veeam.com/vacancies"
        # Page elements locators
        self.accept_cookies_css = "div[id='cookiescript_accept']"
        self.dropdown_options_css = "a[class='dropdown-item']"
        self.checkbox_dropdown_css = "div[class='custom-control custom-checkbox']"
        self.vacancy_card_css = "a[class='card card-sm card-no-hover']"
        self.keyword_css = "input[name='query']"
        self.department_dropdown_xpath = ".//button[text()='All departments']"
        self.language_dropdown_xpath = ".//button[text()='All languages']"
        self.experience_dropdown_xpath = ".//button[text()='Any experience']"
        self.vacancies_count_css = "h3 span[class='text-secondary pl-2']"

    def get_keyword(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, self.keyword_css)

    def get_department_dropdown(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self.department_dropdown_xpath)

    def get_language_dropdown(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self.language_dropdown_xpath)

    def get_experience_dropdown(self) -> WebElement:
        return self.driver.find_element(By.XPATH, self.experience_dropdown_xpath)

    def get_vacancies_count(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, self.vacancies_count_css)

    def get_accept_cookies_btn(self) -> WebElement:
        (WebDriverWait(self.driver, 20)
         .until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.accept_cookies_css))))
        return self.driver.find_element(By.CSS_SELECTOR, self.accept_cookies_css)

    def open_vacancies_page(self):
        self.driver.get(self.page_url)

    def accept_cookies(self):
        self.get_accept_cookies_btn().click()

    def fill_keyword(self, query):
        self.get_keyword().send_keys(query)

    # Opens Department dropdown, waits for dropdown options to be shown
    def select_department(self, text):
        self.get_department_dropdown().click()
        (WebDriverWait(self.driver, 20)
         .until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.dropdown_options_css))))
        opt_list = self.driver.find_elements(By.CSS_SELECTOR, self.dropdown_options_css)
        self.select_option_by_text(opt_list, text)

    # Opens Experience dropdown, waits for dropdown options to be shown
    def select_experience(self, text):
        self.submit_filters()
        self.get_experience_dropdown().click()
        optList = self.driver.find_elements(By.CSS_SELECTOR, self.dropdown_options_css)
        self.select_option_by_text(optList, text)

    # Opens Language dropdown
    def open_language_dropdown(self):
        self.submit_filters()
        self.get_language_dropdown().click()

    # Finds checkbox dropdown to select language
    def select_language(self, text):
        optList = self.driver.find_elements(By.CSS_SELECTOR, self.checkbox_dropdown_css)
        self.select_option_by_text(optList, text)

    # Finds dropdown option by text value and clicks it
    def select_option_by_text(self, options_list, text):
        for opt in options_list:
            if opt.text == text:
                opt.click()
                return opt
        return None

    # Returns number of vacancies cards shown on the page
    def count_vacancies_shown(self):
        list_vacancies = self.driver.find_elements(By.CSS_SELECTOR, self.vacancy_card_css)
        return len(list_vacancies)

    # Returns number shown near "Vacancies open" text
    def get_vacancies_open_num(self):
        return self.get_vacancies_count().text

    # Used to defocus on dropdown filters to hide prev opened dropdown options
    def submit_filters(self):
        self.get_keyword().click()
