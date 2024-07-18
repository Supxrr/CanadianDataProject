# Group Project - Evan Bucholski 

This is a README file to inform the basics of what the program does and acomplishes and inform of how to run each section accordingly to get the expected outputs.


# Program 1 information


Program 1 is called preProcess.py and it will take the massive data set and process it down to most of the information we are looking for so that it is smaller and more concise information that program 2 can sort through. 

this program will take its information and output it to a file called processed.csv 

in order to run this program --> python3 preProcess.py fullData.csv

where "fullData.csv" should be named after the file of whatever data set you want processed.



# Program 2 information

Program 2 is called averageWageSort.py and it takes any province as an arguement value as well as the start date to search from then will search for specifically the Software Engineers and Designers job category and be able to find the not recruiting and constantly recruiting sections then compare the average offered hourly wage between them.

This program uses the processed data file that was created with program 1.

This program will write out this data to a csv file called output.csv which can then be opened and viewed to see the results of the inputted province.


to run this program --> python3 averageWageSort.py processed.csv "Ontario" "2021"

Then the Province can be varied to all the Provinces of Canada.
Then the date can be varied to whatever start date you want to search from.



# Program 3 information

Program 2 is called dataConverter.py and it takes the output.csv file that was created by the second program and uses that to create the graph of all the data in that file


to run this program --> python3 dataConverter.py output.csv

the "output.csv" is a command line arguement and should be replaced with whatever file name you chose.


# processed.csv

This file is the one created by preProcess.py and contains all the processed data.

# output.csv

This file is created by the averageWageSort.py stores all the information that was disected by the program. This file is then used by dataConverter.py to create the graph

# output.png

This png file has the png of the graph created by the dataConverter.py program.



# Note

I tried to last minute attempt to make the program work for if the user puts "Canada" as a parameter and although I did manage to get it to work using the data, the final graph when using Canada comes out a bit weird because the graph does not scale.

