goals = {'Deyverson': 'Nov 27th', 'Breno Lopes': 'Jan 30th'}
while True:
    print('Enter a player name: (blank to quit)')
    name = input()
    if name =='':
        break
    if name in goals:
        print(goals[name]+ ' is the day of the ' +name)
    else:
        print('I do not have a goal for this bagre called:' + name)
        print('What is the date of his goal?')
        goal=input()
        goals[name]= goal 
        print('Goal date databse updated!')