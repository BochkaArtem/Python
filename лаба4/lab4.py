# TODO написать функцию remove
from typing import TypeVar, List, Any
T = TypeVar('T')
def remove(lst: List[T], value: T) -> List[T]:
    try:
        index_to_remove = len(lst) - 1 - lst[::-1].index(value)
    except ValueError:
        raise ValueError(f"Значение {value} не найдено в списке")
    del lst[index_to_remove]
    return lst


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
