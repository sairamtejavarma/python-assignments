#!/usr/bin/env python
# coding: utf-8

# # E-commerce EDA

# Importing some necessary libraries
# here I will be using numpy,pandas,matplotlib and seaborn

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
from scipy import stats


# # ANALYSIS OF THE CUSTOMERS DATABASE

# In[2]:


customers=pd.read_csv(r"C:\Users\hp\Downloads\olist_customers_dataset.csv.zip")


# In[3]:


customers


# In[10]:


customers.shape


# in customers data set there are 99441 rows and 5 columns

# In[11]:


customers.info()


# In[4]:


customers.isnull().sum()


# As we can see, there are no missing values in the table.

# In[16]:


customers["customer_unique_id"].value_counts()


# There are 96096 unique customers

# In[18]:


customers["customer_state"].unique()


# In[9]:


customers["customer_state"].value_counts()


# In[4]:


customers_copy=customers.copy()


# In[5]:


customers_copy


# In[17]:


sns.histplot(data=customers_copy,x="customer_state",bins=5)
plt.title('State Wise Customers Distribution')
plt.xlabel('State')
plt.ylabel('No. of Customers')


# The most customers come from the state SP and 2nd most highest customers are from RJ

# In[6]:


customers_copy["customer_city"].value_counts()


# In[7]:


c1=customers.groupby('customer_city')['customer_id'].nunique().sort_values(ascending=False)


# In[8]:


c1


# In[9]:


c2=c1.head(10)


# In[10]:


c2


# here we can see that the most no of customers come from SAO PAULO city 

# In[14]:


zips = customers.groupby('customer_zip_code_prefix')['customer_id'].nunique().sort_values(ascending=False)


# In[15]:


zips


# Products were delivered the most frequently, 142 times, to the 22790 zip code.

# # ANALYSIS OF THE ORDERS DATABASE

# In[19]:


orders=pd.read_csv(r"C:\Users\hp\Downloads\olist_orders_dataset.csv.zip")


# In[20]:


orders


# In[20]:


orders.shape


# as we can see there are  99441 orders 

# In[21]:


orders.isnull().sum()


# as there are missing values we will make a copy of the data and remove the missing value rows 

# In[23]:


orders_copy=orders.copy()


# In[24]:


orders_copy


# In[28]:


orders_copy=orders_copy.dropna()


# In[30]:


orders_copy.shape


# In[31]:


orders_copy.order_status.value_counts()


# In[46]:


diff_approved_purchase=(pd.to_datetime(orders_copy.order_approved_at) - pd.to_datetime(orders_copy.order_purchase_timestamp)).dt.days


# In[47]:


diff_approved_purchase


# In[48]:


diff_approved_purchase.mean()


# here we can see that the Average time taken for the order to get approved is 0.26 days 

# In[51]:


dif_estimated_deliverydate=(pd.to_datetime(orders_copy.order_estimated_delivery_date) - pd.to_datetime(orders_copy.order_delivered_customer_date)).dt.days


# In[52]:


dif_estimated_deliverydate


# In[53]:


dif_estimated_deliverydate.mean()


# here we can see the Average time taken between estimated delivery date and actual delivery date is 11 days

# # ANALYSIS OF ORDER ITEMS DATABASE

# In[54]:


orderitems=pd.read_csv(r"C:\Users\hp\Downloads\olist_order_items_dataset.csv.zip")


# In[55]:


orderitems


# In[56]:


orderitems.shape


# In[57]:


orderitems.isnull().sum()


# As we can see there are no missing values in the data

# In[58]:


sns.histplot(x='price', data=orderitems)
plt.title('Distribution of Price')
plt.xlabel('Price')


# As we can see, most orders are under 1000 Brazilian Reals 

# # ANALYSIS OF PAYMENT DATASET

# In[82]:


payment=pd.read_csv(r"C:\Users\hp\Downloads\olist_order_payments_dataset.csv.zip")


# In[83]:


payment


# In[62]:


payment.shape


# In[63]:


payment.isnull().sum()


# As we can see there are no missing values

# In[70]:


sns.countplot(x='payment_type', data=payment)
plt.title('Analyzing Payment Types')
plt.xlabel('Payment Type')
plt.ylabel('No. of Customers')


# In[86]:


payment_type_counts =payment['payment_type'].value_counts()


# In[87]:


payment_type_counts


# In[88]:


plt.pie(payment_type_counts,labels=payment_type_counts.index,autopct="%0.2f%%")


# In[96]:


sns.scatterplot(data=payment,x="payment_installments",y="payment_value")
plt.grid(True)
plt.show()


# In[97]:


payment_type_avg_value = payment.groupby('payment_type')['payment_value'].mean()


# In[98]:


plt.bar(payment_type_avg_value.index, payment_type_avg_value.values)
plt.title('Average Payment Value by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Average Payment Value')


# In[ ]:


sns.swarmplot(data=payment,x="payment_value")


# # ANALYSIS OF REVIEWS DATABASE

# In[99]:


reviews=pd.read_csv(r"C:\Users\hp\Downloads\olist_order_reviews_dataset.csv.zip")


# In[100]:


reviews


# In[101]:


reviews.shape


# In[102]:


reviews.isnull().sum()


# as there are more missing values in the comment_title and comment_message columns so, droping the columns

# In[103]:


sns.countplot(x='review_score', data=reviews)
plt.title('Analyzing Review Score')
plt.xlabel('Score')
plt.ylabel('No. of Reviews')


# # ANALYSIS OF SELLERS DATABASE

# In[7]:


sellers=pd.read_csv(r"C:\Users\hp\Downloads\olist_sellers_dataset (1).csv")


# In[8]:


sellers


# In[118]:


sellers.shape


# In[119]:


sellers.isnull().sum()


# In[9]:


sellers_copy=sellers.copy()


# In[121]:


sellers_copy


# In[123]:


sns.countplot(x='seller_state', data=sellers_copy)
plt.title('State Wise Seller Distribution')
plt.xlabel('State')
plt.ylabel('No. of Sellers')


# As we can see, most number of sellers are from state 'SP'

# # ANALYSIS OF GEOLOCATION DATABASE

# In[129]:


geo=pd.read_csv(r"C:\Users\hp\Downloads\olist_geolocation_dataset.csv.zip")


# In[130]:


geo


# In[131]:


geo.shape


# In[132]:


geo.isnull().sum()


# In[ ]:




