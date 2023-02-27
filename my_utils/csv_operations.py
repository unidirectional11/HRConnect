import csv
from pprint import pprint


class CsvFile:
    filename = "C:\\Users\\User\\PycharmProjects\\HRConnect\\employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            result = csv.DictReader(foo)
            data = []
            for item in result:
                data.append(item)
            return data

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()


def main():
    f = CsvFile()
    pprint(f.read_entire_csv())
    pprint(f.read_csv_line_by_line())


if __name__ == "__main__":
    main()
