# Probability of getting sum = 7 with two dice

total_outcomes = 6 * 6
favorable_outcomes = 0

for dice1 in range(1, 7):
    for dice2 in range(1, 7):
        if dice1 + dice2 == 7:
            favorable_outcomes += 1

probability = favorable_outcomes / total_outcomes

print("Favorable outcomes:", favorable_outcomes)
print("Total outcomes:", total_outcomes)
print("Probability of getting sum 7:", probability)