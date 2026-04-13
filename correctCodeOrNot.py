def check_syntax(code):
    try:
        compile(code, "<string>", "exec")
        print("✅ Code is syntactically correct")
    except SyntaxError as e:
        print("❌ Syntax Error:")
        print(e)

# Example usage
user_code = input("Enter your Python code:\n")
check_syntax(user_code)