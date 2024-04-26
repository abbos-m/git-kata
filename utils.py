import pandas as pd
def load_female_passengers(file_path):
   
    # Load the Titanic dataset into a DataFrame
    titanic_data = pd.read_csv(file_path)
    
    # Filter only the female passengers
    female_passengers = titanic_data[titanic_data['sex'] == 'female']
    
    return female_passengers

from utils import load_female_passengers

# Assuming the Titanic dataset file is named 'titanic.csv' and is located in the same directory
file_path = 'titanic.csv'

# Call the function to load female passengers
female_passengers = load_female_passengers(file_path)

# Now you can work with the female_passengers DataFrame as needed
print(female_passengers.head())  # Display the first