my_dict={'Max': 1998, 'Alex': 1998, 'Artem': 2002}
print(my_dict)
print(my_dict.get('Max'))
print(my_dict.get('Denis'))
my_dict.update({'Egor': 1999,
                'Boris': 2009})
d=my_dict.pop('Alex')
print(d)
print(my_dict)

my_set = {1, 1, 2, 3, 4, 6, 6, 8, 4, False, 'True', 6, 0, (3,4,5)}
print(my_set)
my_set.add(97)
my_set.discard(2)
print(my_set)