tnos = 1500000
print("rank priority generator")
a = int(input("how many attempts you gave for jee? : "))
p = float(input("Please enter your percentile : "))
c = input("Please enter your caste Gen/Sc/Pwd : ").lower
g = input("please enter your gender male/female : ").lower
x = 0
y = 0
if c == "gen" :
    x = 1
elif c == "sc" or c == "pwd" :
    x = 2

if g == "male" :
    y = 1
else :
    y = 2

rank_formula = a + x + y
rank = round(tnos - (tnos * p / 100) - (p * rank_formula / 100)) + 10000

a in range (0,2)
p in range (0,101)

print(rank)