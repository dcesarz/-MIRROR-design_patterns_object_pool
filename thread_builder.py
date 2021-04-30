from __future__ import annotations

import threading
from abc import ABC, abstractmethod

from first_pool import FirstPool

"""
   Based on : 
       https://refactoring.guru/pl/design-patterns/builder/python/example
"""


class Builder(ABC):
    """
    BUILDER INTERFACE
    """

    @abstractmethod
    def thread_product(self) -> None:
        pass

    @abstractmethod
    def thread_product_what_pool(self, pool) -> None:
        pass

    @abstractmethod
    def thread_product_total_calculations(self, total) -> None:
        pass

    @abstractmethod
    def thread_product_what_numbers(self, what_numbers) -> None:
        pass

    @abstractmethod
    def thread_product_amount(self, amount) -> None:
        pass

    @abstractmethod
    def thread_product_maximum(self, maximum) -> None:
        pass

    @abstractmethod
    def thread_product_weight_x(self, x) -> None:
        pass

    @abstractmethod
    def thread_product_weight_y(self, y) -> None:
        pass

    @abstractmethod
    def thread_product_weight_z(self, z) -> None:
        pass


class ConcreteThreadBuilder(Builder):
    _thread_product = None

    def __init__(self):
        self.reset()

    def reset(self):
        self._thread_product = ThreadProduct()

    @property
    def thread_product(self) -> ThreadProduct:
        thread_product = self._thread_product
        self.reset()
        return thread_product

    def thread_product_what_pool(self, pool) -> None:
        self._thread_product.add_to_config("pool", pool)

    def thread_product_total_calculations(self, total) -> None:
        self._thread_product.add_to_config("total", total)

    def thread_product_what_numbers(self, what_numbers) -> None:
        self._thread_product.add_to_config("what_numbers", what_numbers)

    def thread_product_amount(self, amount) -> None:
        self._thread_product.add_to_config("amount", amount)

    def thread_product_maximum(self, maximum) -> None:
        self._thread_product.add_to_config("maximum", maximum)

    def thread_product_weight_x(self, x) -> None:
        self._thread_product.add_to_config("weight_x", x)

    def thread_product_weight_y(self, y) -> None:
        self._thread_product.add_to_config("weight_y", y)

    def thread_product_weight_z(self, z) -> None:
        self._thread_product.add_to_config("weight_z", z)

    def thread_product_start(self) -> None:
        self._thread_product.finish()


class ThreadProduct:

    def __init__(self) -> None:
        self._config = {}
        self._result_available = threading.Event()
        self._thread = None
        self._pool = FirstPool(5)
        self._what_numbers = 'random'
        self._total_calculations = 100
        self._amount = 1
        self._maximum = 1
        self._weight_x = 1
        self._weight_y = 1
        self._weight_z = 1

    def add_to_config(self, key, value):
        self._config[key] = value

    def config(self):
        self.__init__()
        self._thread = None
        self._pool = FirstPool(5)
        self._what_numbers = 'random'
        self._total_calculations = 100
        self._amount = 1
        self._maximum = 1
        self._weight_x = 1
        self._weight_y = 1
        self._weight_z = 1
        if 'pool' in self._config:
            self._pool = self._config['pool']
        if 'what_numbers' in self._config:
            self._what_numbers = self._config['what_numbers']
        if 'total' in self._config:
            self._total_calculations = self._config['total']
        if 'amount' in self._config:
            self._amount = self._config['amount']
        if 'maximum' in self._config:
            self._maximum = self._config['maximum']
        if 'weight_x' in self._config:
            self._weight_x = self._config['weight_x']
        if 'weight_y' in self._config:
            self._weight_y = self._config['weight_y']
        if 'weight_z' in self._config:
            self._weight_z = self._config['weight_z']
        self._result_available = threading.Event()

    def calculations(self):
        objects = []
        results = []
        for i in range(self._total_calculations):
            objects.append(self._pool.acquire())
            objects[i].set_what_numbers(self._what_numbers)
            objects[i].set_amount(self._amount)
            objects[i].set_maximum(self._maximum)
            objects[i].set_weight_x(self._weight_x)
            objects[i].set_weight_y(self._weight_y)
            objects[i].set_weight_z(self._weight_z)
            objects[i].gen_num()
            # print(self._thread)
            results.append(objects[i].calculate())
            self._pool.release(objects[i])
            objects[i] = None

    def get_thread(self):
        self.config()
        self._thread = threading.Thread(target=self.calculations)
        return self._thread

    def get_config(self):
        self.config()
        return self.calculations

    def start_thread(self):
        self.config()
        self._thread = threading.Thread(target=self.calculations)
        self._thread.start()
        # self._thread.join()

    def end_thread(self) -> None:
        self._thread.join()
