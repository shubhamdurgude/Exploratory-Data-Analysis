#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation 
# 
# # Data Science & Business Analytics Internship
# 
# ## Task 3: Exploratory Data Analysis (Retail)
# 
# ### By Shubham Durgude

# In[45]:


#Importing all libraries required
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[46]:


df=pd.read_csv('SampleSuperstore.csv')


# In[47]:


df.head()


# In[48]:


df.info()


# In[49]:


df.isnull().sum()


# In[50]:


df.shape


# In[51]:


df.nunique()


# ### Exploratory Data Analysis

# In[52]:


plt.figure(figsize=(8,5))
sns.kdeplot(df['Sales'],color='black',label='Sales',shade=True,bw=25)
sns.kdeplot(df['Profit'],color='g',label='Profit',shade=True,bw=25)
plt.xlim([-100,1000])
plt.legend()
plt.show()


# ### Analysis Using Pairplot for Each Column
# 
# ### 1)Based on Category

# In[73]:


sns.pairplot(df,hue='Category')
plt.show()


# ### 2)Based on Region 

# In[75]:


sns.pairplot(df,hue='Region',palette='Dark2')
plt.show()


# In[55]:


df.corr()


# ### Heatmap for Correlation

# In[56]:


sns.heatmap(df.corr(),cmap='rocket_r',annot=True)
plt.show()


# ### From above heatmap :
# 
# Sales and profit are moderately correlated.
# 
# Discount and Profit are negatively correlated.
# 
# Quantity and Profit are less moderately correlated.

# ### Countplot of each column

# ### Distribution of the data using plot

# In[72]:


fig , axs = plt.subplots(ncols=2,nrows=2,figsize=(10,10))
sns.distplot(df['Sales'],color='red',ax= axs[0][0])
sns.distplot(df['Profit'],color='green',ax=axs[0][1])
sns.distplot(df['Quantity'],color='orange',ax=axs[1][0])
sns.distplot(df['Discount'],color='blue',ax=axs[1][1])
axs[0][0].set_title('Sales Distribution',fontsize=20)
axs[0][1].set_title('Profit Distribution',fontsize=20)
axs[1][0].set_title('Quantity Distribution',fontsize=20)
axs[1][1].set_title('Discount Distribution',fontsize=20)
plt.show


# ### Statewise Deal Analysis

# In[76]:


df['Country'].value_counts()


# In[77]:


df1=df['State'].value_counts()
df1.head(10)


# In[82]:


df1.plot(kind='bar',figsize=(15,5),color='red')
plt.xlabel('States')
plt.ylabel('Frequency/Number of Deals')

plt.title('State wise dealings',fontsize=20)
plt.show()


# ### Here is top 3 states where deals are highest

# 1)California<br>
# 2)New York<br>
# 3)Texas<br>

# ### Wyoming : Lowest number of deal.

# In[83]:


df['State'].value_counts().mean()


# ### Average number of deal per state is 204.

# ### City wise analysis of dealing

# In[84]:


df2=df['City'].value_counts()
df2=df2.head(50)


# In[85]:


df2.plot(kind='bar',figsize=(15,5),color='blue')
plt.ylabel('Frequency/Number of deals')
plt.xlabel('City')

plt.title('City Wise Dealings',fontsize=20)
plt.show()


# ### Here is the top 3 cities where deals are highest

# 1)New York city<br>
# 2)Los Angeles<br>
# 3)Philadelphia

# In[87]:


df['City'].value_counts().mean()


# ### Average number of deal per city is 19.

# ### Segment wise analysis of Profit ,Discount and Sell

# In[88]:


df['Segment'].value_counts()


# In[89]:


df_segment=df.groupby(['Segment'])[['Sales','Discount','Profit']].mean()
df_segment


# In[91]:


#1. Sales 2.Discount 3.Profit
df_segment.plot.pie(subplots=True,
                   autopct='%1.1f%%',
                   figsize=(18,20),
                   startangle=90,
                   shadow=True,
                   labels=df_segment.index)
