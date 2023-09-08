def process_input():
    try:
        value1 = input("Enter the first value: ")
        value2 = input("Enter the second value: ")
        
        try:
            num1 = float(value1)
            num2 = float(value2)
            
            result = num1 + num2
            print("Sum:", result)
        except ValueError:
            result = value1 + value2
            print("Concatenation result:", result)
    
    except KeyboardInterrupt:
        print("Canceled by the user")
    except Exception as e:
        print("An error occurred:", str(e))

process_input()
