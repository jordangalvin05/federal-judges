# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:36:09 2023

@author: GALVJ
"""

import pandas as pd
import numpy as np
import csv
import altair as alt
import streamlit as st
import plotly




#c.execute('''CREATE TABLE demographics(nid,jid,LastName,FirstName,MiddleName,Suffix,BirthMonth,BirthDay,BirthYear,BirthCity,BirthState,DeathMonth,DeathDay,DeathYear,DeathCity,DeathState,Gender,RaceorEthnicity)''')
demos = pd.read_csv('demos.csv')
demos_df = pd.DataFrame(demos, columns=['nid','jid','LastName','FirstName','MiddleName','Suffix','BirthMonth','BirthDay','BirthYear','BirthCity','BirthState','DeathMonth','DeathDay','DeathYear','DeathCity','DeathState','Gender','RaceorEthnicity'])

demos_df.head(20)

state_year_df = demos_df[["nid","BirthState", "BirthYear"]]
group_year = state_year_df.groupby(["BirthYear", "BirthState"])["nid"].size().to_frame(name = 'count').reset_index()


group_state = state_year_df.groupby(["BirthState"])

##charts
hist = group_year.hist(bins=15)

chart = alt.Chart(group_year).mark_circle().encode(
    x="BirthYear",
    y = "count",
    size = "count",
    color = "BirthState").interactive()

st.altair_chart(chart, theme='streamlit')


# add column for region
region_mapping = {'AK':'West',
                  'AL':'South',
                  'Angola': 'Africa',
                  'Antigua':'Caribbean',
                  'AR':'South',
                  'Asia Minor': 'Asia',
                  'Australia' : 'Oceana',
                  'Austra' : 'Europe',
                  'Austria-Hungary' : 'Europe',
                  'AZ': 'Southwest',
                  'Bermuda' : 'Caribbean',
                  'Brazil' : 'Latin America',
                  'CA' : 'West',
                  'Canada' : 'Canada',
                  'Cayman Islands': "Caribbean",
                  'China':'Asia',
                  'CO' : 'West',
                  'Colombia' : 'Latin America',
                  'CT' :'Northeast',
                  'Cuba': 'Caribbean',
                  'DC' : 'Northeast',
                  'DE' : 'Northeast',
                  'Denmark':'Europe',
                  'Dominican Republic': 'Caribbean',
                  'Ecuador':'Latin America',
                  'England':'Europe',
                  'FL':'Southeast',
                  'France':'Europe',
                  'GA': 'South',
                  'Germany': 'Europe',
                  'HI':'US Islands',
                  'Hong Kong': 'Asia',
                  'Hungary': 'Europe',
                  'IA' : 'Midwest',
                  'ID' : 'West',
                  'IL' : 'Midwest',
                  'IN' : 'Midwest',
                  'India' : 'Asia',
                  'Iraq':'Middle East',
                  'Ireland': 'Europe',
                  'Italy': 'Europe',
                  'Jamaica':'Caribbean',
                  'Japan' : 'Asia',
                  'KS': 'Midwest',
                  'KY':'South',
                  'LA': 'South',
                  'Latvia': 'Europe',
                  'MA' : 'Northeast',
                  'MD': 'Northeast',
                  'ME': 'Northeast',
                  'Mexico': 'Latin America',
                  'MI':'Midwest',
                  'MN':'Midwest',
                  'MO':'Midwest',
                  'MS':'South',
                  'MT':'West',
                  'NC': 'Southeast',
                  'ND':'Midwest',
                  'NE':'Midwest',
                  'NH':'Northeast',
                  'Nigeria':'Africa',
                  'NJ':'Northeast',
                  'NM':'Southwest',
                  'Norway':'Europe',
                  'NV':'Southwest',
                  'NY':'Northeast',
                  'OH': 'Midwest',
                  'OK': 'South',
                  'OR': 'West',
                  'PA': 'Northeast',
                  'Pakistan': 'Middle East',
                  'Panama':'Latin America',
                  'Poland': 'Europe',
                  'Prussia':'Europe',
                  'Puerto Rico':'US Islands',
                  'RI':'Northeast',
                  'Romania':'Europe',
                  'Russia': 'Eurasia',
                  'Saudi Arabia': 'Middle East',
                  'SC': 'Southeast',
                  'Scotland':'Europe',
                  'SD':'Midwest',
                  'Sierra Leone':'Africa',
                  'South Korea':'Asia',
                  'Spain':'Europe',
                  'Sweden':'Europe',
                  'Syria':'Middle East',
                  'Taiwan': 'Asia',
                  'TN':'South',
                  'TX':'South',
                  'Ukraine':'Europe',
                  'Uruguay':'Latin America',
                  'UT':'West',
                  'VA':'Southeast',
                  'VA (now WV)':'Southeast',
                  'Venezuela': 'Latin America',
                  'Vietnam':'Asia',
                  'VT':'Northeast',
                  'WA':'West',
                  'WI':'Midwest',
                  'WV':'Southeast',
                  'WY':'West',
                  ' ' :'blank'
    }

state_year_df_revised = state_year_df.assign(region = state_year_df.BirthState.map(region_mapping))
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")