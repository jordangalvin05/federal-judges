# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:46:23 2023

@author: GALVJ
"""

import streamlit as st
from pathlib import Path
import sqlite3
import pandas as pd
import csv
import altair as alt


st.set_page_config(
    page_title="Federal Judge Explorer",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Federal Judge Explorer")

st.header("Introduction")
st.write("Welcome to the Federal Judge Explorer App. The goal is to provide an interactive space for you to learn more about our federal judiciary.")

# get columns into dict format
#demog_df = pd.read_csv('demos.csv', usecols=['nid','jid','LastName','FirstName','MiddleName','Suffix','BirthMonth','BirthDay','BirthYear','BirthCity','BirthState','DeathMonth','DeathDay','DeathYear','DeathCity','DeathState','Gender','RaceorEthnicity'])
#demog_result = demog_df.to_dict(orient = 'records')
#demog_result
# create database

######################## CREAT DATABASES, TABLES #################################

Path('judges_data_full.db').touch()
conn = sqlite3.connect('judges_data_full.db', timeout=20)
c = conn.cursor()
conn.commit()

# create main table judges2

c.execute("""CREATE TABLE if not exists judges2(nid int not null,
          jid int not null,
          LastName varchar(100) not null,
          FirstName varchar(100) not null,
          MiddleName varchar(100) not null,
          Suffix varchar(10),
          BirthMonth int,
          BirthDay int,
          BirthYear int,
          BirthCity varchar(100),
          BirthState varchar(100),
          DeathMonth int,
          DeathDay int,
          DeathYear int,
          DeathCity varchar(100),
          DeathState varchar(100),
          Gender varchar(100),
          RaceorEthnicity varchar(100),
          CourtType varchar(100),	
          CourtName	varchar(100),
          AppointmentTitle varchar(100),
          AppointingPresident varchar(100),
          PartyofAppointingPresident varchar(100),
          ABARating varchar(100),
          SeatID varchar(100),
          StatuteAuthorizingNewSeat	varchar(100),
          RecessAppointmentDate varchar(100),
          NominationDate varchar(100),
          HearingDate varchar(100),
          JudiciaryCommitteeAction varchar(100),
          CommitteeActionDate varchar(100),
          SenateVoteType varchar(100),
          AyesNays varchar(100),
          ConfirmationDate varchar(100),
          ServiceasChiefJudgeBegin varchar(100),
          ServiceasChiefJudgeEnd varchar(100),
          Termination varchar(100),
          TerminationDate varchar(100),
          CourtType2 varchar(100),
          CourtName2 varchar(100),
          AppointmentTitle2 varchar(100),
          AppointingPresident2 varchar(100),
          PartyofAppointingPresident2 varchar(100),
          ABARating2 varchar(100),
          SeatID2 varchar(100),
          StatuteAuthorizingNewSeat2 varchar(100),
          AyesNays2 varchar(100),
          ConfirmationDate2 varchar(100),
          ServiceasChiefJudgeBegin2 varchar(100),
          ServiceasChiefJudgeEnd2 varchar(100),
          Termination2 varchar(100),
          TerminationDate2 varchar(100),
          CourtType3 varchar(100),
          CourtName3 varchar(100),
          AppointmentTitle3 varchar(100),
          AppointingPresident3 varchar(100),
          PartyofAppointingPresident3 varchar(100),
          ABARating3 varchar(100),
          SeatID3 varchar(100),
          StatuteAuthorizingNewSeat3 varchar(100),
          AyesNays3 varchar(100),
          ConfirmationDate3 varchar(100),
          Termination3 varchar(100),
          TerminationDate3 varchar(100),
          CourtType4 varchar(100),
          CourtName4 varchar(100),
          AppointmentTitle4 varchar(100),
          OtherFederalJudicialService2 varchar(100),
          OtherFederalJudicialService3 varchar(100),
          OtherFederalJudicialService4 varchar(100),
          School varchar(100),
          Degree varchar(100),
          DegreeYear varchar(100),
          School2 varchar(100),
          Degree2 varchar(100),
          DegreeYear2 varchar(100),
          School3 varchar(100),
          Degree3 varchar(100),
          DegreeYear3 varchar(100),
          School4 varchar(100),
          Degree4 varchar(100),
          DegreeYear4 varchar(100),
          School5 varchar(100),
          Degree5 varchar(100),
          DegreeYear5 varchar(100),
          ProfessionalCareer varchar(1000),
          OtherNominationsRecessAppointments varchar(1000),
    primary key(nid));""")
file = open('judges_cleaned.csv')
contents = csv.reader(file)
insert_records = "INSERT or REPLACE INTO judges2(nid,jid,LastName,FirstName,MiddleName,Suffix,BirthMonth,BirthDay,BirthYear,BirthCity,BirthState,DeathMonth,DeathDay,DeathYear,DeathCity,DeathState,Gender,RaceorEthnicity,CourtType,CourtName,AppointmentTitle,AppointingPresident,PartyofAppointingPresident,ABARating,SeatID,StatuteAuthorizingNewSeat,RecessAppointmentDate,NominationDate,HearingDate,JudiciaryCommitteeAction,CommitteeActionDate,SenateVoteType,AyesNays,ConfirmationDate,ServiceasChiefJudgeBegin,ServiceasChiefJudgeEnd,Termination,TerminationDate,CourtType2,CourtName2,AppointmentTitle2,AppointingPresident2,PartyofAppointingPresident2,ABARating2,SeatID2,StatuteAuthorizingNewSeat2,AyesNays2,ConfirmationDate2,ServiceasChiefJudgeBegin2,ServiceasChiefJudgeEnd2,Termination2,TerminationDate2,CourtType3,CourtName3,AppointmentTitle3,AppointingPresident3,PartyofAppointingPresident3,ABARating3,SeatID3,StatuteAuthorizingNewSeat3,AyesNays3,ConfirmationDate3,Termination3,TerminationDate3,CourtType4,CourtName4,AppointmentTitle4,OtherFederalJudicialService2,OtherFederalJudicialService3,OtherFederalJudicialService4,School,Degree,DegreeYear,School2,Degree2,DegreeYear2,School3,Degree3,DegreeYear3,School4,Degree4,DegreeYear4,School5,Degree5,DegreeYear5,ProfessionalCareer,OtherNominationsRecessAppointments) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
c.executemany(insert_records, contents)
select_all = "SELECT * FROM judges2"
rows = c.execute(select_all).fetchall()

conn.commit()

df=pd.read_sql_query(select_all,conn)


######################## DATA EXPLORATION #################################

# general exploration queries
c.execute('''SELECT DISTINCT School FROM judges2''').fetchall()
c.execute('''SELECT DISTINCT ABARating FROM judges2''').fetchall()
#c.execute('''SELECT RaceorEthnicity FROM judges2 WHERE RaceorEthnicity LIKE 'Asia%''').fetchall()
c.execute('''SELECT DegreeYear FROM judges2 WHERE DegreeYear > 1950''').fetchall()

# explore demographics data

## Where were our judges born?
st.subheader("Where were our federal judges born?")

###count number of each birth state and transform to dataframe 
birth_state_count = c.execute('''SELECT BirthState, COUNT(*) FROM judges2 GROUP BY Birthstate''').fetchall()
birth_count_df = pd.DataFrame.from_records(birth_state_count, columns = ["BirthState", "Count"])

#print(birth_count_col)


## Does where judges are born change over time? Count number of each birth state per year and transform to dataframe

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

df["region"] = df["BirthState"].map(region_mapping)
region_count = df['region'].value_counts()
region_count_df = region_count.rename_axis('region').reset_index(name='count')
#print(region_count_df)

tab_birthstate, tab_birthregion = st.tabs(["Birth State","Birth Region"])
with tab_birthstate:
    st.subheader("Count of Birth States")
    st.bar_chart(birth_count_df, x = "BirthState", y="Count")
    #st.write(birth_count_df)
with tab_birthregion:
    st.subheader("Count of Birth Regions")
    st.bar_chart(region_count_df, x="region",y="count")
    
region_state_year = df[['region','BirthState', 'BirthYear']].value_counts().to_frame()
rsy_df_flat = region_state_year.reset_index()
rsy_df_flat.columns = ['region', 'BirthState','BirthYear','region_count']

circles = (
    alt.Chart()
    .mark_circle()
    .encode(
        alt.X("BirthYear:Q", title = "BirthYear",scale=alt.Scale(domain=[1700,2020])),
        alt.Y('region_count:Q', title="Region Count"),
        )
)
rsy_chart = alt.Chart(rsy_df_flat).mark_circle().encode(
    x='BirthYear',y='region_count',size='region_count', color = 'region').interactive()

st.altair_chart(rsy_chart, theme=None, use_container_width=True)

## judiciary by gender

st.header("Explore the Gender Divide")

gender_count = df[['Gender']].value_counts().to_frame()
gender_count_flat = gender_count.reset_index()
gender_count_flat.columns = ["Gender", "Gender_Count"]

# create graphs

st.subheader("Gender Divide")
st.bar_chart(gender_count_flat, x = 'Gender', y='Gender_Count')

## judiciary by race/ethnicity
st.header("Historical Race and Ethnic Makeup of the Judiciary")

race_count = df[['RaceorEthnicity']].value_counts().to_frame()
race_count_flat = race_count.reset_index()
race_count_flat.columns = ["Race/Ethnicity", "Race/Ethnicity_Count"]
st.bar_chart(race_count_flat, x = 'Race/Ethnicity', y='Race/Ethnicity_Count')

# explore education data

# explore political ties and career data

## Interactivity

# filters
st.header("Explore the raw data.")

# raw data section

st.write("Help us quality control! If you see something missing or incorrect, click a cell to edit it.")
edited_df = st.data_editor(df, num_rows="dynamic")
#your_add = edited_df.loc[edited_df["nid"].idxmax()]["LastName"]
#st.markdown(f"You added Judge **{your_add}**")
