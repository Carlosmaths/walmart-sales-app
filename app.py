import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration
st.set_page_config(
    page_title="Walmart Sales Predictor",
    page_icon="🛒",
    layout="centered"
)


# 2. Load the Model
@st.cache_resource
def load_model():
    try:
        return joblib.load('walmart_sales_model.pkl')
    except FileNotFoundError:
        st.error("⚠️ Error: File 'walmart_sales_model.pkl' not found.")
        return None


model = load_model()

# 3. Main Interface Layout
st.title("🛒 Walmart Sales Predictor")
st.markdown("### Weekly Sales Estimation Tool")
st.markdown("""
This application uses a **Random Forest Machine Learning model** with **97% accuracy** to predict weekly sales for specific departments.
Adjust the parameters in the sidebar to generate an instant prediction.
""")
st.divider()

# 4. Sidebar - User Inputs
st.sidebar.header("📊 Input Parameters")

# Inputs
dept = st.sidebar.number_input("Department ID (1-99)", min_value=1, max_value=99, value=1,
                               help="Unique identifier for the department.")
size = st.sidebar.slider("Store Size (sq ft)", 30000, 220000, 150000)
store = st.sidebar.selectbox("Store ID", range(1, 46))
week = st.sidebar.slider("Week of the Year", 1, 52, 25, help="Week 52 corresponds to Christmas.")
is_holiday = st.sidebar.checkbox("Is it a Holiday Week?", value=False)

# 5. Prediction Logic
if st.button("Predict Sales 🚀", type="primary"):
    if model is not None:
        # Create input DataFrame
        input_data = pd.DataFrame({
            'Store': [store],
            'Dept': [dept],
            'Size': [size],
            'Week': [week],
            'IsHoliday': [is_holiday],

            # --- Default Values (Historical Averages) ---
            'Type': [1],
            'Temperature': [60.0],
            'Fuel_Price': [3.40],
            'MarkDown1': [0.0],
            'MarkDown2': [0.0],
            'MarkDown3': [0.0],
            'MarkDown4': [0.0],
            'MarkDown5': [0.0],
            'CPI': [171.0],
            'Unemployment': [8.0],
            'Year': [2012],
            'Month': [6]
        })

        # Generate Prediction
        prediction = model.predict(input_data)[0]

        # 6. Display Results
        st.subheader("Analysis Results:")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="Estimated Weekly Sales", value=f"${prediction:,.2f}")

        with col2:
            if prediction > 20000:
                st.success("💰 Performance: HIGH")
            elif prediction > 5000:
                st.warning("⚖️ Performance: AVERAGE")
            else:
                st.error("📉 Performance: LOW")

        # Celebration effect
        if prediction > 25000:
            st.balloons()