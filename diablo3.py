print(" Only enter numbers no prefix after as m,b or tr")
print(" as sfp is included in gph you will need to check urself how many keys used per hour for exact")
side1 = float(input(' T13 GPH: '))
side2 = float(input(' xp/hr getting keys in billions ex 55: '))
side3 = float(input(' input xp/hr with stacked in billions ex 1000 for 1t: '))
side4 = float(input(' Keys used per hour: '))
print(" 1r2gr information")
bas = float(input(' 1r2gr xp/hr: '))
gph = side1 * 2 * 100 + (side1 * 100 / 4)
circumference = side2 * 100
keys = gph / side4
hours = 100 + keys
total = keys * side3 + circumference
area = bas * hours

print(" keys per 100 hours on average = %.2f" %gph)
print(" xp after 100 hours of gathering keys in billions = %.2f" %circumference)
print(" hours keys will last = %.2f" %keys)
print(" total hours of t13 and using all keys = %.2f" %hours)
print(" total exp after all hours = %.2f" %total)
print(" total exp from 1r2gr same time = %.2f" %area)

print(" Every number is in billions!")
q = input("Enter to quit")