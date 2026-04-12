def education_check():
    score = 0

    print("Answer the following questions:\n")

    # Question 1
    q1 = input("1. What is the capital of India? ")
    if q1.strip().lower() == "new delhi":
        score += 1

    # Question 2
    q2 = input("2. What is 5 + 7? ")
    if q2 == "12":
        score += 1

    # Question 3
    q3 = input("3. Who wrote 'Romeo and Juliet'? ")
    if "shakespeare" in q3.lower():
        score += 1

    # Result
    print("\nYour Score:", score)

    if score == 3:
        print("Result: Likely educated (based on this simple test)")
    elif score == 2:
        print("Result: Moderately educated")
    else:
        print("Result: Needs more learning (not a real judgment!)")

education_check()