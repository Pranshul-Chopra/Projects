tnos = 1500000
print("Rank Priority Generator")
while True:
    try:
        a = int(input("How many attempts did you give for JEE? : "))
        if a not in range(1, 3):  
            raise ValueError
        break
    except ValueError:
        print("Please enter 1 or 2 only.")

while True:
    try:
        p = float(input("Please enter your percentile (0-100): "))
        if not (0 <= p <= 100):
            raise ValueError
        break
    except ValueError:
        print("Percentile must be between 0 and 100.")

c = input("Please enter your caste (Gen/SC/PwD): ").lower()
g = input("Please enter your gender (male/female): ").lower()


if c == "gen":
    x = 1
elif c in ["sc", "pwd"]:
    x = 2
else:
    x = 1  

if g == "male":
    y = 1
elif g == "female":
    y = 2
else:
    y = 1 


rank_formula = a + x + y
rank = round(tnos - (tnos * p / 100) - (p * rank_formula / 100))  

rank += 10000  

print(f"Estimated rank: {rank}")
