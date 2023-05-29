# Import pandas and datetime libraries
import pandas as pd
import pymongo

from datetime import datetime


def read_csv(file_path):
    
  df = pd.read_csv(file_path)
  return df


# Function to transform the data
def transform_data(df):

  df['BirthDate'] = pd.to_datetime(df['BirthDate'], errors='coerce').dt.strftime('%Y-%m-%d')

  # Strip any leading/trailing spaces and and any non alphabetic character
  df['FirstName'] = df['FirstName'].str.replace('[^a-zA-Z\s]', '', regex=True)
  df['FirstName'] = df['FirstName'].str.replace('^\s+|\s+$', '', regex=True)
  df['FirstName'] = df['FirstName'].str.replace('\s+', ' ', regex=True)

  df = df.rename(columns={"  LastName  ": "LastName"})
  df['LastName'] = df['LastName'].str.replace('[^a-zA-Z\s]', '', regex=True)
  df['LastName'] = df['LastName'].str.replace('^\s+|\s+$', '', regex=True)
  df['LastName'] = df['LastName'].str.replace('\s+', ' ', regex=True)

  df['Department'] = df['Department'].str.replace('^\s+|\s+$', '', regex=True)
  
  # Merge the FirstName and LastName columns into a new column FullName
  df['FullName'] = df['FirstName'] + ' ' + df['LastName']

  # Calculate the age of each employee from the BirthDate column using Jan 1st, 2023 as reference date
  reference_date = datetime(2023, 1, 1)
  df['Age'] = (reference_date - pd.to_datetime(df['BirthDate'], errors='coerce')).dt.days // 365

  df = df.dropna()
  df = df.drop(df.index[df['Age'] < 0])

  # Add a new column SalaryBucket to categorize the employees based on their salary

  df['Salary'] = df['Salary'].str.replace('[^0-9]', '', regex=True)
  df['Salary'] = abs(df['Salary'].astype(int))
  df['SalaryBucket'] = pd.cut(df['Salary'], bins=[0, 50000, 100000, float('inf')], labels=['A', 'B', 'C']).astype(str)

  # Drop columns FirstName, LastName, and BirthDate
  df.drop(columns=['FirstName', 'LastName', 'BirthDate'], inplace=True)
  
  return df


# Function to load the data into MongoDB
def load_data(df):
  
  try:
  # code that may raise an exception
    client = pymongo.MongoClient('mongodb://mongodb:27017/')
    db = client['employees']
    collection = db['employees']
    data = df.to_dict('records')
    
    print(data)

    collection.insert_many(data)
    collection.create_index('FullName')
    collection.create_index('SalaryBucket')
  except Exception as e:
  # code that handles the exception
    print("An error on Mongo occurred:", e)



if __name__ == '__main__':
  df = read_csv('employee_details.csv')
  df = transform_data(df)
  load_data(df)
