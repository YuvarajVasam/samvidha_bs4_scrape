from bs4 import BeautifulSoup
import re
 

def get_biometric_indexes():

    with open('biometric.html','r') as html_data:
    # Parse HTML data
        soup = BeautifulSoup(html_data, 'html.parser')

    # Find all th elements excluding "JNTUH - AEBAS"
    headers = [header for header in soup.find_all('th') if header.text.strip() != "JNTUH - AEBAS"]

    indexes_dict = {}

    
    for index, header in enumerate(headers,start=-1):
        indexes_dict[header.text] = index

    keys = ['In Time','Out Time','Status']

    index_list = [indexes_dict.get(key) for key in keys] 
    index_tuple = tuple(index_list)

    return index_tuple


print(get_biometric_indexes())


