#Importing libraries
import pandas as pd
import streamlit as st

#Loading df
df = pd.read_csv("JD_QP_similarity.csv")
df.head()

#Streamlit
st.title("NSDC (Prototype)")
st.header("Matching Job Descriptions with Qualification Pack")

#Selecting job
selected_job = st.selectbox("Select a job", df["job"].unique(), index = None, placeholder= "job title")

#Selecting sector
all_option = 'Select all'
selected_sector = st.multiselect("Select sector(s)", options = [all_option] + list(df["qp_sector"].unique()), default = [], placeholder = "sector")

#Selecting no of QPs to display
number_QPs = st.selectbox("Number of top QP matches", [5,10,15], index = None, placeholder= "Choose a number from below")

if all_option in selected_sector:
    selected_sector = list(df["qp_sector"].unique())
    st.write("All sectors selected")

filtered_df = df[(df["job"] == selected_job) & (df["qp_sector"].isin(selected_sector))]
filtered_df = filtered_df.sort_values(by = 'similarity', ascending = False)
filtered_df = filtered_df[:number_QPs]
filtered_df.index = range(1,len(filtered_df)+1)

if st.button ("Find closest matching Qualification Packs", type = "primary"):
    #st.dataframe(filtered_df, hide_index= True)
    st.data_editor(
        filtered_df,
        column_config = {
            "similarity": st.column_config.ProgressColumn(
            "similarity score",
            format="%.2f",
            min_value=0,
            max_value=1,
            ),
            },
        hide_index=True,
        )
