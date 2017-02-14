#!/usr/bin/python3
# -*- coding: utf-8 -*

from random import randint


_randomNumber = randint(1,10)
_try = 1;

while(_try < 6):
    _userNumber = int(input("Guess any number between 1 to 10: "))
    if(_try > 5):
	print("bs chal pajj ja correct answer is: " +  _randomNumber)
    else:
	if(_userNumber == _randomNumber):
	    print("Hurrah you won ")
	   _try = 6;
	else :
	    print("wrong answer ypou have left " + str(5 -_try) + " try ")
	    _try += 1
