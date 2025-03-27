import csv

accountData = "../Data/accountInfo.csv"
contactUsData = "../Data/contactus.csv"

def csvReader(csvData_path):
    data = []
    with open(csvData_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return data