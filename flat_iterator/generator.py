def flat_generator(list_of_lists):
    """
    Генератор для преобразования вложенных списков любой глубины в плоскую последовательность.
    """
    stack = [iter(list_of_lists)]

    while stack:
        try:
            current_iter = stack[-1]
            item = next(current_iter)

            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item

        except StopIteration:
            stack.pop()