plt.title('Segment wise analysis of Sale,Discount,Profit')
plt.show()


# Sales:<br>
# 
# Consumer=32%<br>
# Corporate=33.5%<br>
# Home office=34.5%<br>
# 
# Discount:<br>
# 
# Consumer=15.8%<br>
# Corporate=15.8%<br>
# Home office=14.7%<br>
# 
# Profit:<br>
# 
# Consumer=28.7%<br>
# Corporate=33.8%<br>
# Home office=37.5%<br>

# ### State wise analysis of Profit, Discount and sell

# In[93]:


df['State'].value_counts().head(10)


# In[95]:


df_state=df.groupby(['State'])[['Sales','Discount','Profit']].mean()
df_state.head(10)


# ### Statewise profit analysis

# In[96]:


df_state1=df_state.sort_values('Profit')

df_state1[['Profit']].plot(kind='bar',figsize=(15,4),color='green')
plt.title('Statewise Profit Analysis',fontsize=20)
plt.ylabel('Profit per state')
plt.xlabel('States')
plt.show()


# ### Result
# 
# Vermont:Highest Profit<br>
# Ohio:Lowest Profit

# ### State wise Sale Analysis

# In[98]:


df_state['Sales'].plot(kind='pie',
                      figsize=(20,20),
                      autopct='%1.1f%%',
                       startangle=90,
                       shadow=True
                      )
plt.title('State wise analysis of Sale',fontsize=20)
plt.show()


# Highest amount of sales=Wyoming(11.8%)<br>
# Lowest amount of sales=South Dakota(0.8%)

# ### Statewise Discount Analysis

# In[100]:


df_state1['Discount'].plot(kind='bar',figsize=(18,5),color='purple')
plt.title('Statewise Discount Analysis',fontsize=20)
plt.show()


# ### Illinois at the top.

# ### Citywise Analysis Of The Profit

# In[102]:


df_city=df.groupby(['City'])[['Sales','Discount','Profit']].mean()
df_city=df_city.sort_values('Profit')
df_city.head()


# In[105]:


#1.Low Profit
df_city['Profit'].head(30).plot(kind='bar',figsize=(15,5),color='orange')
plt.title('City wise analysis of Sale,Profit,Discount')
plt.show()


# In[108]:


#2. High Profit
df_city['Profit'].tail(30).plot(kind='bar',figsize=(15,5),color='orange')
plt.title('City wise analysis of Sales,Profit, Discount')
plt.show()


# 30 Cities have profit in positive.<br>
# 30 Cities have profit in negative.<br>
# The balance is pretty good here!

# ### Quantity wise sales,profit and discount analysis

# In[110]:


df_quantity=df.groupby(['Quantity'])[['Sales','Profit','Discount']].mean()
df_quantity.head(10)


# In[111]:


#1. sales 2. Discount 3. Profit
df_quantity.plot.pie(subplots=True, 
                    autopct='%1.1f%%',
                    figsize=(20, 20),
                     pctdistance=0.69,
                    startangle=90,     # start angle 90° (Africa)
                    shadow=True,
                    labels = df_quantity.index)
plt.title('Quantity wise analysis of Sale, Discount, profit')
plt.show()


# 13 Number of quantity is high for sales and profit.

# ### CATEGORY WISE SALES,PROFIT AND DISCOUNT

# In[112]:


df_category=df.groupby(['Category'])[['Sales','Profit','Discount']].mean()
df_category


# In[114]:


df_category.plot.pie(subplots=True, 
                     figsize=(18, 20), 
                     autopct='%1.1f%%', 
                     labels = df_category.index)
plt.show()


# Maximum sales and profit is obtained in Technology.<br>
# Minimum profit obtained in future.

# ### Sub category wise analysis Of Sales,Profit and Discount

# In[116]:


