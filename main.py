from decimal import Decimal, DecimalTuple


# Числовые типы
num_int = 5
num_float = 3.14
num_decimal = Decimal('3.14')
num_complex = 3 + 4j

# Строковые типы
hello_str = "hello world"

# Последовательности
numbers_list = [1, 2, 3]
letters_tuple = ("a", "b", "c")
decimal_tuple = DecimalTuple(0, (1, 2, 3), -1)

# Отображения
person_dict = {"name": "John", "age": 30}

# Множества
numbers_set = {1, 2, 3}
letters_frozenset = frozenset({"a", "b", "c"})

# Логические типы
is_true = True
is_false = False

# Специальные типы
no_value = None
class_type = type(int)
ellipsis_value = ...
not_implemented = NotImplemented
memory_view = memoryview(b'hello')

# Типы данных для управления памятью
byte_array = bytearray(b'hello')
bytes_value = b'hello'
buffer_value = memory_view

print(type(num_int), num_int)  # <class 'int'>
print(type(num_float), num_float)  # <class 'float'>
print(type(num_complex), num_complex)  # <class 'complex'>
print(type(num_decimal), num_decimal)  # <class 'decimal.Decimal'>
print(type(hello_str), hello_str)  # <class 'str'>
print(type(numbers_list), numbers_list)  # <class 'list'>
print(type(letters_tuple), letters_tuple)  # <class 'tuple'>
print(type(decimal_tuple), decimal_tuple)  # <class 'decimal.DecimalTuple'>
print(type(person_dict), person_dict)  # <class 'dict'>
print(type(numbers_set), numbers_set)  # <class 'set'>
print(type(letters_frozenset), letters_frozenset)  # <class 'frozenset'>
print(type(is_true), is_true)  # <class 'bool'>
print(type(is_false), is_false)  # <class 'bool'>
print(type(no_value), no_value)  # <class 'NoneType'>
print(type(class_type), class_type)  # <class 'type'>
print(type(ellipsis_value), ellipsis_value)  # <class 'ellipsis'>
print(type(not_implemented), not_implemented)  # <class 'NotImplementedType'>
print(type(memory_view), memory_view)  # <class 'memoryview'>
print(type(byte_array), byte_array)  # <class 'bytearray'>
print(type(bytes_value), bytes_value)  # <class 'bytes'>
print(type(buffer_value), buffer_value)  # <class 'memoryview'>
