import pandas as pd

# Loads CSV file into pandas data frame
def load_data(file_path):
  
  if file_path is None:
    print("File not found")
    return None

  return pd.read_csv(file_path)


# Strips spaces from columns and removes rows with missing "Incident Type"
def clean_data(file):

  if file is None:
    return None
  
  # strip spaces from columns
  file.columns = file.columns.str.strip()

  cleaned_file = file.dropna(subset=["Incident Type"])

  return cleaned_file


# Uses the cleaned data to count number of incidents per type
def incident_count(file):

  if file is None or "Incident Type" not in file.columns:
    return None
  
  return file["Incident Type"].value_counts()