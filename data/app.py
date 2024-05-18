import streamlit as st

st.title("Sales Forecasting Dashboard")

# Example data visualization
import pandas as pd
import numpy as np

# Create a dataframe
data = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2023', periods=10),
    'Sales': np.random.randint(100, 500, size=10)
})

# Display the dataframe
st.write(data)

# Line chart of sales
st.line_chart(data.set_index('Date'))

