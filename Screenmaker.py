import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

def wait_for_page_load(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    
def take_screenshot(driver, url, base_filename, folder, index, window_sizes=None):
    driver.get(url)
    wait_for_page_load(driver)

    if not window_sizes:
        window_sizes = [(1024, 768)]  # Default window size if not provided

    for i, (window_width, window_height) in enumerate(window_sizes, 1):
        driver.set_window_size(window_width, window_height)
        time.sleep(3)  # Wait for 3 seconds after the page is fully loaded
        filename = f"{base_filename}_{index}_window_{i}_{window_width}x{window_height}.png"
        full_filename = os.path.join(folder, filename)
        driver.save_screenshot(full_filename)
        
def main():
    driver_path = "/Users/rustemsamoilenko/Downloads/chromedriver_mac_arm64-2"  # Replace with your ChromeDriver path
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    # List of links (replace with your own list of 800 links)
    links = [
        "https://www.kingbilly.com/",
    "https://www.kingbilly.com/de",
    "https://www.kingbilly.com/en-NZ",
    "https://www.kingbilly.com/news",
        # Add more links here
    ]

    output_folder = "/Users/rustemsamoilenko/Desktop/screenshots"  # Replace with the path to the folder where you want to save the screenshots

    for link_index, link in enumerate(links, 1):
        link_folder = os.path.join(output_folder, f"link_{link_index}")
        os.makedirs(link_folder, exist_ok=True)
        base_filename = os.path.join(link_folder, f"screenshot_{link_index}")
        # You can specify multiple window sizes for each link here.
        # For example, [(1024, 768), (768, 1024)] to capture screenshots for two different sizes.
        # You can add more sizes or modify them as needed.
        window_sizes = [
    # Desktops
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
        
        take_screenshot(driver, link, base_filename, link_folder, link_index, window_sizes)

    driver.quit()

if __name__ == "__main__":
    main()
