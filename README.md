# Software-Developer-Salary-Prediction-WebApp

A Machine Learning web application that predicts software developer salaries based on country, education, and years of experience. Built with Streamlit and trained on the Stack Overflow Developer Survey 2024 data.

## Features
- Salary prediction using Decision Tree Regressor
- Interactive data exploration and visualization
- Support for multiple countries and education levels
- Real-time predictions

## Setup Instructions

### Using Conda

#### Create conda environment

```bash
    conda create -n salary-pred python=3.12
```

#### Activate environment

```bash
    conda activate salary-pred
```

#### Install required packages

```bash
    conda install --yes --file requirements.txt          
```

### Using Pip


#### Create virtual environment

```bash
    python -m venv venv
```

#### Activate environment (Windows)

```bash
    venv\Scripts\activate
```

#### Activate environment (Linux/Mac)

```bash
    source venv/bin/activate
```
#### Install requirements

```bash
    pip install -r requirements.txt
```


### Data Setup
1. Download Stack Overflow Developer Survey 2024 data from [Stack Overflow](https://insights.stackoverflow.com/survey)
2. Create a `data` directory in the project root
3. Extract and place `survey_results_public.csv` in the `data` directory

### Running the Application

```bash
    streamlit run app.py
```

- This is a Web App deployed on streamlit cloud implemented in streamlit.
- This is a Machine learning based web app which predicts a software engineer's salary on the basis of certain inputs and a model trained on Decision tree predicts the salary 
- The dataset used was from StackOverflow developer's survey 2022
- I have also implemented some data exploration and visualization in the web App itself 
<br>
<img align=left width="48%" alt="Screenshot 2022-09-27 at 8 54 19 PM" src="https://user-images.githubusercontent.com/81188792/192568512-d5c79320-f774-4a0c-8e29-53d56d2f09c5.png">
<img width="48%" alt="Screenshot 2022-09-27 at 8 54 34 PM" src="https://user-images.githubusercontent.com/81188792/192568475-f3b261df-4cab-4b24-93ac-9aea9cc739c8.png">

<br>

check out my web app on : [Click Here](https://developer-salary-prediction.streamlit.app/)
