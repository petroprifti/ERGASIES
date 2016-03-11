import random


randomPX = random.randrange(0, 9)
randomPY = random.randrange(0, 9)

randomTX = random.randrange(0, 9)
randomTY = random.randrange(0, 9)

ll = abs(randomPX - randomTX) + abs(randomPY - randomTY)
print "Distance between you and the treasure: ", ll
print "Press w to go up, a to go left, s to go down amd d to go right"
while ll != 0:
	move = raw_input("Your Move: ")
	while move != "w" and move != "a" and move != "s" and move != "d":
		print "ONLY wasd\n"
		move = raw_input("Your Move: ")
	if move == "w":
		if (randomPY + 1) <10:
			randomPY = randomPY + 1
		else:
			print "error, you are at the top"
			continue
		print "Distance between you and the treasure: ", ll
		ll = abs(randomPX - randomTX) + abs(randomPY - randomTY)
	elif move == "a":
		if (randomPX - 1) >= 0:
			randomPX = randomPX - 1
		else:
			print "error, you can't go more left"
			continue 
		ll = abs(randomPX - randomTX) + abs(randomPY - randomTY)
		print "Distance between you and the treasure: ", ll
	elif move == "s":
		if (randomPY - 1) >= 0:
			randomPY = randomPY - 1
		else:
			print "error, you are at the bottom"
			continue 
		ll = abs(randomPX - randomTX) + abs(randomPY - randomTY)
		print "Distance between you and the treasure: ", ll
	elif move == "d":
		if (randomPX + 1) >= 0:
			randomPX = randomPX + 1
		else:
			print "error, you can't go more right"
			continue 
		ll = abs(randomPX - randomTX) + abs(randomPY - randomTY)		
		print "Distance between you and the treasure: ", ll

print "CONGRATULATIONS!!! YOU WON"

