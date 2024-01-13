import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
import tensorflow as tf

# Function to calculate energy based on the selected date
# Function to load the pre-trained model

def calculate_energy(selected_date):
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

    # model_path = r"/modelTs.h5"  # Replace with the actual path to your H5 file
    # model = load_model(model_path)
    days = pd.date_range(datetime.date.today(), periods=20, freq='D')
    energy_produced = np.random.uniform(2500, 4500, 20)
    chart_data = pd.DataFrame({
        "Time": days,
        "Energy Produced in KWH": energy_produced,
    })

    # Calculate energy button
    if st.button("Calculate Energy"):
        # Display loading bar while calculating energy
        with st.spinner("Calculating energy..."):
            # Call the function to calculate energy
            result = calculate_energy(selected_date)
            # Simulate delay for loading bar effect
            time.sleep(1)
            st.line_chart(chart_data, x="Time", y="Energy Produced in KWH")
            # Display the result
            # st.success(result)


if __name__ == "__main__":
    main()
