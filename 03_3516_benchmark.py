import AulasPraticas.AP_03_ordenacao as ap3
import random
import time
import sys

sys.setrecursionlimit(10**6)

#retorna uma lista aleatoria com os numeros de 1 ate n

def avg_case(N):
    original = [x for x in range(N)]
    my_list = []
    while len(original):
            random_index = random.randint(0,len(original) - 1)
            my_list.append(original[random_index])
            original[random_index], original[-1] = original[-1], original[random_index]
            original.pop(-1)
    return my_list

def gera_worst_case_quick(N):
    return [x for x in range(N)][::-1]


def perf_algo(sort_algo, N, k, worst_case_fun = None):
    times = []
    for _ in range(k):
        my_list = worst_case_fun(N) if worst_case_fun else avg_case(N)
        start_t = time.perf_counter()
        sort_algo(my_list)
        end_t = time.perf_counter()
        times.append(end_t - start_t)
    return sum(times)/k

if __name__ == "__main__":
    print("-" * 64)
    print(f"{'Test N = 100':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 100, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 100, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort,100, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort,100, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort,100, 50)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort,100, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
    print(f"{'Test N = 500':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 500, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 500, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 500, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 500, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 500, 50)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 500, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
    print(f"{'Test N = 1000':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 1000, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 1000, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 1000, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 1000, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 1000, 50)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 1000, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
    print(f"{'Test N = 5000':^64}")
    print("-" * 64)
    print(f"Tempo médio Quick Sort: { perf_algo(ap3.quick_sort, 5000, 5)}ms")
    print(f"Pior tempo Quick Sort: { perf_algo(ap3.quick_sort, 5000, 5, gera_worst_case_quick)}ms")
    print(f"Tempo médio Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 5000, 50)}ms")
    print(f"Pior tempo Divide and Conquer: { perf_algo(ap3.divide_and_conquer_sort, 5000, 50, gera_worst_case_quick)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 5000, 50)}ms")
    print(f"Tempo médio Selection Sort: { perf_algo(ap3.selection_sort, 5000, 50, gera_worst_case_quick)}ms")
    print("-" * 64)
    
