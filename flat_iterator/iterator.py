class FlatIterator:
    """
    Итератор для преобразования вложенных списков любой глубины в плоскую последовательность.
    Использует стек для отслеживания текущего уровня вложенности.
    """

    def __init__(self, list_of_list):
        self.stack = [(list_of_list, 0)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list, current_idx = self.stack[-1]

            if current_idx >= len(current_list):
                self.stack.pop()
                continue

            item = current_list[current_idx]
            self.stack[-1] = (current_list, current_idx + 1)

            if isinstance(item, list):
                self.stack.append((item, 0))
            else:
                return item

        raise StopIteration