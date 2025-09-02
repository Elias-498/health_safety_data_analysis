from workplace_incident_analysis import load_data, clean_data, incident_count
from visual import incidents_plot

def main():
    file_path = "data/government_of_Ireland_workplace_incidents_2017-2021.csv"

    # load data
    file = load_data(file_path)
    print(file.head(8))

    # clean loaded data
    file_clean = clean_data(file)

if __name__ == "__main__":
    main()
