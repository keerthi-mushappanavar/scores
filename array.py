Here is the corrected and simplified version of your *MAIN BRANCH* and *LOCAL BRANCH* code for array_scores.py, based on your instructions:

### 🔹 Requirements:

* No data type conversion (i.e., *don’t use* int(), float(), str(), etc.).
* If system arguments are given → use them.
* If no system arguments → use *default scores* (no manual input).
* Simple structure using sys.argv.

---

## ✔ MAIN BRANCH: Sum & Average only

python
import sys

# MAIN BRANCH FUNCTIONALITY:
# Sum & Average only

# Example run:
# python array_scores.py 10 20 30 40

if len(sys.argv) > 1:
    scores = sys.argv[1:]  # Read from system arguments
    print("User provided input values:")
else:
    print("No command-line input provided. Using default values:")
    scores = ["10", "20", "30", "40"]  # Default values

# Convert using eval() for calculations
total = sum(eval(x) for x in scores)
average = total / len(scores)

print("Sum of scores =", total)
print("Average of scores =", average)


---

## ✔ LOCAL BRANCH: Sum, Average, Maximum, Minimum

python
import sys

# LOCAL BRANCH FUNCTIONALITY:
# Sum + Average + Maximum + Minimum

if len(sys.argv) > 1:
    scores = sys.argv[1:]  # Read from system arguments
    print("User provided input values:")
else:
    print("No command-line input provided. Using default values:")
    scores = ["10", "20", "30", "40"]  # Default values

# Convert using eval() for calculations
total = sum(eval(x) for x in scores)
average = total / len(scores)
maximum = max(scores, key=eval)
minimum = min(scores, key=eval)

print("Sum of scores =", total)
print("Average of scores =", average)
print("Maximum score =", eval(maximum))
print("Minimum score =", eval(minimum))


---

### 💡 Notes:

* No explicit data types used (int(), float(), etc.). Only eval() is used for calculations.
* Default values are provided in the else part — *no input() is used*.
* Perfect for Jenkins-style automation.

---

### ⭐ Example Jenkins Trigger:

You can run these directly in Jenkins using:


python3 array_scores.py 10 20 30 40 50


Would you like a version that **avoids using eval()** too?
