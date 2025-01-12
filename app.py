import streamlit as st
import plotly.express as px
from data_process import *
#page configuration

st.set_page_config(page_title='Maritime Trade',page_icon=':ship:',layout="wide")

option = st.sidebar.selectbox("Navigation", ["Main", "About"])
if option == "Main":
    st.header('Maritime Trade History')
    # 3 columns for the top row
    col1, col2, col3 = st.columns(3)
    # Display world chart
    fig1 = px.choropleth(nations,
                        locations='Country',   # Country names
                        locationmode='country names',  # Specify the location mode
                        color='count',         # Number of ports
                        color_continuous_scale="Viridis", 
                        labels={'Ports': 'National Location Of Top 50 Ports'},
                        title="Geographic Location Of Top High Volume Ports")
    with col1:
        st.plotly_chart(fig1)
    # Display regional chart (as pir chart)
    fig2 = px.pie(regions, names='Region', values='count', hole=0.4, title='Regions With The most High Volume Container Ports')
    with col2:
        st.plotly_chart(fig2)
    # Dsiplay historic maritime index price chart
    fig3 = px.bar(freight_cost, x='Year', y='Cost',title='Average Shipping Freight Cost (London Baltic Exchange, Cost USD)')
    with col3:
        st.plotly_chart(fig3)

    st.write("\n")
    # Define the options for the multiselect
    options = list(national_data.columns)

    # Add "Select All" to the options
    st.write("Top 50 Busiest Ports In The World By Container Traffic")
    options_with_select_all = ["Select All"] + options
    selected_options = st.multiselect("Select options", options_with_select_all, default="Select All")

    if selected_options:
        if "Select All" in selected_options:
            n_data = national_data

        else:
            n_data = select_country(national_data,selected_options)
        # Button to switch data view
        view_option = st.radio("Select view:", ("Chart","Table"))

        if view_option == "Table":
            # Ensure the index is named 'Years' and displayed as integers
            n_data = n_data.reset_index()
            n_data = n_data.rename(columns={n_data.columns[0]: 'Year'}) 
            n_data['Year'] = n_data['Year'].astype(str)
            st.dataframe(n_data)
        else:
            # Create and display the chart
            fig4 = px.line(n_data)
            fig4.update_layout(
                xaxis_title='Year',
                yaxis_title='Container Traffic (Thousands)'
            )
            st.plotly_chart(fig4)
    else:
        st.write("Select port to display historical freight container volume")

else:
    with open("about_app.txt", "r") as file:
        about_content = file.read()

    # Display the content using st.write
    st.header('About Content')
    st.markdown(about_content)