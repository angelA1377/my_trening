grades =[[5,3,3,5,4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
students_1 = {}
index = 0
while index < len(grades):
    element = grades[index]
    synna = sum(element)/len(element)
    result = round(synna, 2)
    student = students[index]
    students_1[student] = result
    index += 1
print(students_1)
