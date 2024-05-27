import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("india.csv")

list_of_states = list(df["State"].unique())
list_of_states.insert(0, "Overall India")

st.set_page_config(layout="wide")

st.sidebar.title("India Census Data Visualization")
selected_state = st.sidebar.selectbox("Select a State", list_of_states)
primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter", sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text('Size Represents primary paramter')
    st.text('Color Represents secondary paramter')
    if selected_state == "Overall India":
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            zoom=3,
            mapbox_style="carto-positron",
            size=primary,
            size_max=35,
            color=secondary,
            width=1200,
            height=700,
            color_continuous_scale="agsunset",
            hover_name="District",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df["State"] == selected_state]
        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            zoom=3,
            mapbox_style="carto-positron",
            size=primary,
            size_max=35,
            color=secondary,
            width=1200,
            height=700,
            color_continuous_scale="agsunset",
            hover_name="District",
        )
        st.plotly_chart(fig, use_container_width=True)
        pass
