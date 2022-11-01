def delete(list_, index=None):
    if index is None:  # проверка, оставил ли пользователь индекс без указания
        index = len(list_) - 1  # вычет единицы, т.к. индексы начинаются с нуля
        return list_[:index]
    return list_[:index] + list_[index + 1:]  # прибавка единицы и возвращение списка, в котором удалено требуемое значение


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

