# PIC
# https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/22951A66J6.jpg

# Aadhar Card
# https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_Aadhar.jpg

# Community and DOB Certificate
# https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_Caste.jpg

# Income Certificate
# https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_Income.jpg

# Inter Memo
# https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_MARKSMEMO.jpg

# SSC Memo
# https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_SSC.jpg

rollno = input("Enter Rollno: ").upper()
print(rollno)

document_url_format = 'https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/'

error_message = 'Document Unavailable'

get_profile_pic = document_url_format + f"{rollno}/{rollno}.jpg"

get_aadhar_card = document_url_format + f"{rollno}/DOCS/{rollno}_Aadhar.jpg"

get_dob_certificate = document_url_format + f"{rollno}/DOCS/{rollno}_Caste.jpg"

get_income_certificate = document_url_format + f"{rollno}/DOCS/{rollno}_Income.jpg"

get_ssc_memo = document_url_format + f"{rollno}/DOCS/{rollno}_SSC.jpg"

get_inter_memo = document_url_format + f"{rollno}//DOCS/{rollno}_MARKSMEMO.jpg"





