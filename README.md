# Macro Project
 
---

### Author : Redoti Zulfikar Sasongko 

### Mentee assignment from IBM Advance AI @ Inifite Learning Macro Project
---

#### Mentee Information
Name : Redoti Zulfikar Sasongko

Program : IBM Advance AI

Mentor Group 16 : Cindy Febriani 

Tech Stack:
- Python

Library
- pandas
- plotly
- scikit learn
- imblearn

Machine Learning Algorithm 
- kNN
---

# How to run streamlit prototype

### Environment Setup

Install fundamental environments including conda, python and the rest of package
 
### Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)

```javascripts
https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html
```

### Download Source Code

Open your terminal and run the following command or just download the `zip file`.
```javascripts
git clone https://github.com/redoti/stunting-classification.git
```

### Create new python environment 

#### Run this command inside anaconda prompt

```javascripts
conda create -n stunting python=3.10.12
```

#### Activate our new environment

```javascripts
conda activate stunting
```

# Deploy the Source Code 
Before running anything, you'll need to install the python library package. Make sure your terminal active on project directory
```javascripts
pip install -r requirements.txt
```
### Running the interface locally
Run on `development environment` if you want to deploy the source code directly to the `development server`. Navigate to [http://192.168.1.207:8501] or any IP that displayed on your terminal.
```javascripts
streamlit run App.py
```
