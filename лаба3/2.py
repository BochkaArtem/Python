# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=","):
    list1=participants_first_group.split(separator)
    list2 = participants_second_group.split(separator)
    intersection= set(list1).intersection(set(list2))
    return sorted(intersection)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group, separator="|")
# TODO Провеьте работу функции с разделителем отличным от запятой
print(common)