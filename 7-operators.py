#types of operators in python 

# ============================================================
#                 PYTHON OPERATORS
# ============================================================


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

print("\n========== ARITHMETIC OPERATORS ==========")

a = 20
b = 6

print("Addition (+):", a + b)
# Adds two numbers
# 20 + 6 = 26

print("Subtraction (-):", a - b)
# Subtracts b from a
# 20 - 6 = 14

print("Multiplication (*):", a * b)
# Multiplies two numbers
# 20 * 6 = 120

print("Division (/):", a / b)
# Normal division
# 20 / 6 = 3.333...

print("Floor Division (//):", a // b)
# Gives the quotient without decimal part
# 20 // 6 = 3

print("Modulus (%):", a % b)
# Gives the remainder
# 20 % 6 = 2

print("Exponentiation (**):", a ** b)
# Raises a to the power of b
# 20 ** 6 = 64000000



# ============================================================
# 2. RELATIONAL / COMPARISON OPERATORS
# ============================================================

print("\n========== RELATIONAL / COMPARISON OPERATORS ==========")

a = 50
b = 30

print("Greater than (>):", a > b)
# Checks if a is greater than b
# 50 > 30 → True

print("Less than (<):", a < b)
# Checks if a is less than b
# 50 < 30 → False

print("Greater than or equal to (>=):", a >= b)
# Checks if a is greater than or equal to b
# 50 >= 30 → True

print("Less than or equal to (<=):", a <= b)
# Checks if a is less than or equal to b
# 50 <= 30 → False

print("Equal to (==):", a == b)
# Checks if a and b are equal
# 50 == 30 → False

print("Not equal to (!=):", a != b)
# Checks if a and b are different
# 50 != 30 → True



# ============================================================
# 3. ASSIGNMENT OPERATORS
# ============================================================

print("\n========== ASSIGNMENT OPERATORS ==========")

# -------------------- = --------------------

x = 10
print("Assignment (=):", x)
# Assigns 10 to x
# x = 10


# -------------------- += --------------------

x = 10
x += 5
print("Add and assign (+=):", x)
# Same as: x = x + 5
# 10 + 5 = 15


# -------------------- -= --------------------

x = 10
x -= 5
print("Subtract and assign (-=):", x)
# Same as: x = x - 5
# 10 - 5 = 5


# -------------------- *= --------------------

x = 10
x *= 5
print("Multiply and assign (*=):", x)
# Same as: x = x * 5
# 10 × 5 = 50


# -------------------- /= --------------------

x = 10
x /= 5
print("Divide and assign (/=):", x)
# Same as: x = x / 5
# Result = 2.0


# -------------------- //= --------------------

x = 10
x //= 3
print("Floor divide and assign (//=):", x)
# Same as: x = x // 3
# Result = 3


# -------------------- %= --------------------

x = 10
x %= 3
print("Modulus and assign (%=):", x)
# Same as: x = x % 3
# Result = 1


# -------------------- **= --------------------

x = 2
x **= 3
print("Exponent and assign (**=):", x)
# Same as: x = x ** 3
# 2³ = 8



# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================

print("\n========== LOGICAL OPERATORS ==========")

a = 50
b = 30


# -------------------- AND --------------------

val1 = True
val2 = True

print("AND (True and True):", val1 and val2)
# AND gives True only when BOTH conditions are True


print("AND example:", (a > b) and (a == 50))
# 50 > 30 → True
# 50 == 50 → True
# True and True → True


# -------------------- OR --------------------

print("OR example:", (a == b) or (a > b))
# 50 == 30 → False
# 50 > 30 → True
# False or True → True


# -------------------- NOT --------------------

print("NOT example:", not False)
# NOT reverses the Boolean value
# not False → True


print("NOT comparison:", not (a > b))
# a > b → True
# not True → False



# ============================================================
# 5. OTHER OPERATORS
# ============================================================

print("\n========== OTHER OPERATORS ==========")


# ============================================================
# 5.1 BITWISE OPERATORS
# ============================================================

print("\n----- BITWISE OPERATORS -----")

a = 5
b = 3

print("Bitwise AND (&):", a & b)
# 5 = 101
# 3 = 011
#     ---
#     001
# Result = 1


print("Bitwise OR (|):", a | b)
# 101
# 011
# ---
# 111
# Result = 7


print("Bitwise XOR (^):", a ^ b)
# 101
# 011
# ---
# 110
# Result = 6


print("Bitwise NOT (~):", ~a)
# ~5 = -6


print("Left Shift (<<):", a << 1)
# 5 << 1
# Shifts bits one position to the left
# Result = 10


print("Right Shift (>>):", a >> 1)
# 5 >> 1
# Shifts bits one position to the right
# Result = 2



# ============================================================
# 5.2 MEMBERSHIP OPERATORS
# ============================================================

print("\n----- MEMBERSHIP OPERATORS -----")

numbers = [10, 20, 30, 40]

print("20 in numbers:", 20 in numbers)
# Checks whether 20 exists in the list
# True


print("50 in numbers:", 50 in numbers)
# Checks whether 50 exists in the list
# False


print("50 not in numbers:", 50 not in numbers)
# Checks whether 50 does NOT exist in the list
# True



# ============================================================
# 5.3 IDENTITY OPERATORS
# ============================================================

print("\n----- IDENTITY OPERATORS -----")

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)
# x and y refer to the SAME object
# True


print("x is z:", x is z)
# x and z have the same values,
# but they are different objects
# False


print("x is not z:", x is not z)
# x and z are different objects
# True



# ============================================================
#                    END OF OPERATORS
# ============================================================

print("\n========== END OF OPERATORS ==========")