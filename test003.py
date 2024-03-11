# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Main function to call our other functions
def main():
    # Add 5 and 3
    sum_result = add_numbers(5, 3)
    print(f"The sum of 5 and 3 is: {sum_result}")
    
    # Multiply 4 and 7
    product_result = multiply_numbers(4, 7)
    print(f"The product of 4 and 7 is: {product_result}")

# Calling the main function
if __name__ == "__main__":
    main()
