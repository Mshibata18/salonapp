#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


merged_df = pd.read_csv("merged.csv")


# In[5]:


st.title("ｻﾛﾝｻｰﾁ")
price_limit = st.slider("最低ｶｯﾄ価格の上限", min_value=2000,
      max_value=8500, step=200, value=6000)
score_limit = st.slider("人気ｽｺｱの下限", min_value=0.0,
      max_value=35.0, step=2.0, value=5.0)


# In[7]:


filtered_df = (merged_df['price'] <= price_limit) & (merged_df['pop_score'] >=
score_limit


# In[28]:


fig = px.scatter
filtered_df,


# In[38]:


X='pop_score',
y='price',
hover_data=['name_salon', 'access','star', 'review'],
title='人気ｽｺｱと最低ｶｯﾄ価格の散布図'


# In[1]:


(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
st.plotly_chart(fiimport plotly.express as px
fig = px.scatterg)
print(type(fig))


# In[50]:


selected_salon = st.selectbox('気になるｻﾛﾝを選んで詳細を確認', filtered_df['name_salon'])

if selected_salon:
    url = filtered_df[filtered_df['name_salon'] == selected_salon]['link_detail'].values[0]
    st.markdown(f"[{selected_salon}のﾍﾟｰｼﾞへ移動] ({url})", unsafe_allow_html=True)


# In[2]:


sort_key = st.selectbox(
    "ﾗﾝｷﾝｸﾞ基準を選んでください",
    ("star", "pop_score", "review", "price", "seats")
)
ascending = True if sort_key == "price" else False   


# In[51]:


st.subheader(f"{sort_key} によるｻﾛﾝﾗﾝｷﾝｸﾞ(上位10件)")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)
st.dataframe(ranking_df[["name_salon", "price", "pop_score", "star", "review",
"seats", "access"]])   


# In[ ]:




