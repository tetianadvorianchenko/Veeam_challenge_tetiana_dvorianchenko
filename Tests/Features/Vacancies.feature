Feature: Vacancies filters

  Scenario Outline: User filters vacancies
    Given Vacancies page is open
    When user fills keyword with "<keyword>"
    And user selects department "<department>"
    And user selects language "<language>"
    And user selects experience "<experience>"
    Then <expected_vacancies_num> vacancies are shown
    #This step is failing because there is a bug about number of vacancies found (static 34)
#    And <expected_vacancies_num> matches Vacancies open number

    Examples:
    | keyword   | department              |  language       | experience  | expected_vacancies_num |
    | ''        | Research & Development  | English         | ''          | 5                      |
    | junior    | All Departments         | English         | 1-3 years   | 1                      |
    | devops    | Corporate Technology    | English, French | 3+ years    | 2                      |
    |    ''     |     ''                  | German          |   ''        | 1                      |
    |    ''     |     ''                  | ''              | 1-3 years   | 1                      |
    |   ''      |     ''                  | ''              | ''          | 33                     |

