import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'Age': 50,
    'Sex': 1,
    'ChestPainType': 0,
    'RestingBP': 120,
    'Cholesterol': 200,
    'FastingBS': 0,
    'RestingECG': 1,
    'MaxHR': 150,
    'ExerciseAngina': 0,
    'Oldpeak': 1.0,
    'ST_Slope': 2
}
headers = {'X-Requested-With': 'curl'}
response = requests.post(url, data=data, headers=headers)
print(response.text)
