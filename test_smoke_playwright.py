from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pytest



class Generator():
    random_email = None
    @staticmethod
    # Function to generate a random email
    def generate_random_email():
        import random
        import string
        if Generator.random_email is None:
            random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
            Generator.random_email = f'{random_word}@kbc.pp.ua'
        
        return Generator.random_email



def test_smoke(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    random_email = Generator.generate_random_email()
    
    page.goto("https://www.kingbillycasino6.com/")
    page.get_by_placeholder("E-Mail").click()
    page.get_by_placeholder("E-Mail").fill(random_email)
    page.get_by_placeholder("Passwort").click()
    page.get_by_placeholder("Passwort").fill("193786Az()")
    page.locator("label").filter(has_text="E-Mail-Aktionen erhalten *").locator("span").first.click()
    page.locator("label").filter(has_text="Ich bin über 18 Jahre alt und akzeptiere die AGB und Datenschutzrichtlinie *").locator("span").first.click()
    page.locator("label").filter(has_text="E-Mail-Aktionen erhalten *").locator("span").first.click()
    page.locator("label").filter(has_text="E-Mail-Aktionen erhalten *").click()
    page.get_by_role("button", name="Registrieren").click()
    time.sleep(4)


    page.get_by_role("banner").get_by_role("link").first.click()
    page.get_by_role("link", name="Abmelden").click()
    page.locator(".close").first.click()
    time.sleep(2)
    page.get_by_role("banner").get_by_role("link").first.click()
    page.locator(".mobile-locale__icon > img").click()
    page.locator(".mobile-locale__drop > li > .mobile-locale__link").first.click()
    page.locator(".close").first.click()
    
    time.sleep(2)
    
    page.get_by_role("banner").get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Enter your email").fill(random_email)
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("193786Az()")
    page.get_by_placeholder("Enter your password").press("Enter")
    
    time.sleep(2)
    
    page.get_by_role("banner").get_by_role("link").first.click()
    page.locator(".mobile-locale__icon > img").click()
    page.locator(".mobile-locale__drop > li > .mobile-locale__link").first.click()
    page.locator(".close").first.click()
    
    time.sleep(1)
    
    page.get_by_role("button", name="Decline").click()
    page.get_by_role("banner").get_by_role("button", name="Deposit").click()
    
    time.sleep(4)
    
    page.get_by_label("First name\n        *").click()
    page.get_by_label("First name\n        *").fill("Testirovshik")
    page.get_by_label("Last name\n        *").click()
    page.get_by_label("Last name\n        *").click()
    page.get_by_label("Last name\n        *").fill("OchenUmnij")
    page.get_by_placeholder("DD").click()
    page.get_by_placeholder("DD").fill("10")
    page.get_by_placeholder("MM").fill("10")
    page.get_by_placeholder("YYYY").fill("1999")
    page.get_by_label("City\n        *").click()
    page.get_by_label("City\n        *").fill("BestTester")
    page.get_by_label("Address\n        *").click()
    page.get_by_label("Address\n        *").fill("NewTest 10")
    page.get_by_label("Postal code\n        *").click()
    page.get_by_label("Postal code\n        *").fill("1234")
    page.get_by_placeholder("+ (country code) (number)").click()
    page.get_by_placeholder("+ (country code) (number)").fill("+4987654876")
    
    time.sleep(2)
    
    page.get_by_role("button", name="Save").click()
    
    time.sleep(1)
    page.locator(".profile-radio__point").first.click()
    page.get_by_role("button", name="Save").click()
    
    page.get_by_role("dialog").get_by_role("button", name="Deposit").click()
    
    page.frame_locator("#devcode_popup iframe").frame_locator("iframe[name=\"\\32 \\.8743708367345974e\\+24\"]").get_by_role("banner").locator("a").click()
    page.get_by_text("✕").click()
    page.get_by_role("dialog").locator("button").nth(4).click()
    
    time.sleep(4)
    
    page.get_by_role("link", name="Search").click()
    page.get_by_role("textbox", name="Find your game").click()
    page.get_by_role("textbox", name="Find your game").fill("Fire lig")
    page.locator("a").filter(has_text="Fire Lightning").click()
    page.locator('a.footer__link i._jackpot').click()
    page.frame_locator("#game-block").frame_locator("iframe").locator("#spin-area").click()
    page.frame_locator("#game-block").frame_locator("iframe").locator("#spin-area").press("Space")
    page.frame_locator("#game-block").frame_locator("iframe").get_by_text("x", exact=True).click()
    
    time.sleep(3)
    page.get_by_role("button", name="Close").click()
    
    
    page.get_by_role("link", name="Testirovshik").click()
    page.get_by_role("link", name=" Profile").click()
    page.get_by_role("link", name=" Bonuses").click()
    page.get_by_placeholder("Type it here").click()
    page.get_by_placeholder("Type it here").fill("SPIN")
    page.get_by_role("button", name="").click()
    context.tracing.stop(path="trace.zip")
    
    if page.get_by_role("heading", name="Casino: The code is incorrect, please contact support for additional details.").first.is_visible():
        pass
    else:
        assert False, "We failed"
        
    context.close()
    browser.close()
    

    