df_sub_category = df.groupby(['Sub-Category'])[['Sales', 'Discount', 'Profit']].mean()
df_sub_category.head(10)


# ### Based On Sales

# In[118]:


plt.figure(figsize=(15,15))
plt.pie(df_sub_category['Sales'],labels=df_sub_category.index,autopct='%1.1f%%')
plt.title('Sub-Category wise analysis,fontsize=20')
plt.legend()
plt.xticks(rotation=90)
plt.show()


# Copier has the highest sales.<br>
# Fasteners has the lowest sales.
# 

# ### Based On The Discount
# 

# In[120]:


plt.figure(figsize=(15,15))
plt.pie(df_sub_category['Discount'],labels=df_sub_category.index,autopct='%1.1f%%')
plt.title('Sub-Category wise analysis,fontsize=20')
plt.legend()
plt.xticks(rotation=90)
plt.show()


# Binders have high discount.

# ### Based on the profit

# In[124]:


df_sub_category.sort_values('Profit')[['Sales','Profit']].plot(kind='bar',
                                                              figsize= (10,5),
                                                              label=['Avg Sales Price($)','Profit($)'])
plt.show()


# ### COPIER : HIGHEST PROFIT AS WELL AS SELL

# In[126]:


df_region=df.groupby(['Region'])[['Sales','Profit','Discount']].mean()
df_region


# ### REGION WISE ANALYSIS

# In[128]:


df_region=df.groupby(['Region'])[['Sales','Profit','Discount']].mean()
df_region


# In[131]:


df_region.plot.pie(subplots=True,
                  figsize=(18,20),
                  autopct='%1.1f%%',
                  labels=df_region.index)
plt.show()


# Profit is high in WEST.<BR>
# Sales is high in SOUTH.<BR>
# Discount is high in Central part.

# ### SHIP MODE WISE ANALYSIS

# In[133]:


df['Ship Mode'].value_counts()


# In[135]:


df_shipmode=df.groupby(['Ship Mode'])[['Sales','Profit','Discount']].mean()
df_shipmode


# In[137]:


df_shipmode.plot.pie(subplots=True,
                     figsize=(18, 20), 
                     autopct='%1.1f%%', 
                     labels = df_shipmode.index)
plt.show()


# Profit and discount is high in first class.<br>
# Sales is high for same day ship.

# ### RESULT
# 
# 1. Profit is more than that of sale but there are some areas where profit can be increased.<br>
# 2.Profit and Discount is high in first class.<br>
# 3.Sales is high for same day ship.<br>
# 4.Sub Category:Copier:High profit and sales<br>
# 5.Sub Category:Binder,Machines and then tables have high discount.<br>
# 6.Category:Maximum sales and Profit obtain in Technology<br>
# 7.Category:Minimum Profit obtain in furniture.<br>
# 8.State:Vermont : Highest Profit<br>
# 9.State:Ohio:Lowest Profit<br>
# 10.Segment:Home office:High profit and sales<br>
# 

# The top 3 cities where deals are highest are<br>
# 1.New York City<br>
# 2.Los Angeles<br>
# 3.Philadelphia<br>
#                   

# Sales and Profit are moderately correlated.<br>
# <br>
# 
# The top 3 states where deals are highest are<br>
# 1.California<br>
# 2.New York City<br>
# 3.Texas<br>
# <br>
# 
# Wyoming : Lowest number of deal,Highest amount of Sales(11.8%)<br>
# Lowest amount Of Sales=South Dakota(0.8%)
# 
# 

# ### CONCLUSION

# THE WEAK AREAS WHERE ONE CAN WORK TO MAKE PROFIT ARE:<BR>
#     1.We should limit the sales of furniture and increase that of technology and office suppliers as furniture has very less profit.<br>
#     2.Considering the sub categories sales of tables should be minimized.<br>
#     3.Increase the sales more in the east as profit is second highest.<br>
#     4.We should concentrate on the states like 'New York' and 'California' to make profit.
