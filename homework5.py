immutable_var = "String", 55, 5.24, True
print(immutable_var)
# immutable_var[0] = "Doom"
# После создания кортежа нельзя изменить его элементы, добавить новые элементы или удалить существующие.

mutable_list = [1, 2, 3, "Привет", True]
print(mutable_list)
mutable_list[0] = 265
mutable_list[4] = "Пока"
mutable_list[-1] = False
print(mutable_list)