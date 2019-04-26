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
    # set index
    idx = [0,1]

    # 1. KT_CZ_Analysis.card_by_upjong.csv
    if idx[0] == 1:
        print("KT_CZ_Analysis.card_by_upjong.csv processing: ")
        # readCSVfile
        card_by_upjong = pd.read_csv("KT_CZ_Analysis.card_by_upjong.csv")
        # removing upjong_code = 3002, which is not in other tables
        # card_by_upjong = card_by_upjong[card_by_upjong.upjong_code != 3002]
        #grouped by year,month,hd_cd,upjong_code
        group1= card_by_upjong.groupby([card_by_upjong.year, card_by_upjong.month, card_by_upjong.hd_cd, card_by_upjong.upjong_code])            

        # make dataframe as result
        result_1 = group1['revenue','customer_count','payment_count'].sum()  

      
        print("End of KT_CZ_Analysis.card_by_upjong.csv processing: ")
    
    if idx[1] == 1:    
        print("KT_CZ_Analysis.card_living_ingu.csv processing: ")
        # 2. KT_CZ_Analysis.card_living_ingu.csv
        card_living_ingu = pd.read_csv("KT_CZ_Analysis.card_living_ingu.csv")
        #grouped by year,month,hd_cd,upjong_code
        group1= card_living_ingu.groupby([card_living_ingu.year, card_living_ingu.month, card_living_ingu.hd_cd, card_living_ingu.sector_code]) 

        result_2 = group1['living_ingu','revenue','customer_count','payment_count'].sum()

        #end: writing CSV file    
        result_2.to_csv('result_2.csv', header = True)

        print("End of KT_CZ_Analysis.card_living_ingu.csv processing: ")


      #end: writing CSV file    
        #result_1.to_csv('result_1.csv', header = True)
    


    

