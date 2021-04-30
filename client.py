from first_pool import FirstPool
from second_pool import SecondPool
from third_pool import ThirdPool
from thread_builder import ConcreteThreadBuilder

base = 5

first_pool = FirstPool(base)
second_pool = SecondPool(base)
third_pool = ThirdPool(base)


#   for quick thread building
def builder_helper(pool, total, amount, maximum, x, y, z):
    thread_builder = ConcreteThreadBuilder()
    thread_builder.thread_product_what_pool(pool)
    thread_builder.thread_product_total_calculations(total)
    thread_builder.thread_product_amount(amount)
    thread_builder.thread_product_maximum(maximum)
    thread_builder.thread_product_weight_x(x)
    thread_builder.thread_product_weight_y(y)
    thread_builder.thread_product_weight_z(z)
    return thread_builder.thread_product


def fill_with_threads(list_length, pool, total, amount, maximum, x, y, z):
    list_result = []
    for i in range(list_length):
        list_result.append(builder_helper(pool, total, amount, maximum, x, y, z))
    return list_result


#  function to test
def test_function(threads):
    threads_temp = []
    for t in threads:
        threads_temp.append(t.get_thread())
    for tt in threads_temp:
        tt.start()
    for tt in threads_temp:
        tt.join()
