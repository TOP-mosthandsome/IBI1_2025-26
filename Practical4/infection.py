# Set the total class size.
class_size = 91
# Set the initial number of infected students.
infected = 5
# Set the daily growth rate.
growth_rate = 0.40
# Set the number of days passed to zero (initial).
days_passed = 0
# Display the number of infected students at the start.
print("Day", days_passed, ":", infected, "students infected")
# While the number of infected students is less than the class size:
# Increase the number of days passed by one.
# Calculate the new number of infected students using the growth rate.
# Display the day number and the number of infected students.
while infected < class_size:
    days_passed = days_passed + 1
    infected = infected * (1 + growth_rate)
    print("Day", days_passed, ":", infected, "students infected")
# When the loop stops, display the total number of days taken to infect the whole class.
print("It took", days_passed, "days after the start to infect the whole class.")
print("If the starting value is counted as day 1, this is day", days_passed + 1, "of the display.")
