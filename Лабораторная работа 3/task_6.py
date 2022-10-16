list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_el = max(list_numbers)
max_el_index = list_numbers.index(max_el)
last_el = list_numbers[-1]

list_numbers[-1] = max_el
list_numbers[max_el_index] = last_el
# TODO Оформить решение

print(list_numbers)
