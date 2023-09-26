import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.common.keys import Keys


# List of links to test
class Links():
    links_to_test = [
        'https://lp.kingbilly.com/ca-bfc/',
        'https://lp.kingbilly.com/ca-freak/',
        'https://lp.kingbilly.com/welcome_pack_new-blue-nl/',
        'https://lp.kingbilly.com/nl-his/',
        'https://lp.kingbilly.com/nl-freak/',
        'https://lp.kingbilly.com/nl-bfc/'
        # Add more links as needed
    ]

class TestBase():
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(15)

    def teardown_method(self): 
        self._driver.quit


class Generator():
    @staticmethod
    # Function to generate a random email
    def generate_random_email():
        import random
        import string
        random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        return f'{random_word}@kbc.pp.ua'


@allure.title("Test Registration")
class Registration(Generator, TestBase, Links):
    def navigate_to_link(self, link):
        # Navigate to the link
        print(f'Navigating to: {link}')
        self._driver.get(link)

    @allure.step("Clicking Get It Now button")    
    def click_get_it_button(self):
        # Click the "GET IT NOW" button by XPath (if it doesn't have an ID)
        print('Clicking "GET IT NOW" button')
        wait = WebDriverWait(self._driver, 10)
        get_it_now_button = wait.until(EC.element_to_be_clickable((By.ID, 'submit-btn')))
        get_it_now_button.click()

    @allure.step("Filling email")    
    def fill_email(self):    
        # Find and fill in the email input by ID
        email_input = self._driver.find_element(By.ID, 'email')
        random_email = Generator.generate_random_email()
        print(f'Filling in email input with: {random_email}')
        email_input.send_keys(random_email)
        # Write email to the log file
        with open('test_accs_automation.txt', 'a') as file:
            file.write(random_email + '\n')

    @allure.step("Filling password")   
    def fill_password(self):
        # Find and fill in the password input by ID
        password_input = self._driver.find_element(By.ID, 'password')
        print('Filling in password input with: 193786Az()')
        password_input.send_keys('193786Az()')
        password_input.send_keys(Keys.TAB)
   
    @allure.step("Click Checkbox")
    def click_checkbox(self):
        try:
            check_box = self._driver.find_element(By.CLASS_NAME, 'label_radio')
            # If the element was found, click it
            check_box.click()
        except Exception as e:
            print(f'Error while interacting with the checkbox: {str(e)}')
        
    @allure.step("Clicking button 'Next'")
    def click_next_button(self):    
        next_button = self._driver.find_element(By.ID, "second_step")
        next_button.click()

    @allure.step("Fill first name input")    
    def fill_first_name(self):    
        # Generate random name and surname using Faker
        fake = Faker()
        first_name = fake.first_name()

        # Fill in First name input
        first_name_input = self._driver.find_element(By.ID, 'first-name')
        first_name_input.send_keys(first_name)

    @allure.step("Fill surname input")    
    def fill_surname(self):
        fake = Faker()
        surname = fake.last_name()     

        # Fill in surname input 
        surname_input = self._driver.find_element(By.ID, 'last-name')
        surname_input.send_keys(surname)
        
    @allure.step("Fill birth date inputs")    
    def fill_birth_date(self):    
            # Choose 03, 03 and 1999 from the day, month and year dropdown lists
        day_dropdown = self._driver.find_element(By.ID, 'date-of-birth-dd')
        month_dropdown = self._driver.find_element(By.ID, 'date-of-birth-mm')
        year_dropdown = self._driver.find_element(By.ID, 'date-of-birth-yy')
        day_dropdown.send_keys('3')
        month_dropdown.send_keys('3')
        year_dropdown.send_keys('1999')
        
    @allure.step("Choose gender")
    def choose_gender(self):
        # Press on "Male" button
        male_button = self._driver.find_element(By.ID, 'm')
        male_button.click()
    
    @allure.step("Proceed")
    def press_next_button(self):
        # Press on "Next" button
        next_button_2 = self._driver.find_element(By.ID, 'last_step')
        next_button_2.click()


    @allure.step("Fill in city input")
    def fill_city(self):
        # Fill in city input with "Besttester"
        city_input = self._driver.find_element(By.ID, 'city')
        city_input.send_keys('Besttester')

    @allure.step("Fill in address input")    
    def fill_address(self):    
        # Fill in address input with "Scripting street 23"
        address_input = self._driver.find_element(By.ID, 'address')
        address_input.send_keys('Scripting street 23')

    @allure.step("Fill in postal code")    
    def fill_postal_code(self):    
         # Fill in postal code input with 1234
        postal_code_input = self._driver.find_element(By.ID, 'postal-code')
        postal_code_input.send_keys('1234')
      
    @allure.step("Assign value to datapicker")
    def assign_value_datapicker(self):
        datepicker = self._driver.find_element(By.TAG_NAME, "kbc-datepicker")
        # Assigning value (phone number)
        phone_number = "07145 99 25 82" 
        self._driver.execute_script('arguments[0].setAttribute("value", arguments[1]);', datepicker, phone_number)
    
    @allure.step("Press on 'Create' button")
    def press_create_button(self):
        # Press on "Create Account" button
        create_account_button = self._driver.find_element(By.NAME, 'send_data')
        create_account_button.click()

    @allure.step("Check url")
    def check_url(self):
        # Check the current URL
        current_url = self._driver.current_url
        print(f'Current URL: {current_url}')


@pytest.mark.parametrize("link", Links.links_to_test)
def test_registration(link):
    registration = Registration()
    registration.setup_method()
    registration.navigate_to_link(link)
    registration.click_get_it_button()
    registration.fill_email()
    registration.fill_password()
    registration.click_checkbox()
    registration.click_next_button()
    registration.fill_first_name()
    registration.fill_surname()
    registration.fill_birth_date()
    registration.choose_gender()
    registration.press_next_button()
    registration.fill_city()
    registration.fill_address()
    registration.fill_postal_code()
    registration.assign_value_datapicker()
    registration.press_create_button()
    time.sleep(5)
    registration.check_url()
    registration.teardown_method()
