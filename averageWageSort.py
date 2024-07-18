'''
averageWageSort.py
  Author(s): Evan Bucholski (1226299)
  Earlier contributors(s): Evan Bucholski (1226299)
  Project: Group Project 2024
  Date of Last Update: April 3rd, 2024

  Functional Summary:
    Takes a CSV file and extracts the average offered hourly wage for software engineers and designers in a given province and start date.


    This is iteration 3 of the script and is the final version.

    
'''
import sys
import csv

def main(argv):
    if len(argv) != 4:
        print("Usage: averageWageSort.py <filename> <name of province or 'Canada'> <start year>")
        sys.exit(1)

    #extract the command line arguments
    input_filename = argv[1]
    province_input = argv[2].strip()
    start_year = argv[3].strip()
    look_for = "Software engineers and designers [2173]".strip()
    job_chars = ["Constantly recruiting", "Not constantly recruiting"]
    stats = "Average offered hourly wage".strip()
    output_filename = "output.csv"

    #list of Canadian provinces to match if user puts in Canada
    canadian_provinces = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
                          "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"]

    try:
        with open(input_filename, encoding="utf-8-sig") as statcan_fh, open(output_filename, 'w', newline='', encoding="utf-8") as output_fh:
            statcan_reader = csv.reader(statcan_fh)
            output_writer = csv.writer(output_fh)

            #write the header to the output file
            output_writer.writerow(["Date", "Province", "Job", "Recruiting Status", "Statistic", "Value"])

            #iterate through the rows in the reader
            for row in statcan_reader:
                if len(row) < 6:
                    continue


                #strip the whitespace from the cells in the row
                date, row_province, job, recruiting_status, statistic, value = row
                date_year = date.split("-")[0]

                #check if the province is in the list of provinces, the job is the one we are looking for, the recruiting status is in the list of job characteristics, and the statistic is the one we are looking for
                province_match = (province_input == "Canada" and row_province in canadian_provinces) or (row_province == province_input)

                if (province_match and job == look_for and recruiting_status in job_chars and 
                    statistic == stats and int(date_year) >= int(start_year)):
                    output_writer.writerow([date, row_province, job, recruiting_status, statistic, value])

    except IOError as err:
        print(f"Unable to open file: {err}", file=sys.stderr)
        sys.exit(1)


main(sys.argv)


