# create the initial variables below
smoker = 0
num_of_children = 3

# Age Factor
age = 28

# BMI Factor
bmi = 26.2

# Male vs. Female Factor
sex = 0

# Insurance Cost Formula
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print(insurance_cost)

# Let’s display this value in an informative way. Print out the following string in the terminal: This person's insurance cost is {insurance_cost} dollars.

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

#Let’s start with the age factor. Using a plus-equal operator, add 4 years to our age variable.
age = 28
age += 4
print(age)

#Now that we have changed our age value, we want to recalculate our insurance cost. Declare a new variable called new_insurance_cost underneath the expression that increased age by 4.

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print(new_insurance_cost)

# Next, we want to find the difference between our new_insurance_cost and insurance_cost. To do this, let’s create a new variable called change_in_insurance_cost and set it equal to the difference between new_insurance_cost and insurance_cost.

change_in_insurance_cost = new_insurance_cost - insurance_cost
print(change_in_insurance_cost)

print("People who are four years older have estimated insurance costs are " + str(change_in_insurance_cost) + " dollars different.")

# We want to display this information in an informative way similar to the output from instruction 3. On the next line, print the following string in the terminal, where XXX is replaced by the value of change_in_insurance_cost:

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# Set age to 28 following your last piece of code. This will reset its value and allow us to focus on just the change in the BMI factor moving forward.

age = 28

# On the next line, using the plus-equal operator, add 3.1 to our bmi variable.

bmi += 3.1

# Below the line where bmi was increased by 3.1, rewrite the insurance cost formula and assign it to the variable name new_insurance_cost.

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print(new_insurance_cost)

# Save the difference between new_insurance_cost and insurance_cost in a variable called change_in_insurance_cost

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(change_in_insurance_cost)

# Display the following string in the output terminal, where XXX is replaced by the value of change_in_insurance_cost: The change in estimated insurance cost after increasing BMI by 3.1 is XXX dollars.

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Let’s look at the effect sex has on medical insurance costs. Before we make any additional changes, first reassign your bmi variable back to its original value of 26.2. 

bmi = 26.2

# On a new line of code, reassign the value of sex to 1. A reminder that 1 identifies male individuals and 0 identifies female individuals.

sex = 1

# Rewrite the insurance cost formula and assign it to the variable name new_insurance_cost.

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# Save the difference between new_insurance_cost and insurance_cost in a variable called change_in_insurance_cost.

change_in_insurance_cost = new_insurance_cost - insurance_cost

# Display the following string in the output terminal, where XXX is replaced by the value of change_in_insurance_cost:

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")