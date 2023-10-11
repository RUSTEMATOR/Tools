from playwright.sync_api import Playwright, sync_playwright, Page
import pytest
import allure

class TestData():
    from playwright.sync_api import Page
# Define the list of test data
    test_data = [
        "example#kbc.pp.ua",
        "example@kbc.pp-ua",
        "example@kbc.pp_ua",
        "example@kbc.pp..ua",
        "",  # Empty value
        "exämple@kbc.pp.ua",
        "example@softs_wis..com",
        "example.softswis.com",
        "example@@softswis.com",
        "example@soft swis.com",
        "example@softswis..com",
        "example@"
    ]

@allure.title("Negative emails_check")
# Define the test function
@pytest.mark.parametrize("email", TestData.test_data)
def test_negative_registration(playwright: Playwright, email: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    #--------------------------------------------------------------
    page.goto("https://www.kingbillycasino6.com/")
    allure.attach(page.screenshot(), name="Step 1: Page is reached", attachment_type=allure.attachment_type.PNG)
    
    page.get_by_role("button", name="Registrieren").click()
    allure.attach(page.screenshot(), name="Step 2: Form is opened", attachment_type=allure.attachment_type.PNG)
    
    page.get_by_placeholder("E-Mail").nth(1).click()
    page.get_by_placeholder("E-Mail").nth(1).fill(email)
    allure.attach(page.screenshot(), name="Step 3: Email is filled", attachment_type=allure.attachment_type.PNG)
    
    
    page.get_by_placeholder("Passwort").nth(1).click()
    page.get_by_placeholder("Passwort").nth(1).fill("123")
    allure.attach(page.screenshot(), name="Step 4: Password is filled", attachment_type=allure.attachment_type.PNG)
    
    page.locator(".modal-registr__form > form > div:nth-child(2) > div > div:nth-child(2) > .custom-checkbox > span").first.click()
    page.get_by_role("button", name="Registrieren").nth(1).click()
    allure.attach(page.screenshot(), name="Final result", attachment_type=allure.attachment_type.PNG)

    # Check if registration failed
    if page.locator(".modal-registr__form > form > div:nth-child(2) > div > div:nth-child(2) > .custom-checkbox > span").first.is_visible():
        # Registration failed, test passed for this input
        pass
    else:
        # Registration succeeded, test failed for this input
        assert False, f"Registration succeeded for email: {email}"

    # -----------------------------------------------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


