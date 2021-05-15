score = int(input())

if score <= 100 and score > 80:
    print('grade is A')
elif score > 60:
    print('grade is B')
elif score > 40:
    print('grade is C')
elif score > 20:
    print('grade is D')
elif score >= 0:
    print('grade is E')
else:
    print('wrong score')