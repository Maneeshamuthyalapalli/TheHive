from datetime import datetime 
input_line = input().strip()
date1_str, date2_str = input_line.split()
date_format = "%Y-%m-%d"
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)
difference = abs((date1 - date2).days)
print(difference)
