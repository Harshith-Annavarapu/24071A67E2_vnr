def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input("Enter a +ve integer:"))
b = int(input("Enter a +ve integer:"))

print(f"GCD of {a} and {b} is {gcd(a, b)}")
print(f"LCM of {a} and {b} is {lcm(a, b)}")