import pandas as pan

# Loads CSV file into pandas data frame
def load_data(file_path):
  
  return pan.read_csv(file_path)


# Removes rows with missing "Incident_Type"
def clean_data(file):
  print (file.columns)
  #return file.dropna(subset=["Incident_Type"])

# Uses the cleaned data to count number of incidents per type
def incident_count(file):
  
  return file["Incident_Type"]