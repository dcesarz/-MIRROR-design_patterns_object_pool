# POOL OF "FIRST" OBJECT
import copy
import math
import queue
import random
import time
import uuid

from global_models import append_to_size_list
from singleton import Singleton


# PYTHON USES PROTOTYPE BY DEFAULT WITH COPY.COPY AND COPY.DEEPCOPY


class FirstPool(metaclass=Singleton):

    def __init__(self, size):
        self._counter_in_use = 0
        self._default_size = size
        self._q = queue.Queue(maxsize=size)
        self._proto = First()
        [self._q.put(copy.copy(self._proto)) for _ in range(self._default_size)]
        # deepcopy not needed here
        # [self._q.put(First()) for _ in range(self._size)]
        # line above is for version w/o copy

    def reset_counter(self):
        self._counter_in_use = 0

    def acquire(self):
        result = None
        while result is None:
            try:
                result = self._q.get(timeout=0.001)
                self._counter_in_use += 1
            except queue.Empty:
                self._q.maxsize += 1
                self._q.put(copy.copy(self._proto))
        append_to_size_list(self._counter_in_use)
        return result

    def release(self, first):
        result = None
        while result is None:
            try:
                self._q.put(first, timeout=0.001)
                result = "Done!"
                self._q.maxsize -= 1
                self._counter_in_use -= 1
            except queue.Full:
                self._q.maxsize += 1
        result = None
        while result is None:
            try:
                self._q.get(timeout=0.001)
                self._q.maxsize -= 1
            except queue.Empty:
                self._q.maxsize += 1
                self._q.put(copy.copy(self._proto))
                result = "Done!"
        append_to_size_list(self._counter_in_use)


class First:
    _num = []
    #   called x y z for common names ?
    _what_numbers = 'random'
    #   options(weights) :
    _amount = 1
    _maximum = 1
    _weight_x = 1
    _weight_y = 1
    _weight_z = 1

    def __init__(self):
        self._id = str(uuid.uuid4())[:8]

    def gen_num(self):
        self._num = []
        if self._what_numbers == 'random':
            for i in range(self._amount):
                self._num.append(random.randrange(self._maximum) + 1)
        else:
            for i in range(self._amount):
                self._num.append(i + 1)

    def calculate(self):
        # ((y^n)/z)^1/x
        result = 0
        for i in self._num:
            temp = math.pow(math.pow(self._weight_y, i), 1 / self._weight_x)
            time.sleep(0.01 / i / self._amount)
            if i % 2 == 1:
                result -= temp
            else:
                result += temp
        return result

    def set_what_numbers(self, what_numbers):
        self._what_numbers = what_numbers

    def set_amount(self, amount):
        self._amount = amount

    def set_maximum(self, maximum):
        self._maximum = maximum

    def set_weight_x(self, x):
        self._weight_x = x

    def set_weight_y(self, y):
        self._weight_y = y

    def set_weight_z(self, z):
        self._weight_z = z

    def get_id(self):
        print(self._id)

    def get_num(self):
        return self._num
