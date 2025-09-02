from workplace_incident_analysis import load_data, clean_data, incident_count
from visual import incidents_plot

def main():
    file_path = "data/government_of_Ireland_workplace_incidents_2017-2021.csv"

    # load data
    file = load_data(file_path)
    print(file.head(20))

    # clean loaded data
    cleaned_file = clean_data(file) 

    # counting incidents by type "Incident Type"
    count = incident_count(cleaned_file)
    
    if count is None:
        print("No incident data to plot")
    else:
        print("\nIncident Counts:")
        print(count)

        incidents_plot(count)

    
if __name__ == "__main__":
    main()