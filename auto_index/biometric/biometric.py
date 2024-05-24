from bs4 import BeautifulSoup
import re 

html_content = """

<table class="table table-striped table-bordered table-hover table-sm">
		<thead>
			<tr class="text-center">
				<th rowspan="2">S.No</th>		
				<th rowspan="2">Rollno</th>			
				<th rowspan="2">Name</th>
				<th rowspan="2">Date</th>
								<th colspan="3">JNTUH - AEBAS</th>
				<th rowspan="2">Class Attendance<br>(out of 7 periods)</th>
				
			</tr>
			<tr class="text-center">
								<th>In Time</th>
				<th>Out Time</th>
				<th>Status</th>
			</tr>
		</thead> 
		<tbody>
						<tr>
					<td style="width:50px;">1</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">11-May-2024</td>
										<td style="text-align:center;">08:56</td>
					<td style="text-align:center;">15:52</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">2</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">10-May-2024</td>
										<td style="text-align:center;">09:24</td>
					<td style="text-align:center;">16:25</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">3</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">09-May-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">4</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">08-May-2024</td>
										<td style="text-align:center;">09:10</td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">5</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">07-May-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">6</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">06-May-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">7</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">04-May-2024</td>
										<td style="text-align:center;">09:28</td>
					<td style="text-align:center;">15:15</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">8</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">03-May-2024</td>
										<td style="text-align:center;">09:22</td>
					<td style="text-align:center;">15:53</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">9</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">02-May-2024</td>
										<td style="text-align:center;">09:35</td>
					<td style="text-align:center;">15:00</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">10</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">01-May-2024</td>
										<td style="text-align:center;">10:53</td>
					<td style="text-align:center;">15:25</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">11</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">30-Apr-2024</td>
										<td style="text-align:center;">09:34</td>
					<td style="text-align:center;">16:02</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">12</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">29-Apr-2024</td>
										<td style="text-align:center;">09:24</td>
					<td style="text-align:center;">16:00</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">13</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">27-Apr-2024</td>
										<td style="text-align:center;">09:50</td>
					<td style="text-align:center;">15:13</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">14</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">26-Apr-2024</td>
										<td style="text-align:center;">10:58</td>
					<td style="text-align:center;">15:02</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">15</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">25-Apr-2024</td>
										<td style="text-align:center;">10:40</td>
					<td style="text-align:center;">16:34</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">16</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">24-Apr-2024</td>
										<td style="text-align:center;">10:41</td>
					<td style="text-align:center;">15:19</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">17</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">23-Apr-2024</td>
										<td style="text-align:center;">09:36</td>
					<td style="text-align:center;">15:12</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">18</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">22-Apr-2024</td>
										<td style="text-align:center;">09:52</td>
					<td style="text-align:center;">15:18</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">19</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">18-Apr-2024</td>
										<td style="text-align:center;">09:49</td>
					<td style="text-align:center;">15:07</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">20</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">16-Apr-2024</td>
										<td style="text-align:center;">10:43</td>
					<td style="text-align:center;">16:06</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">21</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">15-Apr-2024</td>
										<td style="text-align:center;">09:53</td>
					<td style="text-align:center;">15:53</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">22</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">13-Apr-2024</td>
										<td style="text-align:center;">10:12</td>
					<td style="text-align:center;">15:03</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">23</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">10-Apr-2024</td>
										<td style="text-align:center;">09:46</td>
					<td style="text-align:center;">15:01</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">24</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">08-Apr-2024</td>
										<td style="text-align:center;">09:31</td>
					<td style="text-align:center;">15:03</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">25</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">06-Apr-2024</td>
										<td style="text-align:center;">09:32</td>
					<td style="text-align:center;">15:19</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">26</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">04-Apr-2024</td>
										<td style="text-align:center;">09:53</td>
					<td style="text-align:center;">15:01</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">27</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">03-Apr-2024</td>
										<td style="text-align:center;">10:31</td>
					<td style="text-align:center;">15:33</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">28</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">02-Apr-2024</td>
										<td style="text-align:center;">10:27</td>
					<td style="text-align:center;">15:09</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">29</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">01-Apr-2024</td>
										<td style="text-align:center;">09:37</td>
					<td style="text-align:center;">16:13</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">30</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">30-Mar-2024</td>
										<td style="text-align:center;">09:40</td>
					<td style="text-align:center;">15:26</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">31</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">28-Mar-2024</td>
										<td style="text-align:center;">09:25</td>
					<td style="text-align:center;">15:44</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">32</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">27-Mar-2024</td>
										<td style="text-align:center;">09:47</td>
					<td style="text-align:center;">15:57</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">33</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">26-Mar-2024</td>
										<td style="text-align:center;">09:29</td>
					<td style="text-align:center;">15:53</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">34</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">23-Mar-2024</td>
										<td style="text-align:center;">09:34</td>
					<td style="text-align:center;">15:23</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">35</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">22-Mar-2024</td>
										<td style="text-align:center;">09:27</td>
					<td style="text-align:center;">15:04</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">36</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">21-Mar-2024</td>
										<td style="text-align:center;">09:36</td>
					<td style="text-align:center;">15:59</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">37</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">20-Mar-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">38</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">19-Mar-2024</td>
										<td style="text-align:center;">09:42</td>
					<td style="text-align:center;">15:01</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">39</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">18-Mar-2024</td>
										<td style="text-align:center;">09:51</td>
					<td style="text-align:center;">15:06</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">40</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">16-Mar-2024</td>
										<td style="text-align:center;">09:43</td>
					<td style="text-align:center;">16:03</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">41</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">15-Mar-2024</td>
										<td style="text-align:center;">09:50</td>
					<td style="text-align:center;">16:02</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">42</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">14-Mar-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">43</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">13-Mar-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">44</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">12-Mar-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">45</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">11-Mar-2024</td>
										<td style="text-align:center;"></td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">46</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">09-Mar-2024</td>
										<td style="text-align:center;">09:37</td>
					<td style="text-align:center;">15:14</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">47</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">07-Mar-2024</td>
										<td style="text-align:center;">10:45</td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;">Absent</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">48</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">06-Mar-2024</td>
										<td style="text-align:center;">09:50</td>
					<td style="text-align:center;">16:07</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">49</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">05-Mar-2024</td>
										<td style="text-align:center;">10:27</td>
					<td style="text-align:center;">15:18</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">50</td>
					<td style="text-align:center;">22951A66J6</td>
					<td>VASAM YUVARAJ</td>
					<td style="text-align:center;">04-Mar-2024</td>
										<td style="text-align:center;">09:46</td>
					<td style="text-align:center;">15:12</td>
					<td style="text-align:center;">Present</td>
					<td></td>
				</tr>
						<tr>
					<td style="width:50px;">51</td>
					<td style="text-align:center;"></td>
					<td></td>
					<td style="text-align:center;">20-May-2024</td>
										<td style="text-align:center;">-</td>
					<td style="text-align:center;">-</td>
					<td style="text-align:center;"></td>
					<td></td>
				</tr>
				</tbody>
	</table>
"""



