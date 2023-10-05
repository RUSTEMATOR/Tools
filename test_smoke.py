import allure
import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Links for the test
class Links():
    links_to_test = [
        'https://www.kingbillycasino.com/'
    ]

# Needed test setup
class TestBase():
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(15)

    def teardown_method(self):
        self._driver.quit()

# Login test suite
@allure.suite("Log In Test")
class LogInCheck(TestBase):

    @allure.step("Navigating to link: {link}")
    def navigate_to_link(self, link):
        print(f'Navigating to: {link}')
        self._driver.get(link)
        allure.attach(self._driver.get_screenshot_as_png(), name="Navigate_to_Link", attachment_type=allure.attachment_type.PNG)

    @allure.step("Closing Cookie Banner")
    def close_cookie(self):
        decline_button = self._driver.find_element(By.XPATH, "//button[@class='cookies-policy__btn cookies-policy__btn--inactive ng-scope']")
        decline_button.click()
        print("Closed Cookie Banner")
        allure.attach(self._driver.get_screenshot_as_png(), name="Close_Cookie", attachment_type=allure.attachment_type.PNG)

    @allure.step("Clicking on Log In button")
    def click_on_login(self):
        login_button = self._driver.find_element(By.XPATH, "//header//a[@class='login_lnk ng-scope'][1]")
        login_button.click()
        print("Clicked on Log In button")
        allure.attach(self._driver.get_screenshot_as_png(), name="Click_Login", attachment_type=allure.attachment_type.PNG)

    @allure.step("Filling in email field")
    def fill_email(self):
        email_field = self._driver.find_element(By.ID, "email")
        email_field.send_keys("samoilenkofluttershy@gmail.com")
        print("Filled in email field")
        allure.attach(self._driver.get_screenshot_as_png(), name="Fill_Email", attachment_type=allure.attachment_type.PNG)

    @allure.step("Filling in password field")
    def fill_passsword(self):
        password_field = self._driver.find_element(By.ID, "password")
        password_field.send_keys("193786Az")
        print("Filled in password field")
        allure.attach(self._driver.get_screenshot_as_png(), name="Fill_Password", attachment_type=allure.attachment_type.PNG)

    @allure.step("Clicking on Login button")
    def click_login(self):
        login = self._driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/form[1]/div[3]/input")
        login.click()
        print("Clicked on Login button")
        allure.attach(self._driver.get_screenshot_as_png(), name="Click_Login_Button", attachment_type=allure.attachment_type.PNG)

# Deposit test suite
@allure.suite("Deposit Test")
class Deposit(LogInCheck, TestBase):

    @allure.step("Clicking on Deposit button")
    def click_deposit(self):
        deposit_button = self._driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/header/div[1]/div[1]/div/div[1]/div/span/a[2]/button")
        deposit_button.click()
        print("Clicked on Deposit button")
        allure.attach(self._driver.get_screenshot_as_png(), name="Click_Deposit", attachment_type=allure.attachment_type.PNG)

    @allure.step("Clicking on SOFORT payment method")
    def click_on_sofort(self):
        sofort = self._driver.find_element(By.XPATH, "/html/body/div[5]/div/div/payments-tabs/div/div[2]/payments/form/div[2]/div[2]/div[2]/div[2]/div[2]/payment-method-item[1]/div")
        sofort.click()
        print("Clicked on SOFORT payment method")
        allure.attach(self._driver.get_screenshot_as_png(), name="Click_SOFORT", attachment_type=allure.attachment_type.PNG)

    @allure.step("Pressing Deposit button")
    def press_deposit(self):
        deposit_confirm = self._driver.find_element(By.XPATH, "/html/body/div[5]/div/div/payments-tabs/div/div[2]/payments/form/div[3]/div[3]/div/button")
        deposit_confirm.click()
        print("Pressed Deposit button")
        allure.attach(self._driver.get_screenshot_as_png(), name="Press_Deposit", attachment_type=allure.attachment_type.PNG)

    @allure.step("Touching the page")
    def touch_page(self):
        input_field = self._driver.find_element(By.XPATH, "/html/body/mwl-root/main/mwl-form/section/mwl-form-iban/form/mwl-form-input/div/div/input")
        input_field.click()
        print("Touched the page")
        allure.attach(self._driver.get_screenshot_as_png(), name="Touch_Page", attachment_type=allure.attachment_type.PNG)

    @allure.step("Verifying URL with expected term: {expected_term}")
    def verify_url(self, expected_term):
        current_url = self._driver.current_url
        if expected_term in current_url:
            print(f'URL verification passed. Expected term: {expected_term} found in URL: {current_url}')
            verification_result = f'URL Verification Passed for Link: {current_url} - Expected term: {expected_term} found in URL: {current_url}\n'
        else:
            logger.error(f'URL verification failed. Expected term: {expected_term} not found in URL: {current_url}')
            verification_result = f'URL Verification Failed for Link: {current_url} - Expected term: {expected_term} not found in URL: {current_url}\n'

        self._driver.back()

