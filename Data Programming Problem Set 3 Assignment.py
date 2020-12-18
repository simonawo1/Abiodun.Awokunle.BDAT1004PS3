#!/usr/bin/env python
# coding: utf-8

# #Question 4

# In[49]:


#Step 1 : We will need the datetime module for this question and will need to import it with panda and numpy
import pandas as pd
import numpy as np
import datetime 


# In[50]:


#Step 2 
#Give Winddata as name of the dataframe and import it
Winddatas = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data", sep="\s+")


# In[51]:


#Number of rows is much so we will call only the first 10 and the last 10 to display the dataframe
Winddatas.head(10)


# In[52]:


Winddatas.tail(10)


# In[53]:


#Step 4
#Add the Yr, Mo, Dy column as a single column to show a single column displaying a normal date
def to_datetime(year, month, day):
    currentdate = f"19{int(year)}-{int(month)}-{int(day)}"
    return currentdate


# In[54]:


Winddatas["currentdate"] = Winddatas.apply(lambda x: to_datetime(x['Yr'], x['Mo'], x['Dy']), axis=1)


Winddatas.drop(["Yr","Mo", "Dy"], axis = 1, inplace = True)
Winddatas.head()


# In[55]:


Winddatas["currentdate"] = pd.to_datetime(Winddatas["currentdate"], infer_datetime_format=True)


Winddatas.head()


# In[56]:


#Step 5
#Reference stackoverflow
print(Winddatas["currentdate"].dtypes)
Winddatas.set_index('currentdate', inplace=True)


# In[57]:


#Step 6
#Missing values for each location
NoValue = Winddatas.isnull().sum()
NoValue


# In[58]:


#Step 7
#Available value
Value = Winddatas.notnull().sum().sum()
Value


# In[59]:


#Step 8
#Calculate the overall mean
Winddatas.mean().mean()


# In[60]:


#Step 9
#Create new dataset called loc_stats
loc_stats = Winddatas.describe()
loc_stats


# In[62]:


#Step 10
#Create new dataframe called day_stats 
day_stats = Winddatas.apply(pd.Series.describe, axis=1)
day_stats.head()


# In[66]:


#Step 11
#Using the .loc command which displays all the variables for a row
jan_mean = Winddatas.loc[Winddatas.index.month==1, :].mean()
jan_mean


# In[67]:


#Step 12
#I referenced https://www.geeksforgeeks.org/python-pandas-dataframe-resample/
#Letting Y represent year
Yearfreq = Winddatas.resample('Y').sum()
Yearfreq


# In[68]:


# step 13
#Letting M represent month
Monthlyfreq = Winddatas.resample('M').sum()
Monthlyfreq


# In[69]:


# step 14
#Letting W represent Week
Weeklyfreq2 = Winddatas.resample('W').sum()
Weeklyfreq2


# #Question 5
# 

# In[13]:


#Steps 1, 2, 3, 4
#Import data and assign it to variable named Chipo
Chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep='\t')
Chipo.head(10)


# In[14]:


#Step 5 - Number of observations
Chipo.shape[0]


# In[16]:


#Step 6 - Number of columns
print(len(Chipo.columns))


# In[17]:


#Step 7
list(Chipo.columns) 


# In[18]:


#Step 8 - Don't have much idea
Chipo.index[0]


# In[19]:


#Step 9
Chipo.groupby(["item_name", "quantity"]).size().reset_index(name="Count").sort_values(by="Count", ascending=False).drop_duplicates("item_name", keep="first")


# In[20]:


#Step 10
orderqty1 = Chipo.groupby(["item_name", "quantity"]).size()
orderqty1


# In[21]:


#Step 10
orderqty1 = orderqty1.reset_index()
orderqty1


# In[111]:


#Step 10
mostordered = orderqty1[orderqty1.quantity == orderqty1.quantity.max()]
mostordered


# In[85]:


#Step 11
Chipo.groupby(["choice_description", "quantity"]).size().reset_index(name="Count").sort_values(by="Count", ascending=False).drop_duplicates("choice_description", keep="first")


# In[112]:


#Step 12
Chipo.sum()


# In[22]:


#Step14
(Chipo['quantity'] * Chipo['item_price']).sum()



# In[23]:


