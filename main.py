class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
        else:
            print("Данной книги нет в списке")

    def display_books(self):
        if not self.books:
            print("Библиотека пуста")
        else:
            for book in self.books:
                print(book)


# task_2:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if self.is_empty():
            print("Стек пуст")
            return None

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Стек пуст")
            return None

        return self.stack[-1]

    def is_empty(self):
        return not self.stack

# task_3:
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста")
            return None

        return self.queue.pop(0)

    def is_empty(self):
        return not self.queue

# task_4:
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        index = hash(key) % self.size
        return index

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value

        return None

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (stored_key, stored_value) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                return

# task_5:
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Если цикл закончился, элемент не найден
    return -1