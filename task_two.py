"""
TASK 2:
Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.
The output should be in following format.
{
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}
task_two.py
"""

from datetime import datetime
from pprint import pprint
from my_utils.csv_operations import CsvFile


def actual():
    content = CsvFile.read_entire_csv()
    final_dict = {}
    for i in content:

        if 30 < int(i["DEPARTMENT_ID"]) < 110 and int(i["SALARY"]) > 4200:
            bar = i["HIRE_DATE"]

            date = datetime.strptime(bar, "%d-%b-%y")
            get_date = date.strftime("%Y-%m-%d")
            final_dict.setdefault(get_date, []).append(i["FIRST_NAME"] + " " + i["LAST_NAME"])
    return final_dict


if __name__ == "__main__":
    pprint(actual())
