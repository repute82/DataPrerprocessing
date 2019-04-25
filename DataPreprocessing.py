import pandas as pd
# import csv

# def readCSVfile(filename):
#     with open(filename) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:            
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1 
#         print(f'Processed {line_count} lines.')



if __name__ == "__main__": 
    # readCSVfile("KT_CZ_Analysis.card_by_upjong.csv")
    df = pd.read_csv("KT_CZ_Analysis.card_by_upjong.csv", skiprows=[0], names=['일련번호','행정동 코드', '년', '월', '업종코드', '결제금액', '결제고객', '결제건수', '대분류', '생활업종별'])
    print(type(df))
    df.groupby(['행정동 코드'], as_index=False).mean()
    print(df.describe())

