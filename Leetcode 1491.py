def average(salary):
    maxsal = salary[0]
    for i in range(len(salary)):
        if salary[i] > maxsal:
            maxsal = salary[i]

    minsal = salary[0]
    for i in range(len(salary)):
        if salary[i] < minsal:
            minsal = salary[i]

    total = 0
    for i in range(len(salary)):
        if salary[i]!=maxsal and salary[i]!=minsal:
            total += salary[i]

    return total/(len(salary)-salary.count(maxsal)-salary.count(minsal))

print(average([4000,3000,2000,1000]))
