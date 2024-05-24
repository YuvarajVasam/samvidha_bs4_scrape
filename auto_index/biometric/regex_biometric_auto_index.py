from bs4 import BeautifulSoup
import re

with open('/Users/yuvarajvasam/Developer/Web/bs4/auto_index/biometric/biometric.html','r') as html_data:
    # Parse HTML data
    soup = BeautifulSoup(html_data, 'html.parser')

# Find all th elements excluding "JNTUH - AEBAS"
headers = [header for header in soup.find_all('th') if header.text.strip() != "JNTUH - AEBAS"]

# Function to find the index of a given header name
def find_header_index(header_name):
    for index, header in enumerate(headers,start=-1):
        if re.search(header_name, header.text, re.IGNORECASE):
            return index
    return None

# Example usage
index_in_time = find_header_index("In Time")
index_out_time = find_header_index("Out Time")
index_status = find_header_index("Status")

print("Index of 'In Time':", index_in_time)
print("Index of 'Out Time':", index_out_time)
print("Index of 'Status':", index_status)



