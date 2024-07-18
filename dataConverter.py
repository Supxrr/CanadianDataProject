'''
dataConverter.py
  Author(s): Evan Bucholski (1226299)
  Earlier contributors(s): Evan Bucholski (1226299)
  Project: Group Project 2024
  Date of Last Update: April 3rd, 2024

  Functional Summary:
    
  this script takes in the output.csv file from the averageWageSort.py script and plots the data in a line graph.
  The data is filtered by 'Constantly recruiting' and 'Not constantly recruiting' and plotted on the same graph.
  The graph is then saved to a png file and displayed to the user.

  This is the final iteration of the script

'''

import pandas as pd
import matplotlib.pyplot as plt
from sys import argv


#load data from output.csv, skip the first row, and name columns for the data.
#this allows for arguemnts to be passed in the command line to specify the file to be read.
data_filename = argv[1]
data = pd.read_csv(data_filename, skiprows=1, header=None, names=['Date', 'Province', 'Job', 'Recruiting Status', 'Statistic', 'Value'])


#convert the 'Date' column to datetime type and sort by it.
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(by='Date', inplace=True)


#filter the data for 'Constantly recruiting' and 'Not constantly recruiting'.
constantly_recruiting = data[data['Recruiting Status'] == 'Constantly recruiting']
not_constantly_recruiting = data[data['Recruiting Status'] == 'Not constantly recruiting']


#plot the data.
plt.figure(figsize=(10, 6))
plt.plot(constantly_recruiting['Date'], constantly_recruiting['Value'], label='Constantly Recruiting', marker='o')
plt.plot(not_constantly_recruiting['Date'], not_constantly_recruiting['Value'], label='Not Constantly Recruiting', marker='x')


plt.title('Average Offered Hourly Wage for Software Engineers and Designers')
plt.xlabel('Date')
plt.ylabel('Average Offered Hourly Wage ($)')
plt.xticks(rotation=45)
plt.legend()


plt.tight_layout()


#save the plot to a png file that can be viewed and saved as needed.
plt.savefig('output.png')


plt.show()





