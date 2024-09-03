import csv
import os
print("Current Working Directory:", os.getcwd())

# In my Python file I create empty lists for the various attributes in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# Helper function to load csv data

def load_list_data(list, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv
        for row in csv_dict:
            list.append(row[column_name])
        return list


# look at the data in insurance_csv_dict
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

class PatientsInfo:
    # init method that takes in each list parameter
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    # method that calculates the average ages of the patients in insurance.csv
    def analyze_ages(self):
        # initialize total age at zero
        total_age = 0
        # iterate through all ages in the ages list
        for age in self.patients_ages:
            # sum of the total age
            total_age += int(age)

        # Calculate the average age
        average_age = round(total_age/len(self.patients_ages), 2)

        # return total age divided by the length of the patient list
        return (f"Average Patient Age: {average_age} years")
    
    # method that calculates the number of males and females in insurance.csv
    def analyze_sexes(self):
        # initialize total of both sexes at zero
        males = 0
        females = 0
        # iterate through all the sexes in the sexes list
        for sex in self.patients_sexes:
            # sum of total for each
            if sex == 'males':
                males += 1
            elif sex == ' females':
                females += 1
          # print out the number of each
        print("Count for female: ", females)
        print("Count for male: ", males)

    # method to find each unique region patients are from
    def unique_regions(self):
        # initialize empty list
        unique_regions = []
        # iterate through each region in regions list
        for region in self.patients_regions:
            # if the region is not already in the unique regions list
            # then add it to the unique regions list
            if region not in unique_regions: 
                unique_regions.append(region)
        # return unique regions list
        return unique_regions

    # method to find average yearly medical charges for patients in insurance.csv
    def average_charges(self):
        # initialize total_charges variable
        total_charges = 0
        # iterate through charges in patients charges list
        # add each charge to total_charge
        for charge in self.patients_charges:
            total_charges += float(charge)

        # calculate the average charges
        average_charge = round(total_charges/len(self.patients_charges), 2)
        # return the average charges rounded to the hundredths place
        return (f"Average Yearly Medical Insurance Charges: {average_charge} dollars.")
    
    # method to create dictionary with all patients information
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary
    
# Create an instance of the class named 'patient_info'. 
# Use this instance to call each method and view the analysis results.

patients_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

print(patients_info.analyze_ages())
print(patients_info.analyze_sexes())
print(patients_info.unique_regions())
print(patients_info.average_charges())
# print(patients_info.create_dictionary())