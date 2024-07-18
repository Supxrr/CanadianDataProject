'''
averageWageSort.py
  Author(s): Evan Bucholski (1226299)
  Earlier contributors(s): Evan Bucholski (1226299)
  Project: Group Project 2024
  Date of Last Update: April 3rd, 2024

  Functional Summary:
    Takes in the big data file CSV and will process it in terms of the province, job, recruiting status, and statistic.


    This is iteration 3 of the script and is the final version.

    
'''

import sys
import csv


def main(argv):


    if len(argv) != 2:
        print("Usage: preProcess.py <filename>")
        sys.exit(1)


    input_filename = argv[1]
    provinces = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", 
                 "Newfoundland and Labrador", "Nova Scotia", "Ontario", 
                 "Prince Edward Island", "Quebec", "Saskatchewan", "Northwest Territories", 
                 "Nunavut", "Yukon"]
    look_for = "Software engineers and designers [2173]"
    job_chars = ["Constantly recruiting", "Not constantly recruiting"]
    stats = "Average offered hourly wage"
    output_filename = "processed.csv"

    try:
        #opening file 
        with open(input_filename, encoding="utf-8-sig") as statcan_fh, open(output_filename, 'w', newline='', encoding="utf-8") as output_fh:
            #assign variables for the reader and writer
            statcan_reader = csv.reader(statcan_fh)
            output_writer = csv.writer(output_fh)
            
            #writes the header to the output file.
            output_writer.writerow(["Date", "Province", "Job", "Recruiting Status", "Statistic", "Value"])

            #iterates through the rows in the reader
            for row in statcan_reader:
                if len(row) < 13:
                    continue
                
                #strips the whitespace from the cells in the row
                row = [cell.strip() for cell in row]

                #checks if the province is in the list of provinces, the job is the one we are looking for, the recruiting status is in the list of job characteristics, and the statistic is the one we are looking for
                if (row[1] in provinces and row[3] == look_for and row[4] in job_chars and row[5] == stats):
                    the_value = row[12] if row[12] else "0"

                    #writes the row to the output file if the value is not 0
                    if the_value != "0":
                        output_writer.writerow([row[0], row[1], row[3], row[4], row[5], the_value])

    except IOError as err:
        print(f"Unable to open file: {err}")
        sys.exit(1)

main(sys.argv)