# GameCheck test suite
@allure.suite("Game Check Test")
class GameCheck(Deposit, TestBase):

    @allure.step("Pressing on Search button")
    def press_on_search(self):
        search_button = self._driver.find_element(By.CLASS_NAME, "search-panel")
        search_button.click()
        print("Pressed on Search button")
        allure.attach(self._driver.get_screenshot_as_png(), name="Press_Search_Button", attachment_type=allure.attachment_type.PNG)

    @allure.step("Filling the search field with text: {search_text}")
    def fill_search_field(self, search_text):
        search_field = self._driver.find_element(By.ID, "search")
        search_field.send_keys(search_text)
        print(f'Filled the search field with text: {search_text}')
        allure.attach(self._driver.get_screenshot_as_png(), name="Fill_Search_Field", attachment_type=allure.attachment_type.PNG)

    @allure.step("Clicking on Game link")
    def click_on_game(self):
        game = self._driver.find_element(By.CLASS_NAME, "search__link")
        game.click()
        print("Clicked on Game link")
        allure.attach(self._driver.get_screenshot_as_png(), name="Click_Game_Link", attachment_type=allure.attachment_type.PNG)

    @allure.step("Closing banner")
    def close_banner(self):
        cross = self._driver.find_element(By.XPATH, "//*[@id='mm-0']/div[2]/div/div[3]/div/div[1]/ul/li[5]/div/a/i[@class='iconfonts icon-close']")
        cross.click()
        print("Closed banner")
        allure.attach(self._driver.get_screenshot_as_png(), name="Close_Banner", attachment_type=allure.attachment_type.PNG)

    @allure.step("Making a bet")
    def make_bet(self):
        bet_button = self._driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[1]/div[2]/div/canvas[1]')

        # Define the coordinates where you want to click within the canvas
        x_coordinate = 445
        y_coordinate = 704

        self._driver.execute_script(f"arguments[0].dispatchEvent(new MouseEvent('click', {{'clientX': {x_coordinate}, 'clientY': {y_coordinate}}}))", bet_button)
        print("Made a bet")
        allure.attach(self._driver.get_screenshot_as_png(), name="Make_Bet", attachment_type=allure.attachment_type.PNG)

@pytest.mark.parametrize("link", Links.links_to_test)
def test_smoke(link):
    gamecheck = GameCheck()
    gamecheck.setup_method()
    gamecheck.navigate_to_link(link)
    gamecheck.close_cookie()
    gamecheck.click_on_login()
    gamecheck.fill_email()
    gamecheck.fill_passsword()
    gamecheck.click_login()

    gamecheck.click_deposit()
    gamecheck.click_on_sofort()
    gamecheck.press_deposit()
    gamecheck.touch_page()
    expected_term = "https://bankstransfer.com/"
    gamecheck.verify_url(expected_term)

    time.sleep(1)
    gamecheck.close_cookie()
    gamecheck.press_on_search()
    gamecheck.fill_search_field("Fire Lightning")
    gamecheck.click_on_game()
    time.sleep(2)
    gamecheck.close_banner()
    gamecheck.make_bet()
