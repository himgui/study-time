# Python Base - Linux Tips

Want to know more about this course? find it [LinuxTips.](https://www.linuxtips.io/course/python-base)
Created by Bruno Rocha.

# A few notes

### Debugging

If you want to debug your python script, run it using -i.

    python -i script.py

This will allow you to debug any variables or functions running on this script.

Funcions Debugging

    print(locals())
    print(globals())

This will print local or global variables within a py file.

## Modules

A few modules used in the classes, full doc on [docs python.](https://docs.python.org/3/tutorial/modules.html#)

    
    import random
    import os
    import sys
    import logging
    from datetime import datetime
    import random
    import itertools as it
    import functools as ft
    import uuid
    import getpass
     
    random.random()
    0.523697942392058
    random.randint(1,666)
    79
    
    import functools as ft
    myprint = ft.partial(print, sep="---")
    myprint
    functools.partial(<built-in  function  print>, sep='---')
    myprint("Abel", "Ferreira")
    Abel---Ferreira
    
    import statistics as st
    numbers = [6, 4, 7, 7, 7, 5, 3, 1, 2, 2]
    st.mean(numbers)
    4.4
## Test SMTP Server
To test the code we were doing, we activated an builtin SMTP mailserver using terminal.
	
    python -m smtpd -c DebuggingServer -n localhost:8025