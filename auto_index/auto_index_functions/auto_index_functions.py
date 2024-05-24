from bs4 import BeautifulSoup
import re
 

def get_attendence_indexes():

    """
    Extracts the indices of specific headers from the attendance HTML table.
    Raises a KeyError if any specified header is not found.

    Returns:
        tuple: A tuple containing the indices of 'Course Name', 'Conducted',
               'Attended', 'Attendance %', 'Status'.
    """

    with open('attendence.html','r') as html_data:

        soup = BeautifulSoup(html_data, 'html.parser')

    table = soup.thead.tr

    headers = [header for header in table.find_all('th')]

    indexes_dict = {}
    
    for index, header in enumerate(headers,start=0):
        indexes_dict[header.text] = index
    
    keys = ['Course Name','Conducted','Attended','Attendance %','Status']

    # index_list = [indexes_dict.get(key) for key in keys] 

    # Gets the indexes of specified keys, raise KeyError if any key not found 
    index_list = []
    for key in keys:
        if key not in indexes_dict:
            raise KeyError(f"Header {key} not found in the table.")
        
        index_list.append(indexes_dict.get(key))
        

    index_tuple = tuple(index_list)

    return index_tuple



def get_pat_indexes():

    """
    Extracts the indices of specific headers from the PAT HTML table.
    Raises a KeyError if any specified header is not found.

    Returns:
        tuple: A tuple containing the indices of 'Course Name', 'Conducted',
               'Attended', 'Attendance %', 'Status'.
    """


    with open('pat.html','r') as html_data:
        soup = BeautifulSoup(html_data, 'html.parser')

    tables_list = soup.find_all('table')
    attendance_table = tables_list[2]

    headers = [header for header in attendance_table.find_all('th')]

    indexes_dict = {}

    for index, header in enumerate(headers,start=0):
        indexes_dict[header.text] = index

    keys = ['Course Name','Conducted','Attended','Attendance %','Status']

    # index_list = [indexes_dict.get(key) for key in keys] 

    # Gets the indexes of specified keys, raise KeyError if any key not found 
    index_list = []
    for key in keys:
        if key not in indexes_dict:
            raise KeyError(f"Header {key} not found in the table.")
        
        index_list.append(indexes_dict.get(key))

    index_tuple = tuple(index_list)

    return index_tuple



def get_biometric_indexes():

    """
    Extracts the indices of specific headers from the biometric HTML table.
    Excludes the 'JNTUH - AEBAS' header.
    Raises a KeyError if any specified header is not found.

    Returns:
        tuple: A tuple containing the indices of 'In Time', 'Out Time', 'Status'.
    """

    with open('biometric.html','r') as html_data:
    # Parse HTML data
        soup = BeautifulSoup(html_data, 'html.parser')

    # Find all th elements excluding "JNTUH - AEBAS"
    headers = [header for header in soup.find_all('th') if header.text.strip() != "JNTUH - AEBAS"]

    indexes_dict = {}

    
    for index, header in enumerate(headers,start=-1):
        indexes_dict[header.text] = index

    keys = ['In Time','Out Time','Status']

    # index_list = [indexes_dict.get(key) for key in keys] 

    # Gets the indexes of specified keys, raise KeyError if any key not found 
    index_list = []
    for key in keys:
        if key not in indexes_dict:
            raise KeyError(f"Header {key} not found in the table.")
        
        index_list.append(indexes_dict.get(key))

    index_tuple = tuple(index_list)

    return index_tuple




# Call the functions and print the results, handling KeyErrors\


try:
    print(get_attendence_indexes())

except KeyError as e:
    print(e)



try:
    print(get_pat_indexes())

except KeyError as e:
    print(e)


try:
    print(get_biometric_indexes())

except KeyError as e:
    print(e)
