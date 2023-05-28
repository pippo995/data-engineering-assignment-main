# Import pandas and datetime libraries
import pandas as pd
import pymongo

from datetime import datetime


def read_csv(file_path):
    
  df = pd.read_csv(file_path)
  return df


# Function to transform the data
def transform_data(df):
 
  df['BirthDate'] = pd.to_datetime(df['BirthDate']).dt.strftime('%Y-%m-%d')

  # Strip any leading/trailing spaces from FirstName and LastName columns
  df['FirstName'] = df['FirstName'].str.strip()
  df['LastName'] = df['LastName'].str.strip()

  # Merge the FirstName and LastName columns into a new column FullName
  df['FullName'] = df['FirstName'] + ' ' + df['LastName']

  # Calculate the age of each employee from the BirthDate column using Jan 1st, 2023 as reference date
  reference_date = datetime(2023, 1, 1)
  df['Age'] = (reference_date - pd.to_datetime(df['BirthDate'])).dt.days // 365

  # Add a new column SalaryBucket to categorize the employees based on their salary
  df['SalaryBucket'] = pd.cut(df['Salary'], bins=[0, 50000, 100000, float('inf')], labels=['A', 'B', 'C']).astype(str)

  # Drop columns FirstName, LastName, and BirthDate
  df.drop(columns=['FirstName', 'LastName', 'BirthDate'], inplace=True)

  return df


# Function to load the data into MongoDB
def load_data(df):
  
  client = pymongo.MongoClient('mongodb://localhost:27017/')
  db = client['employees']
  collection = db['employees']
  data = df.to_dict('records')

  collection.insert_many(data)
  collection.create_index('FullName')
  collection.create_index('SalaryBucket')



if __name__ == '__main__':
  df = read_csv('employee_details.csv')
  print(df)
  df = transform_data(df)
  load_data(df)
