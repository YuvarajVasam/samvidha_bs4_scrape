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
    "safebrowsing.esabled": True,
    "profile.default_content_setting_values.notifications": 2  # Disable notifications
}
options.add_experimental_option("prefs", prefs)

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Function to get memory usage
d                                   ef get_memory_usage(process):
    return process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

# Initialize process for memory monitoring
process = psutil.Process(os.getpid())

# List to store memory usage for each step
memory_usage = []

# Step 1: Initialization
memory_usage.append(("Initialization", get_memory_usage(process)))

try:
    # Step 2: Navigate to the website
    driver.get("https://bigpdf.11zon.com/en/compress-pdf")
    memory_usage.append(("Navigate to Website", get_memory_usage(process)))

    # Step 3: Close the popup
    try:
        close_popup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "zon-donation-popup-close"))
        )
        close_popup_button.click()
    except Exception as e:
        print("No popup found or failed to close popup:", e)
    memory_usage.append(("Close Popup", get_memory_usage(process)))

    # Step 4: Click "Select PDF" button
    select_pdf_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@id='zon-f-s-btn-txt']/ancestor::button"))
    )
    select_pdf_button.click()
    memory_usage.append(("Select PDF Button Clicked", get_memory_usage(process)))

    # Step 5: Upload the PDF file
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    file_input.send_keys(pdf_upload_path)
    memory_usage.append(("Upload PDF", get_memory_usage(process)))

    # Step 6: Set compression level
    compression_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "compress-input-range"))
    )
    compression_input.clear()
    compression_input.send_keys("60")
    memory_usage.append(("Set Compression Level", get_memory_usage(process)))

    # Step 7: Click "Compress" button
    compress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "apply-button"))
    )
    compress_button.click()
    memory_usage.append(("Click Compress Button", get_memory_usage(process)))

    # Step 8: Download the compressed PDF
    download_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "zon-download-cbtn0"))
    )
    download_button.click()
    time.sleep(10)  # Wait for download to start
    memory_usage.append(("Download PDF", get_memory_usage(process)))

finally:
    # Step 9: Finalize and close the browser
    driver.quit()
    memory_usage.append(("Finalize and Close Browser", get_memory_usage(process)))

# Output memory usage for each step
for step, memory in memory_usage:
    print(f"{step}: {memory:.2f} MB")

print(f"File downloaded to {download_dir}")
