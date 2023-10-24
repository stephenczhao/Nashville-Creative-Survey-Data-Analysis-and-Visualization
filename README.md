# Creative Community Survey Data Analysis & Visualization
This repository contains the efforts of our team to analyze and visualize the data collected from a survey conducted on the creative community in Nashville. Our primary objective was to deliver insights and a graphical user interface for better understanding and decision-making by the non-profit organization. 

## Table of Contents
- [Introduction to the Data](#introduction-to-the-data)
- [Steps Taken](#steps-taken)
  - [Data Cleaning and Preparation](#data-cleaning-and-preparation)
  - [Data Analysis](#data-analysis)
  - [User Interface Development](#user-interface-development)
- [Project Structure](#project-structure)
- [Instructions for Setup and Execution](#instructions-for-setup-and-execution)

## Introduction to the Data
The dataset encompasses responses from different roles in the creative industry of Nashville, including:
- **Creative Entrepreneurs**
- **Creative Workers**
- **Arts Administrators**
- **Arts Educators or Teaching Artists**
- **Arts Funders**
- **Business Professionals**
- **Civic and/or Social Service Workers**

Each role has its specific set of questions, with some questions being common across multiple roles.

## Steps Taken

### Data Cleaning and Preparation
We started our project by initially cleaning the dataset to ensure accuracy and comprehensibility. This involved:
* Handling missing values
* Correcting data inconsistencies by normalizing responses into comparable, numerical values
* Rephrasing certain responses to questions that are unnecessarily long for Exploratory Data Analysis

### Data Analysis
Our team dived deep into the data using Jupyter Notebooks, answering various insightful questions that help inform the non-profit organization about:
* The demographics of the respondents.
* The barriers faced by different roles.
* The needs and aspirations of the creative community.
* The potential directions the non-profit organization can invest in.

### User Interface Development
For a broader audience, we developed an interactive user interface using Streamlit that allows any individual, even non-technical ones, to explore the data visually. The UI focuses on delivering key insights about:
* The demographics.
* The challenges and needs of **Creative Entrepreneurs**.
* Barriers faced by the community.
* Space needs of various roles.

## Project Structure
- `app.py`: Contains the Streamlit app for the user interface.
- `requirements.txt`: Lists all the necessary packages and libraries required to run the app and notebooks.
- `Jupyter Notebooks`: Five separate notebooks detailing different analyses.
- `.devcontainer`: Contains configuration for creating a replicable development environment.
- `ReadMe.md`: This file you're currently reading.

## Instructions for Setup and Execution
1. Clone this repository to your local machine.
2. Set up a virtual environment (optional but recommended).
3. Install the necessary packages using:
   ```bash
   pip install -r requirements.txt
4. Run the Streamlit app using:
   ```bash
   streamlit run app.py
5. Open the Jupyter Notebooks to explore the analysis. Each notebook is numbered and named according to its primary focus. 
