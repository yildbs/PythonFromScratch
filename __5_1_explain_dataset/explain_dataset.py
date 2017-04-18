import generateGradesDict
import collections
from matplotlib import pyplot as plt

grades = generateGradesDict.generateGradesDict(1000)
grades_value = grades.values()

grades_count = collections.Counter(list(grades_value))

xs = range(101)
ys = [grades_count[x] for x in xs]

print(grades_count)
print(ys)
print(grades)

print(max(ys))

plt.bar(xs,ys)
plt.axis([0, 101, 0, max(ys)+5])

plt.title("Histogram of grades")
plt.xlabel('Grades')
plt.ylabel('# of students')

plt.show()

