import streamlit as st
import requests

st.title("Employee Attrition Prediction")

# Input fields for all features
age = st.number_input("Age", min_value=18, max_value=65)
business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
daily_rate = st.number_input("Daily Rate")
department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
distance = st.number_input("Distance From Home")
education = st.selectbox("Education", [1, 2, 3, 4, 5])
education_field = st.selectbox("Education Field", ["Life Sciences", "Other", "Medical", "Marketing", "Technical Degree", "Human Resources"])
env_satisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
gender = st.selectbox("Gender", ['Male', 'Female'])
hourly_rate = st.number_input("Hourly Rate")
job_involvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
job_role = st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
monthly_income = st.number_input("Monthly Income")
monthly_rate = st.number_input("Monthly Rate")
num_companies_worked = st.number_input("Num Companies Worked", min_value=0)
overtime = st.selectbox("OverTime", ["Yes", "No"])
percent_salary_hike = st.number_input("Percent Salary Hike")
performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])
relationship_satisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
total_working_years = st.number_input("Total Working Years")
training_times_last_year = st.number_input("Training Times Last Year")
work_life_balance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
years_at_company = st.number_input("Years At Company")
years_in_current_role = st.number_input("Years In Current Role")
years_since_last_promotion = st.number_input("Years Since Last Promotion")
years_with_curr_manager = st.number_input("Years With Curr Manager")

# Prepare payload
payload = {
    "Age": age,
    "BusinessTravel": business_travel,
    "DailyRate": daily_rate,
    "Department": department,
    "DistanceFromHome": distance,
    "Education": education,
    "EducationField": education_field,
    "EnvironmentSatisfaction": env_satisfaction,
    "Gender": 1 if gender == "Male" else 0,
    "HourlyRate": hourly_rate,
    "JobInvolvement": job_involvement,
    "JobLevel": job_level,
    "JobRole": job_role,
    "JobSatisfaction": job_satisfaction,
    "MaritalStatus": marital_status,
    "MonthlyIncome": monthly_income,
    "MonthlyRate": monthly_rate,
    "NumCompaniesWorked": num_companies_worked,
    "OverTime": 1 if overtime == "Yes" else 0,
    "PercentSalaryHike": percent_salary_hike,
    "PerformanceRating": performance_rating,
    "RelationshipSatisfaction": relationship_satisfaction,
    "StockOptionLevel": stock_option_level,
    "TotalWorkingYears": total_working_years,
    "TrainingTimesLastYear": training_times_last_year,
    "WorkLifeBalance": work_life_balance,
    "YearsAtCompany": years_at_company,
    "YearsInCurrentRole": years_in_current_role,
    "YearsSinceLastPromotion": years_since_last_promotion,
    "YearsWithCurrManager": years_with_curr_manager
}

# Call the FastAPI backend
if st.button("Predict Attrition"):
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Attrition Prediction: {'Yes' if prediction == 1 else 'No'}")
    else:
        st.error("Failed to get prediction")
