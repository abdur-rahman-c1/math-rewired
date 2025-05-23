import math

"""
BODMAS / PEMDAS Order of Operations

+--------------------+-----------------------------------------------+
| Priority Level      | Operation                                     |
+--------------------+-----------------------------------------------+
| 1 (Highest)         | Brackets (import math


BODMAS / PEMDAS Order of Operations

+--------------------+-----------------------------------------------+
| Priority Level      | Operation                                     |
+--------------------+-----------------------------------------------+
| 1 (Highest)         | Brackets ( ), { }, [ ]                        |
+--------------------+-----------------------------------------------+
| 2                   | Orders (Exponents, Powers, Roots)             |
+--------------------+-----------------------------------------------+
| 3                   | Division (÷) & Multiplication (×) (Left to Right) |
+--------------------+-----------------------------------------------+
| 4 (Lowest)          | Addition (+) & Subtraction (−) (Left to Right)     |
+--------------------+-----------------------------------------------+



print( 6 - (56 - 40) / (2 * 4 ) + 5 )
print(f"6 - {56 - 40} / {2 * 4} + 5")
print(f"6 - 16 / 8 + 5 = 6 - {16 / 8} + 5")
print(f"6 - 2.0 + 5 = {6 - 2.0 + 5}") ), { }, [ ]                        |
+--------------------+-----------------------------------------------+
| 2                   | Orders (Exponents, Powers, Roots)             |
+--------------------+-----------------------------------------------+
| 3                   | Division (÷) & Multiplication (×) (Left to Right) |
+--------------------+-----------------------------------------------+
| 4 (Lowest)          | Addition (+) & Subtraction (−) (Left to Right)     |
+--------------------+-----------------------------------------------+


"""


"""
    12 Biscuits + 30 Candies = 192 BDT
       ||
    1 Biscuit = 6 BDT | 1 candy ? 


    1. 1 biscuit = 6BDT Mulitply that to 12 Biscuits = 72 BDT
    2. 72 BDT -   192
    3. That's the 30 Candies price
    4. now 30 candies / 30 Candies price

"""

solution = (192 - (6 * 12 )) / 30 
print(solution)