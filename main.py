# Реализация пирамидальной сортировки

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Тестирование
if __name__ == "__main__":
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Исходный массив:", data)
    heapsort(data)
    print("Отсортированный массив:", data)

# Тестирование производительности
import time
import random
import matplotlib.pyplot as plt

def test_sorting_algorithms():
    sizes = [10, 100, 1000, 10000, 100000]
    algorithms = {
        "Heapsort": heapsort,
        "Quicksort": lambda arr: arr.sort(),
        "Bubble Sort": bubble_sort,
    }

    results = {name: [] for name in algorithms}

    for size in sizes:
        data = [random.randint(1, 1000000) for _ in range(size)]
        print(f"\nРазмер массива: {size}")

        for name, algorithm in algorithms.items():
            test_data = data.copy()
            start_time = time.time()

            if name == "Quicksort":
                algorithm(test_data)
            else:
                algorithm(test_data)

            elapsed_time = time.time() - start_time
            results[name].append(elapsed_time)
            print(f"{name}: {elapsed_time:.4f} сек.")

    # Построение графиков
    for name, timings in results.items():
        plt.plot(sizes, timings, label=name)

    plt.title("Сравнение времени сортировки")
    plt.xlabel("Количество элементов")
    plt.ylabel("Время (секунды)")
    plt.legend()
    plt.grid()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

test_sorting_algorithms()