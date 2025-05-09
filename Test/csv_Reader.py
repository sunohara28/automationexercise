import csv

accountData = "../Data/accountInfo.csv"
contactUsData = "../Data/contactus.csv"
searchProductData_viaName = "../Data/searchProduct_viaName.csv"
searchProductData_viaIndex = "../Data/searchProduct_viaIndex.csv"

def csvReader(csvData_path):
    data = []
    with open(csvData_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return data