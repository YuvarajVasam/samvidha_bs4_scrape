from bs4 import BeautifulSoup
import re
 
 
def get_pat_indexes():

    with open('pat.html','r') as html_data:
        soup = BeautifulSoup(html_data, 'html.parser')

    tables_list = soup.find_all('table')
    attendance_table = tables_list[2]

    headers = [header for header in attendance_table.find_all('th')]

    indexes_dict = {}

    for index, header in enumerate(headers,start=0):
        indexes_dict[header.text] = index

    keys = ['Course Name','Conducted','Attended','Attendance %','Status']

    index_list = [indexes_dict.get(key) for key in keys] 
    index_tuple = tuple(index_list)

    return index_tuple


print(get_pat_indexes())


