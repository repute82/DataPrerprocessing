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
    # 1. read csv:  card_by_upjong = pd.read_csv("KT_CZ_Analysis.card_by_upjong.csv")
    # 1-1. when reading csv holding Korean: spop = pd.read_csv("KT_CZ_Analysis.sejong_spop.csv", encoding='CP949') (in windows)

    # 2. create new column
    # 2-1. by splitting the exisiting columns: nowork['year'] = nowork['etl_ymd'].astype(str).str[:4]
    # 2-2. by concatenating the existing columns: nowork['sido+sgg'] = nowork['sido_code'].astype(str) + nowork['sgg_code'].astype(str)
    
    # 3. removing NAN rows : nowork.dropna(how='any') ( meaning removing all rows holding any NAN in their columns)
    # 3-1. removing columns: del nowork['elt_ymd']

    # 4. groupby
    # 4-1. grouping by some columns: nowork_group = nowork.groupby(['year','month','sido+sgg'])
    # 4-2. sum, mean of groups: nowork_group['cnt'].sum()

    # 5. writing result: nowork_group['cnt'].sum().to_csv("nowork_result.csv", header=True)

    # 6. merging dataframes : pd.merge(df1, df2, on="id")

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
    


    

