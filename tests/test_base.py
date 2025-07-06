# общие тестовые функции для обеих структур данных
import types
from flat_iterator import FlatIterator, flat_generator

def test_shallow_structure():
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    # Тест итератора
    assert list(FlatIterator(list_of_lists)) == expected

    # Тест генератора
    result = list(flat_generator(list_of_lists))
    assert result == expected
    assert isinstance(flat_generator(list_of_lists), types.GeneratorType)

def test_deep_structure():
    list_of_lists = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    # Тест итератора
    assert list(FlatIterator(list_of_lists)) == expected

    # Тест генератора
    result = list(flat_generator(list_of_lists))
    assert result == expected
    assert isinstance(flat_generator(list_of_lists), types.GeneratorType)