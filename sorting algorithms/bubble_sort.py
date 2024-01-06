def bubble_sort_asc(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    return numbers


def bubble_sort_des(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__=="__main__":
    numbers = [23,43,45,23,23,5,34,65,78,78,98,90]
    print(f'Sorted List in ascending order: {bubble_sort_asc(numbers)}')  
    numbers = [23,43,45,23,23,5,34,65,78,78,98,90]
    print(f'Sorted List in descending order: {bubble_sort_des(numbers)}')  