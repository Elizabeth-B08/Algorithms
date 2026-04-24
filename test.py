import time
import random

def test_algorithm(sort_func, data):
    start = time.perf_counter()
    sort_func(data.copy())
    end = time.perf_counter()
    return end - start

def run_trials(sort_func, size, trials=5):
    times = []
    for _ in range(trials):
        data = [random.randint(0, 10000) for _ in range(size)]
        times.append(test_algorithm(sort_func, data))
    return sum(times) / len(times)