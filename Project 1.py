#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas_datareader')


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from pandas_datareader.data import get_data_yahoo


# In[10]:


get_ipython().system('pip install yfinance')


# In[3]:


import yfinance as yf
import pandas as pd
tickers = input("ENTER STOCK NAME : ").split()
start_date = input(" Enter start date : ")
end_date = input("Enter end date : ")
capm = yf.download(tickers, start=start_date, end=end_date, interval='1mo')
print(capm)


# In[15]:


capm = capm[['AAPL', '^GSPC', '^IRX']]  # Select the desired columns
capm.columns = ['AAPL', 'GSPC', 'IRX']  # Rename the columns
print(capm)


# In[16]:


capm_return = capm.join(capm[['AAPL', 'GSPC']].pct_change().add_suffix('_m_return'))
capm_return


# In[17]:


capm_return['AAPL_rp'] = capm_return['AAPL_m_return'] - capm_return['IRX']
capm_return['GSPC_rp'] = capm_return['GSPC_m_return'] - capm_return['IRX']
capm_return


# In[18]:


capm_return['GSPC_rp'].describe()


# In[36]:


capm_return.plot.scatter(x='GSPC_rp', y='AAPL_rp', title='Market return vs. Apple return', figsize = (12, 7))


# In[23]:


capm_lm = smf.ols("AAPL_rp ~ GSPC_rp", data=capm_return).fit()
capm_lm.summary()


# In[ ]:





# In[25]:


capm_return[['AAPL_rp','GSPC_rp']].cov()


# In[26]:


capm_lm.rsquared


# In[32]:


plt.figure(figsize=(12 ,7))
ax = sns.regplot(x= 'GSPC_rp', y='AAPL_rp', data=capm_return, fit_reg=True,
            scatter_kws={"color": "black"}, line_kws={'color':'red'})
ax.set_title("Market return vs. Apple return")
ax.set(xlabel="Market", ylabel="Apple")


# In[35]:


capm_return.to_csv('capm_return.csv')
print(capm_return)

