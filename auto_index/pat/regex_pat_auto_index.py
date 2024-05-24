from bs4 import BeautifulSoup
import re

with open('pat.html','r') as html_data:
    # Parse HTML data
    soup = BeautifulSoup(html_data, 'html.parser')

tables_list = soup.find_all('table')
attendance_table = tables_list[2]
# print(attendance_table)

headers = [header for header in attendance_table.find_all('th')]

# Function to find the index of a given header name
def find_header_index(header_name):
    for index, header in enumerate(headers,start=0):
        if re.search(header_name, header.text, re.IGNORECASE):
            return index
    return None


index_course_name = find_header_index("Course Name")
index_conducted = find_header_index("Conducted")
index_attended = find_header_index("Attended")
index_attendance_percentage = find_header_index("Attendance %")
index_status = find_header_index("Status")


print("Index of 'Course Name':", index_course_name)
print("Index of 'Conducted':", index_conducted)
print("Index of 'Attended':", index_attended)
print("Index of 'Attendence Percentage':", index_attendance_percentage)
print("Index of 'Status':", index_status)



