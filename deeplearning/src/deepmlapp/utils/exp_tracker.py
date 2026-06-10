import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import mlflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from deepmlapp.configurations.conf import LOAN_FILE_PATH
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

file_path = LOAN_FILE_PATH

data = pd.read_csv(file_path)
print("Dataset loaded successfully!")

# Convert categorical variables to numerical using one-hot encoding
    #label encoding for loan_status
data['LoanStatus'] = data['LoanStatus'].map({'Rejected': 0, 'Approved': 1})
    #identify x and y
x=data.drop(['LoanStatus','ApplicantID'],axis=1)
y=data['LoanStatus']

#apply standard scalar
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
y_scaled=y.values
#create ml flow experiment
with mlflow.start_run():
    mlflow.log_param("model_type", "simple_nn")
    mlflow.log_param("epochs", 10)
    mlflow.log_param("batch_size", 32)
    
    #build a simple nn model tensor flow with keras
    model=tf.keras.Sequential([
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x_scaled, y_scaled, epochs=10, batch_size=32)
    
    #evaluate the model
    loss, accuracy = model.evaluate(x_scaled, y_scaled)
    print(f"Loss: {loss}, Accuracy: {accuracy}")
    
    mlflow.log_metric("loss", loss)
    mlflow.log_metric("accuracy", accuracy)



