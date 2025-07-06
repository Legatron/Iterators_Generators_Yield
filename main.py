# import types
#
#
# class FlatIterator:
#     """
#     Итератор для преобразования вложенных списков любой глубины в плоскую последовательность.
#     Использует стек для отслеживания текущего уровня вложенности.
#     """
#
#     def __init__(self, list_of_list):
#         """
#         Инициализация итератора.
#         :param list_of_list: Основной список, содержащий вложенные списки любой глубины
#         """
#         # Стек хранит кортежи (текущий_список, текущий_индекс)
#         # Инициализируем стек основным списком и начальным индексом 0
#         self.stack = [(list_of_list, 0)]
#
#     def __iter__(self):
#         """Возвращает сам объект итератора (обязательный метод для итераторов)"""
#         return self
#
#     def __next__(self):
#         """
#         Возвращает следующий элемент плоской последовательности.
#         Использует стек для обработки вложенных структур:
#         1. Пока стек не пуст, обрабатываем верхний элемент
#         2. Если текущий список закончился - удаляем его из стека
#         3. Если текущий элемент - список, добавляем его в стек для обработки
#         4. Если элемент не список - возвращаем его
#         """
#         while self.stack:
#             # Берем верхний элемент стека (текущий список и текущий индекс)
#             current_list, current_idx = self.stack[-1]
#
#             # Проверяем, достигли ли конца текущего списка
#             if current_idx >= len(current_list):
#                 # Удаляем обработанный список из стека
#                 self.stack.pop()
#                 continue
#
#             # Получаем текущий элемент и обновляем индекс в стеке
#             item = current_list[current_idx]
#             # Увеличиваем индекс в текущем списке (заменяем верхний элемент стека)
#             self.stack[-1] = (current_list, current_idx + 1)
#
#             # Если элемент - список, добавляем его в стек для дальнейшей обработки
#             if isinstance(item, list):
#                 self.stack.append((item, 0))
#             else:
#                 # Нашли несписочный элемент - возвращаем его
#                 return item
#
#         # Если стек пуст - элементов больше нет
#         raise StopIteration
#
#
# def flat_generator(list_of_lists):
#     """
#     Генератор для преобразования вложенных списков любой глубины в плоскую последовательность.
#     Использует стек итераторов для обработки вложенных структур.
#
#     :param list_of_lists: Список, содержащий вложенные списки элементов любой глубины
#     :yield: Элементы из всех вложенных списков в последовательном порядке
#     """
#     # Стек хранит итераторы для каждого уровня вложенности
#     # Начинаем с итератора для основного списка
#     stack = [iter(list_of_lists)]
#
#     while stack:
#         try:
#             # Берем итератор с вершины стека
#             current_iter = stack[-1]
#             # Получаем следующий элемент из текущего итератора
#             item = next(current_iter)
#
#             # Проверяем тип элемента
#             if isinstance(item, list):
#                 # Если элемент - список, добавляем в стек его итератор
#                 stack.append(iter(item))
#             else:
#                 # Если обычный элемент - возвращаем его
#                 yield item
#
#         except StopIteration:
#             # Текущий итератор закончился - удаляем его из стека
#             stack.pop()
#
#
# # Тестовые функции
# def test_1():
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#
# def test_2():
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
#
#
# def test_3():
#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#
#
# def test_4():
#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
#
#
# if __name__ == '__main__':
#     test_1()
#     test_2()
#     test_3()
#     test_4()
from tests import test_shallow, test_deep

if __name__ == '__main__':
    print("Пуск тестов плоской структуры данных...")
    try:
        test_shallow.test_flat_iterator_shallow()
        test_shallow.test_flat_generator_shallow()
        print("\nТесты плоской структуры данных прошли успешно!")

    except AssertionError: print("Ошибка проверки данных!")

    print("\nПуск тестов вложенной структуры данных...")
    try:
        test_deep.test_flat_iterator_deep()
        test_deep.test_flat_generator_deep()
        print("\nТесты вложенных структур данных прошли успешно!")
    except AssertionError:
        print("Ошибка проверки данных!")
