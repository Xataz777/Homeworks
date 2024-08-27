team1_num = 42 # Число участников
team2_num = 32
team1_name = 'Терминиды' # Названия команд
team2_name = 'Автоматоны'
score1 = 40 # Кол-во решённых задач
score2 = 42
team1_time = 45 # Общее время решения задач команды
team2_time = 57
tasks_total = score1 + score2 # Всего задач выполнено

time_avg = (team1_time + team2_time) * 60 / tasks_total # Среднее время выполнения задачи

if score1 > score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = f'Победа команды "{team1_name}"'
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = f'Победа команды "{team2_name}"'
else:
    challenge_result = 'Ничья'

print('Число участников в команде "%s": %s ' % (team1_name, team1_num))
print('Сегодня в командах %s и %s участников соответственно' % (team1_num, team2_num))
print()
print('Команда "{}" решила задач: {}' .format(team2_name, score2))
print('Команда "{}" решила задачи за {} минут' .format(team2_name, team2_time))
print()
print(f'Команды решили {score1} и {score2} соответственно')
print(f'Результат игры: {challenge_result}')
print(f'Сегодня решено {tasks_total} задач, в среднем по {time_avg:5.2f} секунды каждая')