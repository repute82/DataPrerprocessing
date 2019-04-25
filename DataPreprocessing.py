import csv

def readCSVfile(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:            
            print(f'Column names are {", ".join(row)}')
            line_count += 1 
        print(f'Processed {line_count} lines.')


if __name__ == "__main__": 
    readCSVfile("KT_CZ_Analysis.card_by_upjong.csv")
