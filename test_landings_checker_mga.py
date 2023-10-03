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

    @allure.step("Filling password")   
    def fill_password(self):
        try:
            # Find and fill in the password input by ID
            password_input = self._driver.find_element(By.ID, 'password')
            print('Filling in password input with: 193786Az()')
            password_input.send_keys('193786Az()')
            password_input.send_keys(Keys.TAB)
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill_password", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill_password_Failure", attachment_type=allure.attachment_type.PNG)
            raise e
   
    @allure.step("Click Checkbox")
    def click_checkbox(self):
        try:
            try:
                check_box = self._driver.find_element(By.CLASS_NAME, 'label_radio')
                # If the element was found, click it
                check_box.click()
            except Exception as e:
                print(f'Error while interacting with the checkbox: {str(e)}')
                
            allure.attach(self._driver.get_screenshot_as_png(), name="Click_checkbox", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Click_checkbox_Failure", attachment_type=allure.attachment_type.PNG)
            raise e
    
    @allure.step("Select currency")
    def select_currency(self):
        try:
            #Select EUR as currency 
            currency_dropdown = self._driver.find_element(By.ID, "sel_currency")
            currency_dropdown.send_keys('EUR')
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Select currency", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Select_currency_Failure", attachment_type=allure.attachment_type.PNG)
            raise e
    
    @allure.step("Select country")
    def select_country(self):
        try:
            #Select Germany
            country_dropdown = self._driver.find_element(By.ID, "sel_country")
            country_dropdown.send_keys('Deutschland')
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Select country", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Select country Failure", attachment_type=allure.attachment_type.PNG)
            raise e
    
    @allure.step("Clicking button 'Next'")
    def click_next_button(self):
        try:  
            next_button = self._driver.find_element(By.ID, "second_step")
            next_button.click()
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Clicking button 'Next", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Clicking button 'Next Failure", attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Fill first name input")    
    def fill_first_name(self):
        # Generate random name and surname using Faker
        fake = Faker()
        first_name = fake.first_name()
        
        try:
            # Fill in First name input
            first_name_input = self._driver.find_element(By.ID, 'first-name')
            first_name_input.send_keys(first_name)
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill first name input", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill first name input Failure", attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Fill surname input")    
    def fill_surname(self):
        fake = Faker()
        surname = fake.last_name()     

        try:
            # Fill in surname input 
            surname_input = self._driver.find_element(By.ID, 'last-name')
            surname_input.send_keys(surname)
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill surname input", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill surname input Failure", attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("Fill birth date inputs")    
    def fill_birth_date(self):
        try:
                # Choose 03, 03 and 1999 from the day, month and year dropdown lists
            day_dropdown = self._driver.find_element(By.ID, 'date-of-birth-dd')
            month_dropdown = self._driver.find_element(By.ID, 'date-of-birth-mm')
            year_dropdown = self._driver.find_element(By.ID, 'date-of-birth-yy')
            day_dropdown.send_keys('3')
            month_dropdown.send_keys('3')
            year_dropdown.send_keys('1999')
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill birth date inputs", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill birth date inputs Failure", attachment_type=allure.attachment_type.PNG)
            raise e
        
    @allure.step("Choose gender")
    def choose_gender(self):
        try:
            # Press on "Male" button
            male_button = self._driver.find_element(By.ID, 'm')
            male_button.click()
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Choose gender", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Choose gender Failure", attachment_type=allure.attachment_type.PNG)
            raise e
    
    @allure.step("Proceed")
    def press_next_button(self):
        
        try:
            # Press on "Next" button
            next_button_2 = self._driver.find_element(By.ID, 'last_step')
            next_button_2.click()
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Proceed", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Proceed Failure", attachment_type=allure.attachment_type.PNG)
            raise e


    @allure.step("Fill in city input")
    def fill_city(self):
        try:
            # Fill in city input with "Besttester"
            city_input = self._driver.find_element(By.ID, 'city')
            city_input.send_keys('Besttester')
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill in city input", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill in city input Failure", attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Fill in address input")    
    def fill_address(self):
        try:
            # Fill in address input with "Scripting street 23"
            address_input = self._driver.find_element(By.ID, 'address')
            address_input.send_keys('Scripting street 23')

            allure.attach(self._driver.get_screenshot_as_png(), name="Fill in address input", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill in address input Failure", attachment_type=allure.attachment_type.PNG)
            raise e
        

    @allure.step("Fill in postal code")    
    def fill_postal_code(self):
        try:   
            # Fill in postal code input with 1234
            postal_code_input = self._driver.find_element(By.ID, 'postal-code')
            postal_code_input.send_keys('1234')
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill in postal code", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Fill in postal code Failure", attachment_type=allure.attachment_type.PNG)
            raise e
      
    @allure.step("Assign value to datapicker")
    def assign_value_datapicker(self):
        try:
            datepicker = self._driver.find_element(By.TAG_NAME, "kbc-datepicker")
            # Assigning value (phone number)
            phone_number = "07145 99 25 82" 
            self._driver.execute_script('arguments[0].setAttribute("value", arguments[1]);', datepicker, phone_number)
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Assign value to datapicker", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Assign value to datapicker Failure", attachment_type=allure.attachment_type.PNG)
            raise e
        
    
    @allure.step("Press on 'Create' button")
    def press_create_button(self):
        try:
            # Press on "Create Account" button
            create_account_button = self._driver.find_element(By.NAME, 'send_data')
            create_account_button.click()
            
            allure.attach(self._driver.get_screenshot_as_png(), name="Press on 'Create' button", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Press on 'Create' button Failure", attachment_type=allure.attachment_type.PNG)
            raise e
    
    @allure.step("Press on 'Deposit' button")
    def press_deposit_button(self):
        try:
            #press on "Deposit" button
            deposit_button = self._driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/header/div[1]/div[1]/div/div[1]/div/span/a[2]/button")
            deposit_button.click()

            allure.attach(self._driver.get_screenshot_as_png(), name="Press on 'Deposit' button", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(self._driver.get_screenshot_as_png(), name="Press on 'Deposit' button Failure", attachment_type=allure.attachment_type.PNG)
            raise e

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
    time.sleep(2)
    registration.fill_email()
    registration.fill_password()
    registration.click_checkbox()
    registration.select_country()
    registration.select_currency()
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
    registration.press_deposit_button()
    time.sleep(3)
    expected_term = "kingbilly"
    registration.verify_url(expected_term)
