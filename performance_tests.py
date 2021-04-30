import cProfile

import global_models
from client import fill_with_threads
from client import test_function
from first_pool import FirstPool
from second_pool import SecondPool
from third_pool import ThirdPool

base = 5

first_pool = FirstPool(base)
second_pool = SecondPool(base)
third_pool = ThirdPool(base)

max_sizes_list = []
min_sizes_list = []


def start_series_of_tests(thread_parameters, total, amount, maximum, x, y, z):
    test_prez_string = '\n====== {} POOL, {} THREADS, {} OBJECTS, {} OPERATIONS INSIDE FUNCTION ======\n'
    test_start_string = 'test_function(test_threads[{}])'
    le = len(thread_parameters)
    test_threads = []
    for i in range(le * 3):
        test_threads.append([])
    for i in range(le):
        global_models.clean_size_list()
        test_threads[i * 3] = fill_with_threads(thread_parameters[i], first_pool, total, amount, maximum, x, y, z)

        print(test_prez_string.format('FIRST', thread_parameters[i], total, amount))
        cProfile.runctx(test_start_string.format(i * 3), globals(), locals())

        x = global_models.get_max_size_list()
        y = global_models.get_min_size_list()
        max_sizes_list.append((x, "first"))
        min_sizes_list.append((y, "first"))
        global_models.clean_size_list()
        first_pool.reset_counter()

        test_threads[(i * 3) + 1] = fill_with_threads(thread_parameters[i], second_pool, total, amount, maximum, x, y,
                                                      z)

        print(test_prez_string.format('SECOND', thread_parameters[i], total, amount))
        cProfile.runctx(test_start_string.format((i * 3) + 1), globals(), locals())

        x = global_models.get_max_size_list()
        y = global_models.get_min_size_list()
        max_sizes_list.append((x, "second"))
        min_sizes_list.append((y, "second"))
        global_models.clean_size_list()
        second_pool.reset_counter()

        test_threads[(i * 3) + 2] = fill_with_threads(thread_parameters[i], third_pool, total, amount, maximum, x, y, z)

        print(test_prez_string.format('THIRD', thread_parameters[i], total, amount))
        cProfile.runctx(test_start_string.format((i * 3) + 2), globals(), locals())

        x = global_models.get_max_size_list()
        y = global_models.get_min_size_list()
        max_sizes_list.append((x, "third"))
        min_sizes_list.append((y, "third"))
        global_models.clean_size_list()
        third_pool.reset_counter()


# sys.stdout = open('profiler_tests_results_4', 'w')
start_series_of_tests([1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 100, 10000, 10, 2, 2, 2)
# sys.stdout.close()

# sys.stdout = open('profiler_tests_results_5', 'w')
start_series_of_tests([1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 1000, 10000, 10, 2, 2, 2)
# sys.stdout.close()

# sys.stdout = open('profiler_tests_results_6', 'w')
start_series_of_tests([1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 10000, 10000, 10, 2, 2, 2)
# sys.stdout.close()


# sys.stdout = open('maxes', 'w')
# print(max_sizes_list)
# sys.stdout.close()
#
# sys.stdout = open('mins', 'w')
# print(min_sizes_list)
# sys.stdout.close()
#
# print("DONE")
