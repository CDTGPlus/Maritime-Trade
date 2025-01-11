import streamlit as st
import plotly.express as px
from data_process import *

st.set_page_config(layout="wide")

# 3 columns for the top row
col1, col2, col3 = st.columns(3)
# Display world chart
fig1 = px.choropleth(nations,
                    locations='Country',   # Country names
                    locationmode='country names',  # Specify the location mode
                    color='count',         # Number of ports
                    color_continuous_scale="Viridis", 
                    labels={'Ports': 'National Location Of Top 50 Ports'},
                    title="Countries with the Most Ports")
with col1:
    st.plotly_chart(fig1)
# Display regional chart (as pir chart)
fig2 = px.pie(regions, names='Region', values='count', hole=0.4, title='Regions With The most High Volume Container Ports')
with col2:
    st.plotly_chart(fig2)
# Dsiplay historic maritime index price chart
fig3 = px.bar(freight_cost, x='Year', y='Cost',title='Average Shipping Freight Cost Index (London Baltic Exchange)')
with col3:
    st.plotly_chart(fig3)

st.write("\n")
# st.dataframe(national_data)
# Define the options for the multiselect
options = list(national_data.columns)

# Add "Select All" to the options
st.write("Top 50 Busiest Ports In The World By Container Traffic")
options_with_select_all = ["Select All"] + options
selected_options = st.multiselect("Select options", options_with_select_all, default="Select All")
if selected_options:
    if "Select All" in selected_options:
        fig4 = px.line(national_data)

    else:
        fig4 = px.line(select_country(national_data,selected_options))

    st.plotly_chart(fig4)
else:
    st.write("Select port to display historical freight container volume")