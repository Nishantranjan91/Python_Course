import random

def human_or_robot():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    print(f"Prove you're human: What is {a} + {b}?")
    
    try:
        answer = int(input("Your answer: "))
        if answer == a + b:
            print("✅ You are human!")
        else:
            print("❌ You might be a robot!")
    except:
        print("❌ Invalid input. You might be a robot!")

human_or_robot()