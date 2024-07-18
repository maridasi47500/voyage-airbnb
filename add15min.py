from datetime import datetime
from datetime import timedelta
# Given timestamp in string
time_str = '23/2/2020 11:12:22.234513'
date_format_str = '%d/%m/%Y %H:%M:%S.%f'
# create datetime object from timestamp string
given_time = datetime.strptime(time_str, date_format_str)
print('Given timestamp: ', given_time)
n = 15
# Add 15 minutes to datetime object
final_time = given_time + timedelta(minutes=n)
print('Final Time (15 minutes after given time ): ', final_time)
# Convert datetime object to string in specific format 
final_time_str = final_time.strftime('%d/%m/%Y %H:%M:%S.%f')
print('Final Time as string object: ', final_time_str)
