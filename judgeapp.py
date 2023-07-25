# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:25:49 2023

@author: GALVJ
"""
import streamlit as st
from pathlib import Path
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Federal Judge Explorer",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# create dababase
Path('judges_data.db').touch()
conn = sqlite3.connect('judges_data.db', timeout=20)
c = conn.cursor()
conn.commit()

# load demographics table
#c.execute('''CREATE TABLE demographics(nid,jid,LastName,FirstName,MiddleName,Suffix,BirthMonth,BirthDay,BirthYear,BirthCity,BirthState,DeathMonth,DeathDay,DeathYear,DeathCity,DeathState,Gender,RaceorEthnicity)''')
#demos = pd.read_csv('demos.csv')
#demos.to_sql('demos', conn, if_exists='append', index = False)
#c.execute('''SELECT * FROM demos''').fetchall()

# load education table
#c.execute('''CREATE TABLE education(nid,Sequence,JudgeName,School,Degree,DegreeYear)''')
edu = pd.read_csv('education.csv')
edu.to_sql('edu', conn, if_exists='append', index = False)
#c.execute('''SELECT * FROM edu''').fetchall()

# load federal-judicial-service table
#c.execute('''CREATE TABLE fedserv(nid,Sequence,JudgeName,CourtType,CourtName,AppointmentTitle,AppointingPresident,PartyofAppointingPresident,ReappointingPresident,PartyofReappointingPresident,ABARating,SeatID,StatuteAuthorizingNewSeat,RecessAppointmentDate,NominationDate,CommitteeReferralDate,HearingDate,JudiciaryCommitteeAction,CommitteeActionDate,SenateVoteType,Ayes/Nays,ConfirmationDate,CommissionDate,ServiceasChiefJudgeBegin,ServiceasChiefJudgeEnd,2ndServiceasChiefJudgeBegin,2ndServiceasChiefJudgeEnd,SeniorStatusDate,Termination,TerminationDate)''')
fedserv = pd.read_csv('fedserv.csv')
fedserv.to_sql('fedserv', conn, if_exists='append', index = False)
#c.execute('''SELECT * FROM fedserv''').fetchall()

# load career table
#c.execute('''CREATE TABLE career(nid,Sequence,JudgeName,ProfessionalCareer)''')
career = pd.read_csv('career.csv')
career.to_sql('career', conn, if_exists='append', index = False)
#c.execute('''SELECT * FROM career''').fetchall()

# load otherfedserv table
#c.execute('''CREATE TABLE otherfedserv(nid,Sequence,JudgeName,Type,OtherFederalJudicialService)''')
otherfedserv = pd.read_csv('otherfedserv.csv')
otherfedserv.to_sql('otherfedserv', conn, if_exists='append', index = False)
#c.execute('''SELECT * FROM otherfedserv''').fetchall()

st.title("Federal Judge Explorer")
demo_table = c.execute('''SELECT * FROM demos''')
st.write(demo_table)



# create edu table
c.execute("""CREATE TABLE if not exists edu(nid int not null,
          Sequence int,
          JudgeName varchar(100) not null,
          School varchar(100),
          Degree varchar(100),
          DegreeYear int,
    primary key(nid));""")
efile = open('C:/Users/galvj/.spyder-py3/db_final/education.csv')
econtents = csv.reader(efile)
insert_erecords = "INSERT or REPLACE INTO edu(nid,Sequence,JudgeName,School,Degree,DegreeYear) VALUES(?,?,?,?,?,?)"
c.executemany(insert_erecords, econtents)
eselect_all = "SELECT * FROM edu"
erows = c.execute(eselect_all).fetchall()
conn.commit()

# join demogs and edu tables
edtable = c.execute('''SELECT * FROM demogs INNER JOIN edu ON demogs.nid = edu.nid''').fetchall()
edtable_df = pd.DataFrame.from_records(edtable, columns= ['nid','jid','LastName','FirstName','MiddleName','Suffix','BirthMonth','BirthDay','BirthYear','BirthCity','BirthState','DeathMonth','DeathDay','DeathYear','DeathCity','DeathState','Gender','RaceorEthnicity','nid2','Sequence','JudgeName','School','Degree','DegreeYear'])

#demos = pd.read_csv('C:/Users/galvj/.spyder-py3/db_final/demos.csv')
#demos_df = pd.DataFrame(demos, columns=['nid','jid','LastName','FirstName','MiddleName','Suffix','BirthMonth','BirthDay','BirthYear','BirthCity','BirthState','DeathMonth','DeathDay','DeathYear','DeathCity','DeathState','Gender','RaceorEthnicity'])

#group_year = state_year_df.groupby(["BirthYear", "BirthState"])["nid"].size().to_frame(name = 'count').reset_index()


state_year_count = c.execute('''SELECT BirthState, BirthYear FROM judges2 GROUP BY BirthState''').fetchall()
state_year_count_df = pd.DataFrame.from_records(state_year_count, columns = ["BirthState", "BirthYear"])

state_year_df_revised = state_year_count_df.assign(region = state_year_count_df.BirthState.map(region_mapping))

group_year_revised = state_year_df_revised.groupby(["BirthYear","region"])

hist = state_year_df_revised.hist(bins=15)

birthplacechart = alt.Chart(state_year_df_revised).mark_circle().encode(
    x ='BirthYear:O',
    y = "Count",
    size = "Count",
    color = "region").interactive()

with st.container():
    st.altair_chart(birthplacechart, theme='streamlit', use_container_width = True)
    
