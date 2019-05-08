#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[20]:


df.columns


# In[21]:


df = pd.read_csv('card_living_ingu_result.csv')
df.rename(columns={'hd_cd':'h_dng_cd'}, inplace=True)
df.columns


# In[5]:


df_6 = pd.read_csv('living_population_result.csv')
df_7 = pd.read_csv('revenue_by_hangjeong_result.csv')
df_9 = pd.read_csv('sangju_ingu_micro_result.csv')
df_12 = pd.read_csv('spop_result.csv')


# In[13]:


df_6.columns


# In[25]:


merged = pd.merge(df,df_6,on=['year','month','h_dng_cd'])
merged


# In[35]:


df[(df['year'] == 2017) & (df['month'] == 1) & (df['h_dng_cd'] == 36110250)]


# In[37]:


merged[(merged['year'] == 2017) & (merged['month'] == 1) & (merged['h_dng_cd'] == 36110250)]


# In[42]:


df_12.rename(columns={'admdong_cd':'h_dng_cd'}, inplace =True)


print(df_7.columns)
print(df_9.columns)
print(df_12.columns)


# In[43]:


df_7


# In[45]:


merged.rename(columns={'population':'saengwhal_population'}, inplace =True)
merged


# In[46]:


merged_2 = pd.merge(merged,df_7,on=['year','month','h_dng_cd'])
merged_2


# In[48]:


merged_2.drop(columns='living_sector_revenue',inplace=True)
merged_2.info()


# In[49]:


merged_2.columns


# In[56]:


merged_2.to_csv('ymhu_result.csv')


# In[55]:


g = merged_2.groupby(['year','month','h_dng_cd'])
g['saengwhal_population'].sum()


# In[75]:


h_cd_name = pd.read_csv('d_cd_name.csv', encoding = 'euc-kr', header =None) 
h_cd_name.set_index(1, inplace = True)
h_cd_name.info()


# In[74]:


u_cd_name = pd.read_excel('u_cd_name.xlsx', encoding = 'euc-kr', header =None)
u_cd_name.set_index(1, inplace = True)
u_cd_name


# In[80]:


upjong_code = pd.read_csv('upjong_code.csv', encoding = 'euc-kr')
upjong_code.set_index('업종코드', inplace=True)
upjong_code


# In[85]:


d_dict = h_cd_name.to_dict('index')
d_dict


# In[86]:


u_dict=upjong_code.to_dict('index')


# In[102]:


h_cd_name.loc[36110550]


# In[99]:


u_dict.get(1199).get('대분류')


# In[103]:


def converHCodeToName(x):
    return h_cd_name.loc[x]    


# In[121]:


merged_2['h_dng_cd']


# In[134]:





# In[135]:


names = []
for i in merged_2['h_dng_cd']:
    names.append(converHCodeToName(i)[0])

    


# In[141]:


upjong_code.loc[1001]['대분류']


# In[142]:


upjongs = []
for i in merged_2['sector_code']:
    upjongs.append(upjong_code.loc[int(i)]['대분류'])
upjongs
print(len(upjongs))


# In[143]:


upjongs


# In[136]:


print(len(names))


# In[144]:


merged_2['upjong_name'] = upjongs


# In[137]:


merged_2['dong_name'] = names


# In[147]:


merged_2.to_csv('ymdu_result_190508.csv', encoding='euc=kr')


# In[94]:



h_cd_name.info()


# In[ ]:




