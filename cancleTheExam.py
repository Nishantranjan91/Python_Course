# Input data
total_exams = int(input("Enter total number of exams conducted: "))
cancelled_exams = int(input("Enter number of exams cancelled due to corruption: "))

# Calculate probability
if total_exams > 0:
    probability = cancelled_exams / total_exams
    print("Probability of exam cancellation due to corruption:", probability)
else:
    print("Total exams must be greater than 0")