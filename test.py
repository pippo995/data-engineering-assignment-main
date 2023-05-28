import unittest
import os
import pandas as pd

from etl import read_csv, transform_data, load_data


class TestCode(unittest.TestCase):

  def setUp(self):

    # Create a test csv file with some employee data
    with open('test.csv', 'w') as file:
      file.write('FirstName,LastName,BirthDate,Salary\n')
      file.write('     Alice,Smith,1990-01-01,45000\n')
      file.write('Bob    , Jones ,1985-05-15,75000\n')
      file.write('Charlie,Brown,1975-12-25,120000\n')

    # Create a test dataframe with the expected transformed data
    self.expected_df = pd.DataFrame({
      'Salary': [45000, 75000, 120000],
      'FullName': ['Alice Smith', 'Bob Jones', 'Charlie Brown'],
      'Age': [33, 37, 47],
      'SalaryBucket': ['A', 'B', 'C']
    })

    print(self.expected_df)

  
  def tearDown(self):
    os.remove('test.csv')

  
  def test_read_csv(self):
    
    df = read_csv('test.csv')
    
    self.assertIsNotNone(df)
    self.assertEqual(df.shape, (3, 4))
    self.assertListEqual(list(df.columns), ['FirstName', 'LastName', 'BirthDate', 'Salary'])

  
  def test_transform_data(self):

    df = read_csv('test.csv')
    df = transform_data(df)
    
    self.assertIsNotNone(df)
    self.assertEqual(df.shape, (3, 4))
    self.assertListEqual(list(df.columns), ['Salary', 'FullName', 'Age', 'SalaryBucket'])
    
    pd.testing.assert_frame_equal(df, self.expected_df)


if __name__ == '__main__':
    unittest.main()
