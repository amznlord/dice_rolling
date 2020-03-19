import random
import time

#author info
__author__ = "Jakub Mareš"
__copyright__ = "Copyright 2020, Jakub Mareš"
__contact__ = "instagram: @kubamari"


print("\nDěkuji za stažení programu: Kostka.\n")

#proměnné pro rozsah kostky
var_min = 1
var_max = 6

#aktuální čas v ms
milliseconds = int(round(time.time() * 1000))

#vytvoření seedu pro generátor
random.seed(milliseconds)

while True:
	rolled_num = random.randint(var_min, var_max)
	print("Číslo na kostce je: ", rolled_num)
	repeat = input("Chceš pokračovat? (y/n)\n")
	if repeat.lower() == 'y':
		continue
	else:
		break
		print("Jakub Mareš, 2020")