from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE_LINK = "http://users.bugred.ru"
    #USER_ICON = (By.CSS_SELECTOR, "#fat-menu").dropdown-toggle
    USER_ICON = (By.CSS_SELECTOR, ".dropdown-toggle")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#main-menu :nth-child(2) a")
    EXIT_BUTTON = (By.CSS_SELECTOR, ".dropdown-menu :nth-child(3)")
    SEARCH_NAME_EMAIL = (By.CSS_SELECTOR, "table :nth-child(4) .form-control")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn.btn-submit")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".ajax_load_row :nth-child(1) :nth-child(6) a") # кнопка в 1 строке
    NAME_IN_TABLE_USER = (By.CSS_SELECTOR, ".ajax_load_row :nth-child(1) :nth-child(2)") # имя в 1 строке


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, ".col-md-6 :nth-child(4) .table.center")
    REGISTER_NAME = (By.CSS_SELECTOR, ".table.center [name='name']")
    REGISTER_E_MAIL = (By.CSS_SELECTOR, ".table.center [name='email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, ".col-md-6 :nth-child(4) .table.center [name='password']")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".col-md-6 :nth-child(4) .table.center .btn")
    REGISTER_MESSAGE = (By.CSS_SELECTOR, ".col-md-6 :nth-child(4) p")
    LOGIN_FORM = (By.CSS_SELECTOR, ".col-md-6 :nth-child(3) .table.center")
    LOGIN_E_MAIL = (By.CSS_SELECTOR, ".table.center [name='login']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, ".col-md-6 :nth-child(3) .table.center [name='password']")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".col-md-6 :nth-child(3) .table.center .btn")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#main-menu li:nth-child(2)")
        
class CompaniesPageLocators():
    pass

class TasksPageLocators():
    pass

class UserPageLocators():
    pass