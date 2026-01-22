from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    eagle_count = 0
    tails_count = 0

    for _ in range(count):
        result = choice(coin)
        if result == EAGLE:
            eagle_count += 1
        else:
            tails_count += 1  # TODO подсчитать количество выпаданий орлов и решек

    min_count = min(eagle_count, tails_count)
    max_count = max(eagle_count, tails_count)

    ratio = min_count / max_count
    list_freq.append(ratio)
    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат
print(list_freq)
