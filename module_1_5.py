immutable_var=tuple([1, 'r', 2.0])
print(immutable_var)
#кортеж нельзя изменить тк он присвоен к переменной

mutable_list=['art', 1, 4.1, 'q']
mutable_list.extend(['modified'])
mutable_list.append(23)
print(mutable_list)