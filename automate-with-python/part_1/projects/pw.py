#! python3
# pw.py - Not the safest place to put your password.

PASSWORDS = {'email': 'gkajskaj23ksaASd',
            'blog': 'sokorterq#@33',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for'+ account + copied + 'copied to clipboard')
else:
    print('There is no account name ' + account)