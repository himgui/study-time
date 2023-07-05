#! python
# randomQuizGenerator.py - Generating random questions and answers.
# Theme: Brazilian Cities and Capitals

# Start

import random

capitals ={'Acre': 'Rio Branco', 
'Alagoas': 'Maceio',
'Amapa': 'Macapa', 
'Amazonas': 'Manaus', 
'Bahia': 'Salvador', 
'Ceara': 'Fortaleza',    
'Distrito Federal': 'Brasilia',    
'Espirito Santo': 'Vitoria',    
'Goias': 'Goiania',    
'Maranhao': 'Sao Luis',    
'Mato Grosso': 'Cuiaba',    
'Mato Grosso do Sul': 'Campo Grande',    
'Minas Gerais': 'Belo Horizonte',    
'Para': 'Belem',    
'Paraiba': 'Joao Pessoa',    
'Parana': 'Coritiba',    
'Pernambuco': 'Recife',    
'Piaui': 'Teresina',    
'Rio de Janeiro': 'Rio Branco',    
'Rio Grande do Norte': 'Natal',    
'Rio Grande do Sul': 'Porto Alegre',    
'Rondonia': 'Porto Velho',    
'Roraima': 'Rondonia',    
'Sao Paulo': 'Sao Paulo',    
'Sergipe': 'Aracaju',
'Tocantins': 'Palmas'}  

# Generate 35 files with the exams
for quizNum in range(5):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1), 'w')

# Exam heading
quizFile.write('Name: \n\nDate:\n\nPeriod:\n\n')
quizFile.write((' ' * 20) + 'State Capitals of Brazil (Form %s)' % (quizNum + 1))
quizFile.write('\n\n')

# Randomize the questions
states =list(capitals.keys())
random.shuffle(states)

# Generating questions
for questionNum in range(26):
    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

# Shows the questions and anwswers

quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))

for i in range(4):
    quizFile.write('       %s. %s\n' % ('ABCD'[i], answerOptions[i]))
quizFile.write('\n')

answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()