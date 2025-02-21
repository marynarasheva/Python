randomList = [1000, 50, 345, 788, 2, 10, 88, 67, 999, 0, 5]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

randomList = [1000, 50, 345, 788, 2, 10, 88, 67, 999, 0, 5]
bubble_sort(randomList)

even_numbers = [num for num in randomList if num % 2 == 0]
odd_numbers = [num for num in randomList if num % 2 != 0]
even_avg = calculate_average(even_numbers)
odd_avg = calculate_average(odd_numbers)
print("Sorted list:", randomList)
print("Even numbers:", even_numbers, "Average:", even_avg)
print("Odd numbers:", odd_numbers, "Average:", odd_avg)
