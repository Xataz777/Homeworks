my_list = ['Minecraft', 'Escape from Tarkov', 'Deep Rock Galactic', 'Voices of the Void', 'The Long Dark', 'Subnautica', 'Terraria']
print ('Список:', my_list)
print ('Первый элемент:', my_list [0])
print ('Последний элемент:', my_list [-1])
print ('Подсписок:', my_list [2:5])
my_list [2] = 'Helldivers 2'
print ('Изменённый список:', my_list)

print()

my_dict = {'Valve':'Half Life 2', 'Battlestate Games':'Escape from Tarkov', 'Mojang':'Minecraft'}
print ('Словарь:', my_dict)
print ('Mojang:', my_dict ['Mojang'])
my_dict ['Valve'] = 'Portal 2'
my_dict ['Hiterland'] = 'The Long Dark'
print ('Изменённый и дополненный словарь:',my_dict)