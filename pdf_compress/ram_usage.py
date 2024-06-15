import psutil
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# File paths
pdf_upload_path = "/Users/yuvarajvasam/Developer/Python/others/pdf_compress/sel/input.pdf"  # Update this to your PDF location
download_dir = "/Users/yuvarajvasam/Developer/Python/others/pdf_compress/sel/"  # Update this to your desired download path

# Chrome options
options = Options()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_setting_values.notifications": 2  # Disable notifications
}
options.add_experimental_option("prefs", prefs)

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    # Start tracking memory usage
    process = psutil.Process(os.getpid())

    # Step 1: Navigate to the website
    driver.get("https://bigpdf.11zon.com/en/compress-pdf")

    # Step 2: Close the popup
    try:
        close_popup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "zon-donation-popup-close"))
        )
        close_popup_button.click()
    except Exception as e:
        print("No popup found or failed to close popup:", e)

    # Step 3: Click "Select PDF" button to open the file selector
    select_pdf_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@id='zon-f-s-btn-txt']/ancestor::button"))
    )
    select_pdf_button.click()

    # Step 4: Upload the PDF file
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    file_input.send_keys(pdf_upload_path)

    # Step 5: Set the compression level if needed
    compression_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "compress-input-range"))
    )
    compression_input.clear()
    compression_input.send_keys("60")

    # Step 6: Click the "Compress" button
    compress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "apply-button"))
    )
    compress_button.click()

    # Step 7: Click the "Download" button to save the compressed PDF
    download_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "zon-download-cbtn0"))
    )
    download_button.click()

    # Wait a few seconds to ensure the download starts
    time.sleep(10)

finally:
    # Output memory usage
    memory_info = process.memory_info()
    print(f"Memory usage: {memory_info.rss / (1024 * 1024)} MB")

    # Close the browser
    driver.quit()

print(f"File downloaded to {download_dir}")
