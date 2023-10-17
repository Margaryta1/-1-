import random

def average(row):
    return sum(row) / len(row)

# Дано масив
array = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 3, 2]
]
def mean_of_row(row):
    #Обчислення середніх значень рядків
    return sum(row) / len(row) if len(row) > 0 else 0
def sort_array(array):
    #Відсортовування масиву за зростанням середніх значень
    row_means = [mean_of_row(row) for row in array]

    for i in range(len(row_means)):
        for j in range(0, len(row_means) - i - 1):
            if row_means[j] > row_means[j + 1]:
                #Зміна рядків та середніх значень
                row_means[j], row_means[j + 1] = row_means[j + 1], row_means[j]
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

print("Заданий масив:")
for row in array:
    print(row)

# Сортування та вивід відсортованого масиву
sorted_array = sort_array(array)
print("Відсортований масив:")
for row in sorted_array:
    print(row)