soup = BeautifulSoup(html_content,'html.parser')

table = soup.table.tbody.find_all('tr')

new_table = table[2:-2]
table_content = "".join(str(row) for row in new_table)

present_days = len(re.findall('Present',table_content))
absent_days = len(re.findall('Absent',table_content))
total_days = 0



first_and_last_two_rows = table[0:2] + table[-2:]

html_content_2 = "".join(str(row) for row in first_and_last_two_rows)

rows = BeautifulSoup(html_content_2,'html.parser')

# Find all th elements excluding "JNTUH - AEBAS"
headers = [header for header in soup.find_all('th') if header.text.strip() != "JNTUH - AEBAS"]

# Function to find the index of a given header name
def find_header_index(header_name):
    for index, header in enumerate(headers,start=-1):
        if re.search(header_name, header.text, re.IGNORECASE):
            return index
    return None


index_in_time = find_header_index("In Time")
index_out_time = find_header_index("Out Time")
index_status = find_header_index("Status")

print(index_in_time,index_out_time,index_status)

for row in rows:
    cells = row.find_all('td')
    intime = cells[index_in_time].text
    outtime = cells[index_out_time].text
    status = cells[index_status].text
    # print(intime,outtime,status)
    
    if (intime != "" and outtime != "") and status == "Present":
        present_days += 1

    elif (intime != "" and outtime == ("" or '-')) and status == "Absent":
          absent_days += 1 

    elif (intime == ("" or '-') and outtime != "" ) and status == "Absent":
          absent_days += 1 

    elif (intime == ("" or '-') and outtime == ("" or '-')) and status == "":
        pass
    else:
        pass
    

total_days = absent_days + present_days

print(present_days,absent_days,total_days)
