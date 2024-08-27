immutable_var = (1, 0, 'd', 'g')
print (immutable_var)
#immutable_var[2] = 200
# Изменить элемент кортежа нельзя, т.к. кортеж относится к неизменяемым типам данных.

mutable_list = [1, 0, 'd', 'g']
mutable_list.extend(['Modified', True])
mutable_list[2] = 5
print(mutable_list)