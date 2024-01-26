#!/usr/bin/env python
# coding: utf-8

# In[1]:


Objective:
    - Improve Customer Experience by analyzing sales data.
    - Increase Revenue


# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inlinehttp://localhost:8889/notebooks/PROJECT%20DIWALI%20SALES%20DATA.ipynb#')
import seaborn as sns


# In[7]:


df=pd.read_csv(r'C:\Users\Aashish\Downloads\Diwali Sales Data.csv',encoding='unicode_escape') 


# In[8]:


df.shape  # shows total rows & columns


# In[9]:


df.head() #show top 5 rows but if you want to show desire rows you and type number like(10).


# # Data Cleaning

# In[11]:


df.info()


# In[13]:


#drop unrelated/blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)  #inplace is use to save the command that you have performed.


# In[14]:


df.info()


# In[15]:


#Check for null values
pd.isnull(df).sum()


# In[16]:


df.shape #to check no of rows and columns are there befor deleting the null values.


# In[17]:


# drop null values
df.dropna(inplace=True)


# In[18]:


df.shape # to check after deleted null values how many rows & columns are there.


# In[19]:


#change data type
df['Amount']=df['Amount'].astype('int')


# In[20]:


df['Amount'].dtypes #to check 'Amount' data type has been changed or not .


# In[21]:


df.columns


# In[22]:


#rename column
df.rename(columns={'Zone':'Region'}) # just to get knowledge, if you need to change name of a particular Column.


# In[23]:


#describe()
df.describe()   # describe() used to find values (count,mean,std,min,max)


# In[24]:


#use descibe() for specific column
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[27]:


ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen)


# # on above graph,we can see that most of the buyers are females and even purchasing power of females are greater tha men.

# # Age

# In[31]:


df.columns


# In[33]:


ax=sns.countplot(x='Age Group',data=df,hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[36]:


sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount',data=sales_age)


# # on above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State

# In[37]:


df.columns


# In[44]:


sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(x='State',data=sales_state,y='Orders')


# In[49]:


#Total amount/sales from top 10 states
sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(x='State',data=sales_state,y='Amount')


# # From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh,Maharashtra and Karnataka respectively.

# # Martial Status

# In[50]:


df.columns


# In[59]:


ax=sns.countplot(x='Marital_Status',data=df)
sns.set(rc={'figure.figsize':(6,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[62]:


sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(x='Marital_Status',y='Amount',data=sales_state,hue='Gender')


# # From above graphs we can see that most of the buyers are married(Women) and they have high purchasing power.

# # Occupation

# In[63]:


df.columns


# In[64]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(x='Occupation',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[70]:


sales_state=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(21,5)})
sns.barplot(x='Occupation',y='Amount',data=sales_state)


# # from above graphs we can see the most of the buyers are working in IT,Healthcare and Aviation sector.

# # Product Category

# In[72]:


sns.set(rc={'figure.figsize':(24,5)})
ax=sns.countplot(x='Product_Category',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[73]:


sales_state=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_Category',y='Amount',data=sales_state)


# # From above graphs we can see the most of the product sold are from Food,Clothing & Electronics category.

# In[80]:


sales_state=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(21,5)})
sns.barplot(x='Product_ID',y='Orders',data=sales_state)


# # Conclusion:
# # Married women age group 26-35 yrs from UP,Maharastra and Karnataka working i IT,Healthcare and Aviations are more likely to buy products from Food,Clothing and Electronics Category.

# In[ ]:




