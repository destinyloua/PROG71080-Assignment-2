from calculations import add, subtract, multiply, divide

if __name__ == "__main__": 
    """Applies simple math operations to 2 defined variables then prints the results"""
    a = 5
    b = 10
    
    # simple math functions
    sum = add(a,b)
    difference = subtract(a, b)
    product = multiply(a, b)
    quotient = divide(b, a)

    # print input and output 
    print(f"{a} + {b} = {sum}")
    print(f"{a} - {b} = {difference}")
    print(f"{a} * {b} = {product}")
    print(f"{a} / {b} = {quotient}")

    # invokes a value error
    divide(a, 0)