# Veeam test automation challenge

Using Selenium WebDriver, please do the following: 
- Open https://cz.careers.veeam.com/vacancies and maximize the browser window.
- Then, choose Research & Development and English from the lists of departments and
languages, respectively.
- Please, count the number of jobs found and compare this value with the expected result.

## Coverage

## Run requirements
- pytest installed
- chromedriver installed
- allure installed
- allure_pytest_bdd installed
- web access

## How to run
In command line and run command from the root project folder
```bash
pytest --alluredir=allure-bdd-results -v Tests/Steps/VacanciesStep.py
```

## Results observing
Test report is generated in Json. If you wish a pretty report page, please run:
````
allure generate --clean --output allure-bdd-report allure-bdd-results                 
````
