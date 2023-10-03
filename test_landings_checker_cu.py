import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# List of links to test
class Links():
    links_to_test = [
    'https://lp.kbtraf.com/au-bfc/',
    'https://lp.kbtraf.com/au-freak/',
    'https://lp.kingbillycasino.com/welcome_pack-2-25fs-en/',
    'https://lp.kingbillycasino.com/welcomepack-50fs-ndb-en/'
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
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        return f'{random_word}{random_numbers}@kbc.pp.ua'


@allure.title("Test Registration")
class Registration(Generator, TestBase, Links):
    def navigate_to_link(self, link):
        # Navigate to the link
        print(f'Navigating to: {link}')
        self._driver.get(link)
    
    @allure.step("Click 'GET IT NOW' button")
    def click_get_it_button(self):
        # Click the "GET IT NOW" button by XPath (if it doesn't have an ID)
        print('Clicking "GET IT NOW" button')
        wait = WebDriverWait(self._driver, 10)
        get_it_now_button = wait.until(EC.element_to_be_clickable((By.ID, 'submit-btn')))
        get_it_now_button.click()

    @allure.step("Fill in email input") 
    def fill_email(self):
        try:
            # Find and fill in the email input by ID
            email_input = self._driver.find_element(By.ID, 'email')
            random_email = Generator.generate_random_email()
            print(f'Filling in email input with: {random_email}')
            email_input.send_keys(random_email)
            # Write email to the log file
            with open('test_accs_automation.txt', 'a') as file:
                file.write(random_email + '\n')
                
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill_Email", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill_Email_Failure", attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("Fill in password") 
    def fill_password(self):
        try:
            # Find and fill in the password input by ID
            password_input = self._driver.find_element(By.ID, 'password')
            print('Filling in password input with: 193786Az()')
            password_input.send_keys('193786Az()')
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill_password", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill_password_Failure", attachment_type=allure.attachment_type.PNG)
            raise e
    
    @allure.step("Write list of accs in a separate document")
    def write_accs_list(self):
        random_email = Generator.generate_random_email()    
        # Write email to the log file
        with open('test_accs_automation.txt', 'a') as file:
            file.write(random_email + '\n')

        
    
    @allure.step("Wait for the Sign up button to appear")
    def wait_for_element(self):
        try:
            # Wait for "Sign up now" button to be clickable based on the determined XPath
            print('Waiting for "Sign up now" button to be clickable')
            wait = WebDriverWait(self._driver, 3)
            
            allure.attach(self._driver.get_screenshot_as_png(), name="wait_for_element", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="wait_for_element_Failure", attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Click Sign up button")
    def sign_up(self):
        try:
            sign_up_button = self._driver.find_element(By.CSS_SELECTOR, "#reg-form > div.form_box.form_box__submit")
            sign_up_button.click()
            # Wait for navigation to complete
            time.sleep(10)  # You may need to adjust the waiting time
        
            allure.attach(self._driver.get_screenshot_as_png(), name="sign_up", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="sign_up_Failure", attachment_type=allure.attachment_type.PNG)
            raise e
        
        
        # Check the current URL
        current_url = self._driver.current_url
        print(f'Current URL: {current_url}')

    @allure.step("Verify Step")
    def verify_url(self, expected_term):
        try:
            current_url = self._driver.current_url
            # Verify if the expected term is present in the URL
            if expected_term in current_url:
                print(f'URL verification passed. Expected term: {expected_term} found in URL: {current_url}')
                verification_result = f'URL Verification Passed for Link: {current_url} - Expected term: {expected_term} found in URL: {current_url}\n'
            else:
                print(f'URL verification failed. Expected term: {expected_term} not found in URL: {current_url}')
                verification_result = f'URL Verification Failed for Link: {current_url} - Expected term: {expected_term} not found in URL: {current_url}\n'
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Verify_url", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Verify_url_Failure", attachment_type=allure.attachment_type.PNG)
            raise e




@pytest.mark.parametrize("link", Links.links_to_test)
def test_registration(link):
    registration = Registration()
    registration.setup_method()
    registration.navigate_to_link(link)
    registration.click_get_it_button()
    time.sleep(1)
    registration.fill_email()
    registration.fill_password()
    registration.write_accs_list()
    registration.wait_for_element()
    registration.sign_up()
    time.sleep(2)
    expected_term = "kingbillycasino"
    registration.verify_url(expected_term)
    registration.teardown_method()


