# План задания
# 1. посчитать отдельно средние значения и заполнить этими данными новый список
# 2. отсортировать в алфавитном порядке множество students
# 3. Заполнить словарь готовыми списками

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = list() #объявил пустой список, для того чтобы его заполнить с помощью цикла
for i in range(len(grades)):
    average = 0
    average = sum(grades[i])/len(grades[i])
    average_grades.append(average)  
print(average_grades)
list_studendts = list(students)
sorted(list_studendts)

students_and_average_score = dict(zip(list_studendts,average_grades))

print(students_and_average_score)