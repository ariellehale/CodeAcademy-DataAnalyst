# Arielle Hale | May 14, 2021

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

# Append a new individual, "Priscilla", to names.
names.append("Priscilla")

# Append her insurance cost, 8320.0, to insurance_costs.
insurance_costs.append(8320.0)

#Create a new variable called medical_records that combines insurance_costs and names into a list using the zip() function
medical_records = list(zip(insurance_costs, names))

# Print out medical_records in the terminal, and make sure the output is what you expected.
print(medical_records)

# Create a variable called num_medical_records that stores the length of medical_records.
num_medical_records = len(medical_records)

# Print num_medical_records with the following message: There are {number of medical records} medical records.
print(num_medical_records)

# Select the first medical record in medical_records, and save it to a variable called first_medical_record.
first_medical_record = medical_records[0]

# Print first_medical_record with the following message: Here is the first medical record: {first medical record}
print("Here is the first medical record: " + str(first_medical_record))

# Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list.
medical_records.sort()

# Print the sorted medical_records with the following message: Here are the medical records sorted by insurance cost: {sorted list}
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

# Slice the medical_records list, and store the three cheapest insurance costs in a list called cheapest_three.
cheapest_three = medical_records[:3]

# Print cheapest_three with the following message: Here are the three cheapest insurance costs in our medical records: {cheapest three}
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# Slice the medical_records list, and store the three most expensive insurance costs in a list called priciest_three.
priciest_three = medical_records[-3:]

# Print priciest_three with the following message: Here are the three most expensive insurance costs in our medical records: {priciest three}
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

# Count the number of occurrences of “Paul” in the names list, and store the result in a variable called occurrences_paul.
occurences_paul = names.count("Paul")

# Print occurrences_paul with the following message: There are {occurrences Paul} individuals with the name Paul in our medical records.
print("There are " + str(occurences_paul) + " individuals with the name Paul in our medical records.")