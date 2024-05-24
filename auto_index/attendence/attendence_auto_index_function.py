from bs4 import BeautifulSoup
import re
 

def get_attendence_indexes():
    with open('attendence.html','r') as html_data:

        soup = BeautifulSoup(html_data, 'html.parser')

    table = soup.thead.tr

    headers = [header for header in table.find_all('th')]

    indexes_dict = {}
    
    for index, header in enumerate(headers,start=0):
        indexes_dict[header.text] = index
    
    keys = ['Course Name','Conducted','Attended','Attendance %','Status']

    index_list = [indexes_dict.get(key) for key in keys] 
    index_tuple = tuple(index_list)

    return index_tuple


print(get_attendence_indexes())


