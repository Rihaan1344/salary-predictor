import streamlit as st
import joblib 
from pandas import DataFrame

model = joblib.load("salary_predictor.joblib")

with st.form("get_input"):
    job_title = st.selectbox("What's your desired job title?",
                             options = ['AI Engineer', 'Data Analyst',
                                        'Frontend Developer',          'Business Analyst',
                                        'Product Manager',         'Backend Developer',
                                        'Machine Learning Engineer',           'DevOps Engineer',
                                        'Software Engineer',     'Cybersecurity Analyst',
                                        'Data Scientist',            'Cloud Engineer'])
    
    education_level = st.selectbox("What level of education do you have?", options = ["High School", "Diploma", "Bachelor", "Master", "PhD"])
    
    industry = st.selectbox("Which industry do you want to work in?", 
                            options = ['Healthcare',       'Telecom',         'Media',        'Retail',
                                        'Manufacturing',     'Education',       'Finance',    'Technology',
                                        'Consulting',    'Government'])
    
    company_size = st.selectbox("What would you say is the size of the company you wish to work in?", options = ['Startup', 'Small', 'Medium', 'Large', 'Enterprise'])

    location = st.selectbox("Where would you be working?", 
                            options = ['India',   'Australia',   'Singapore',      'Canada',      'Sweden',
                                        'USA', 'Netherlands',      'Remote',     'Germany',          'UK'])
    
    remote_work = st.selectbox("Would you have the freedom for remote work?", options = ["Yes", "No", "Hybrid"])

    experience_years = st.select_slider("How many years of experience do you have?",
                                        options = list(range(0, 21)))
    
    skills_count = st.select_slider("How many 'skills' would you say you possess? Eg, Docker, Jenkins, Scikit-learn, etc...", 
                                    options = sorted([ 2, 17,  4, 13,  7, 16, 18, 14, 10,  3,  5,  9,  1, 12, 15,  8, 19,
       11,  6]))
    
    certifications = st.select_slider("How many official certifications do you possess?", options = list(range(0, 6)))
   
    submitted = st.form_submit_button(label = "Have my model calculate your predicted salary!") 
if submitted:
    info = DataFrame([[job_title, experience_years, education_level, skills_count,
                    industry, company_size, location, remote_work,
                    certifications]], 
                    columns=['job_title', 'experience_years', 'education_level', 'skills_count',
                    'industry', 'company_size', 'location', 'remote_work',
                    'certifications'],
                    index = [0])
    salary = model.predict(info)
    st.write(salary)