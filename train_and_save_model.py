import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load and preprocess the dataset
df = pd.read_csv('hearts.csv')
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df['ChestPainType'] = le.fit_transform(df['ChestPainType'])
df['RestingECG'] = le.fit_transform(df['RestingECG'])
df['ExerciseAngina'] = le.fit_transform(df['ExerciseAngina'])
df['ST_Slope'] = le.fit_transform(df['ST_Slope'])

X = df.drop(columns=['HeartDisease'])
y = df['HeartDisease']

# Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model properly
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully as model.pkl")
