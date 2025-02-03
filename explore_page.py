import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    return categorical_map

def clean_experience(x):
    if x == "Less than 1 year":
        return 0.5
    elif x == "More than 50 years":
        return 50
    else:
        return float(x)

def clean_education(x):
    if "Bachelor's degree" in x:
        return "Bachelor's degree"
    elif "Master's degree" in x:
        return "Master's degree"
    elif "Other doctoral" in x or "Professional degree" in x:
        return "Doctorate or Professional degree"
    else:
        return "Less than Bachelor's degree"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/survey_results_public.csv")
        df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
        df = df.rename({"ConvertedCompYearly" : "Salary"}, axis = 1)
        df = df[df["Salary"].notnull()]
        df = df.dropna()
        df = df[df["Employment"] == "Employed, full-time"]
        df = df.drop("Employment",axis=1)

        country_map = shorten_categories(df["Country"].value_counts(), 400)
        df["Country"] = df["Country"].map(country_map)

        df = df[df["Salary"] <= 120000]
        df = df[df["Salary"] >= 5000]
        df = df[df["Country"] != "Other"]

        df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
        df["EdLevel"] = df["EdLevel"].apply(clean_education)

        return df
    except FileNotFoundError:
        st.error("Please download the Stack Overflow survey data and place it in the data directory")
        return None

df = load_data()

def show_explore_page():
    st.title("Explore Software Engeneering Salaries")
    st.write("""### Stack OverFlow Survey 2024""")

    data = df["Country"].value_counts()

    st.write("""#### Number of Data from different countries""")
    st.bar_chart(data)
    
    st.write("""#### Mean Salary Based On Country""")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Mean Salary Based On Experience""")
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

    st.write("""#### Mean Salary Based On Education Level""")
    data = df.groupby(["EdLevel"])["Salary"].mean().sort_values(ascending=True)
    st.area_chart(data)