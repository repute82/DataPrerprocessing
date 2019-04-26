import pandas as pd
import numpy as np
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
    # 1. KT_CZ_Analysis.card_by_upjong.csv
    # readCSVfile
    card_by_upjong = pd.read_csv("KT_CZ_Analysis.card_by_upjong.csv")
    # removing upjong_code = 3002, which is not in other tables
    card_by_upjong = card_by_upjong[card_by_upjong.upjong_code != 3002]
    group1= card_by_upjong.groupby([card_by_upjong.year, card_by_upjong.month, card_by_upjong.hd_cd, card_by_upjong.upjong_code])            

    # make dataframe as result
    result = group1['revenue','customer_count','payment_count'].sum()  

    #end: writing CSV file    
    result.to_csv('result.csv', index=True,header = True)

    # 2. KT_CZ_Analysis.card_by_upjong.csv
    


    

