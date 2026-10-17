# Compare three integers and demonstrate De Morgan's Law.
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# A chained comparison requires both neighboring comparisons to be true.
expression1 = a < b < c
expression2 = not (a > b or b > c)
# Negating an OR changes it to AND and negates each comparison.
expression3 = a <= b and b <= c

print("a < b < c            :", expression1)
print("not (a > b or b > c) :", expression2)
print("a <= b and b <= c    :", expression3)

if expression2 == expression3:
    print("De Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("Expressions 2 and 3 do not match.")
