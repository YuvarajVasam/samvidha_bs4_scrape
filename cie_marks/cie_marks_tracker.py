from bs4 import BeautifulSoup

def cie_marks_tracker():
    try:
        # Open and parse the HTML file
        with open('cie_marks.html', 'r') as html_content:
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find all tables 
            tables = soup.find_all('table')

            # Select the latest semester table 
            cie_table = tables[1].find_all('tr')

            # Initialize a list to store the relevant data
            subject_marks_data = []

            # Iterate over each row in the selected semester table
            for row in cie_table:
                cells = row.find_all('td')
                row_data = [cell.get_text(strip=True) for cell in cells]

                # Break if 'Laboratory Marks (Practical)' is found -> to get only subject marks
                if 'Laboratory Marks (Practical)' in row_data:
                    break

                # Append row data if it's not empty -> to get only subject marks
                if row_data:
                    subject_marks_data.append(row_data)



        # Initialize dictionaries and total mark variables
        cie1_marks_dict = {}
        cie2_marks_dict = {}
        total_cie1_marks = 0
        total_cie2_marks = 0

        # Process each row data
        for marks_row in subject_marks_data:
            subject_name = marks_row[2]
            cie1_marks = marks_row[3]
            cie2_marks = marks_row[5]

            cie1_marks_dict[subject_name] = cie1_marks
            cie2_marks_dict[subject_name] = cie2_marks
            excluded_marks = ['-', '0', '0.0'] 

            if cie1_marks not in excluded_marks:
                total_cie1_marks += float(cie1_marks)

            if cie2_marks not in excluded_marks:
                total_cie2_marks += float(cie2_marks)

        
        
        total_cie_marks = total_cie1_marks + total_cie2_marks

        # print(f"Total CIE 1 Marks: {total_cie1_marks}")
        # print(f"Total CIE 2 Marks: {total_cie2_marks}")
        # print(f"Total CIE Marks: {total_cie_marks}")

        return total_cie_marks
    except FileNotFoundError:
        print("The file 'cie_marks.html' was not found. Please ensure the file exists in the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")    

print(cie_marks_tracker())