#Step 15
Chipo['quantity'].sum()


# In[70]:


#Step 16
round((Chipo['quantity']*Chipo['item_price']).sum()/Chipo['quantity'].sum(), 2)


# In[71]:


#Step 17
Chipo['item_name'].nunique()


# #Question 6

# In[149]:


##Step 1 - change the backward slash to forward slash and call the dataset
Marriages1 = pd.read_csv('C:/Users/simon/OneDrive/Desktop/Dataset/us-marriages-divorces-1867-2014.csv')
Marriages1


# In[150]:


#Make the Year column the index column 
Marriages1.set_index('Year', inplace=True)
Marriages1


# In[179]:


Marriages1[["Marriages_per_1000", "Divorces_per_1000"]].plot(kind='line')

plt.ylabel('Marriages and Divorces per capita')


# #Question 7

# In[163]:


#Step 1 - change the backward slash to forward slash and call the dataset
Marriages2 = Marriages1[Marriages1.index.isin([1900, 1950,2000])]
Marriages2


# In[180]:


Marriages2[["Marriages_per_1000", "Divorces_per_1000"]].plot(kind='bar')


plt.ylabel('Marriages and Divorces per capita')


# #Question 8

# In[165]:


##Step 1 - change the backward slash to forward slash and call the dataset
Actornoofkills = pd.read_csv('C:/Users/simon/OneDrive/Desktop/Dataset/actor_kill_counts.csv')
Actornoofkills


# In[184]:


Actornoofkills.set_index('Actor')


# In[185]:


Actornoofkills.plot(kind='barh')

plt.ylabel('Actor')


# #Question 9

# In[167]:


#Step 1 - change the backward slash to forward slash and call the dataset
Emperor = pd.read_csv('C:/Users/simon/OneDrive/Desktop/Dataset/roman-emperor-reigns.csv')
Emperor


# In[193]:


Emperor.groupby(['Cause_of_Death']).sum().plot(kind='pie', subplots=True, shadow = True,startangle=90,
figsize=(15,10), autopct='%1.1f%%')


# #Question 10

# In[25]:


#Step 1 - change the backward slash to forward slash and call the dataset
ArcadeDoc = pd.read_csv('C:/Users/simon/OneDrive/Desktop/Dataset/arcade-revenue-vs-cs-doctorates.csv')
ArcadeDoc


# In[31]:


# create color dictionary
colors = {'ArcadeDoc-setosa':'r', 'ArcadeDoc-versicolor':'g', 'ArcadeDoc-virginica':'b'}
# create a figure and axis
fig, ax = plt.subplots()
# plot each data-point
for i in range(len(ArcadeDoc['Total Arcade Revenue (billions)'])):
    ax.scatter(ArcadeDoc['Total Arcade Revenue (billions)'][i], ArcadeDoc['Computer Science Doctorates Awarded (US)'][i])
# set a title and labels
ax.set_title('ArcadeDoctorates Dataset')
ax.set_xlabel('Total Arcade Revenue (billions)')
ax.set_ylabel('Computer Science Doctorates Awarded (US)')


# #Question 3

# In[82]:


# Step 1 - import neccessary libraries
import pandas as pd
import random
import numpy as np


# In[92]:


#Step 2
randomList1 = []
randomList2 = []
randomList3 = []

# Set a length of the list to 100
for i in range(0, 100):
   
    #Any random numbers as stated for the 3 series in the question
    randomList1.append(random.randint(1, 4))
    randomList2.append(random.randint(1, 3))
    randomList3.append(random.randint(10000, 30000))
    


# In[93]:


print(len(randomList1))
print(len(randomList2))
print(len(randomList3))


# In[94]:


#Step 3
JoinSeries = zip(randomList1, randomList2, randomList3)
JoinTable = pd.DataFrame(list(JoinSeries))

JoinTable


# In[96]:


#Step 4
JoinTable.rename(columns={0: "bedrs", 1: "bathrs", 2:"price_sqr_meter"}, inplace=True)
JoinTable


# In[98]:


#Step 5
bigcolumn = randomList1 + randomList2 + randomList3
bigcolumn


# In[ ]:


#Step 6
Answer No


# In[101]:


#Step 7
JoinTable = JoinTable.reindex(list(range(300))


# In[ ]:




