def is_arithmetic(seq):
    if len(seq) < 2:
        return True
    
    diff = seq[1] - seq[0]
    
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return False
    
    return True

# Example
seq = list(map(int, input("Enter numbers separated by space: ").split()))

if is_arithmetic(seq):
    print("✅ Arithmetic pattern")
else:
    print("❌ Not an arithmetic pattern")