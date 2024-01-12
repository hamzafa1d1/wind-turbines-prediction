import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
import tensorflow as tf

# Function to calculate energy based on the selected date
# Function to load the pre-trained model
def load_model(model_path):
    return tf.keras.models.load_model(model_path)
def create_features(selected_date):
    features = {
        'dayofweek': selected_date.dayofweek,
        'quarter': selected_date.quarter,
        'month': selected_date.month,
        'year': selected_date.year,
        'dayofyear': selected_date.dayofyear,
        'dayofmonth': selected_date.day,
        'weekofyear': selected_date.isocalendar().week
    }
    return features
def calculate_energy(selected_date, model):
    features = create_features(selected_date)

    # model.predict()
    time.sleep(2)  # Simulating a delay for energy calculation
    return f"Energy calculated for {selected_date} is 100 kWh"

# Streamlit app
def main():
    st.title("Energy Calculator App ⚡🍃")

    # Image
    # st.image("wind-turbine.jpg", caption="Wind Turbine", use_column_width=True)

    # Date selection
    selected_date = st.date_input("Select a date", datetime.date.today())

    model_path = "modelTs.h5"  # Replace with the actual path to your H5 file
    model = load_model(model_path)


    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )


    # Calculate energy button
    if st.button("Calculate Energy"):
        # Display loading bar while calculating energy
        with st.spinner("Calculating energy..."):
            # Call the function to calculate energy
            result = calculate_energy(selected_date, model)
            # Simulate delay for loading bar effect
            time.sleep(1)

            # Display the result
            st.success(result)

    st.area_chart(chart_data, x="col1", y="col2", color="col3")
if __name__ == "__main__":
    main()
