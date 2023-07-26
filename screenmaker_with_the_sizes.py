import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_page_load(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

def take_fullpage_screenshot(driver, url, base_filename, folder, index, window_sizes=None):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode without a visible browser window
    options.add_argument('--start-maximized')  # Start Chrome maximized
    options.add_argument('--disable-gpu')  # Disable GPU acceleration

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    wait_for_page_load(driver)

    if not window_sizes:
        window_sizes = [(1366, 768)]  # Default window size if not provided

    for i, (window_width, window_height) in enumerate(window_sizes, 1):
        driver.set_window_size(window_width, window_height)

        # Get the total height of the webpage
        total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

        # Resize the browser window to match the total height of the webpage
        driver.set_window_size(window_width, total_height)

        # Wait for a moment to ensure the page layout is stable after resizing
        time.sleep(1)

        # Capture the full-page screenshot using the headless browser
        screenshot_filename = f"{base_filename}_{window_width}x{total_height}_{i}.png"
        screenshot_filepath = os.path.join(folder, screenshot_filename)
        driver.save_screenshot(screenshot_filepath)

    driver.quit()

def main():
    driver_path = "/path/to/chromedriver"  # Replace with the path to the chromedriver executable
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    # List of links (replace with your own list of links)
    links = [
        "https://www.kingbilly.com/",
        "https://www.kingbilly.com/news",
        # Add more links here
    ]

    output_folder = "/Users/rustemsamoilenko/Desktop/screenshots"  # Replace with the path to the folder where you want to save the screenshots

    for link_index, link in enumerate(links, 1):
        link_folder = os.path.join(output_folder, f"link_{link_index}")
        os.makedirs(link_folder, exist_ok=True)
        base_filename = os.path.join(link_folder, f"screenshot_{link_index}")
        # You can specify multiple window sizes for each link here.
        # For example, [(1366, 768), (1024, 768)] to capture screenshots for two different sizes.
        # You can add more sizes or modify them as needed.
        window_sizes = [
    (1920, 1080),  # Standard desktop size
    (1366, 768),   # Common laptop size
    (1440, 900),   # Widescreen laptop size

    # Tablets
    (768, 1024),   # iPad portrait
    (1024, 768),   # iPad landscape
    (800, 1280),   # Samsung Galaxy Tab portrait
    (1280, 800),   # Samsung Galaxy Tab landscape

    # Mobiles
    (375, 667),    # iPhone 6/7/8 portrait
    (667, 375),    # iPhone 6/7/8 landscape
    (414, 736),    # iPhone 6/7/8 Plus portrait
    (736, 414),    # iPhone 6/7/8 Plus landscape
    (360, 640),    # Samsung Galaxy S5 portrait
    (640, 360),    # Samsung Galaxy S5 landscape
    (375, 812),    # iPhone X portrait
    (812, 375),    # iPhone X landscape

    # Other Devices
    (320, 568),    # iPhone 5/SE portrait
    (568, 320),    # iPhone 5/SE landscape
    (768, 1280),   # Nexus 4 portrait
    (1280, 768),   # Nexus 4 landscape
    (320, 480),    # iPhone 4 portrait
    (480, 320),    # iPhone 4 landscape
        ]
        
        take_fullpage_screenshot(driver, link, base_filename, link_folder, link_index, window_sizes)

if __name__ == "__main__":
    main()