# Jogo de Adivinhar o numero
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# O jogador precisa adivinhar 6 numeros
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # Condicao ao palpite correto
if guess == secretNumber:
    print('Parabéns! Você acertou o numero em' + str(guessesTaken) + 'tentativas.')
else:
    print('Errado, o número que estava pensando era ' + str(secretNumber))    