# title: "🫀 Heart Disease Prediction App"

# badges:
  - "![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)"
  - "![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)"
  - "![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)"
  - "![Render](https://img.shields.io/badge/Deployed%20on-Render-green?logo=render)"
---
# live_demo:
- text: "🚀 Click here to try the app"
- url: "https://heart-diseae-prediction.onrender.com/"

---

# description: >
  A Machine Learning web app built with Flask and deployed on Render.
  It predicts whether a person has heart disease based on medical input parameters.
  

# project_structure: |
  - heart_diseae_ml/
  - ├── app.py             # Flask app
  - ├── model.pkl          # Trained ML model
  - ├── requirements.txt   # Dependencies
  - ├── Procfile           # Deployment process
  - ├── README.md          # Project documentation
  - ├── templates/         # HTML files
  - └── static/            # CSS/JS files

  ---

# tech_stack:
  - "🐍 Python 3.9"
  - "🌐 Flask"
  - "📊 scikit-learn"
  - "⚡ Gunicorn"
  - "☁️ Render"
    
---
# setup:
  - clone: "git clone https://github.com/Vaishnavirajulu21/heart_diseae_ml.git"
  - commands:
    - cd heart_diseae_ml
    - pip install -r requirements.txt
    - python app.py
  - run_local: "http://127.0.0.1:5000/"

    ---

# deployment:
 - platform: ☁️ Render
 - start_command: web: gunicorn app:app
 - repo: https://github.com/Vaishnavirajulu21/heart_diseae_ml
 -  live_link: https://your-app-name.onrender.com

---

# author:
  - name: 👩‍💻 Vaishnavi V
  - role: 📌 Machine Learning Engineer | Data Analyst | Data scientist
