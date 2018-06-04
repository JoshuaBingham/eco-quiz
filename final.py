print "Biology Testing on Ecology"
print "By Joshua Bingham"
print "This test will test your knowledge about Ecology and show you what areas you need to improve in."
print "When answering a question, type the number of the answer you think is true."
#name = str(input("What is your name?"))
score = 0
score = int(score)



print "Question One: What specifically is Ecology?"
print "1: The science of all life on earth"
print "2: Cell division"
print "3: The interactions between organisms and their environment"
print "4: The origins of life"

q1r = input("Selection: ")

if q1r == 3:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Two: What is the highest level of Ecology listed?"
print "1: Population"
print "2: Ecosystem"
print "3: Community"
print "4: Species"

q2r = input("Selection: ")

if q2r == 2:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Three: Which of the following is not a defense against predation?"
print "1: Commensalism"
print "2: Hiding/feeding"
print "3: Chemical poisons"
print "4: Spines and thorns"

qr3 = input("Selection: ")

if qr3 == 1:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Four: What limits the number of individuals that can occupy an area at a time?"
print "1: Limiting factors"
print "2: Carrying capacity"
print "3: Low resources"
print "4: Predators"

qr4 = input("Selection: ")

if qr4 == 2:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Five: Which of the following is an example of a keystone species?"
print "1: Jaguar"
print "2: Coral"
print "3: Sea Star"
print "4: All of the above"

qr5 = input("Selection: ")

if qr5 == 4:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Six: Which of the following is a density-dependent factor?"
print "1: Weather"
print "2: Rain"
print "3: Competition for food"
print "4: feeding"

qr6 = input("Selection: ")

if qr6 == 3:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Seven: What is the name for the most abundant species in a community?"
print "1: Dominant"
print "2: Recessive"
print "3: Keystone"
print "4: Producer"

qr7 = input("Selection: ")

if qr7 == 1:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Eight: Which of the following is not a name for an interaction within a community?"
print "1: Predation"
print "2: Mutualism"
print "3: Commensalism"
print "4: Consumerism"

qr8 = input("Selection: ")

if qr8 == 4:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Nine: What is an example of two species that have a symbiotic relationship?"
print "1: Bears and deers"
print "2: Bees and flowers"
print "3: Sea stars and humans"
print "4: wolves and moose"

qr9 = input("Selection: ")

if qr9 == 2:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Question Ten: What is an abiotic factor?"
print "1: The Nonliving factors of an environment"
print "2: The factors that effect population growth"
print "3: The resources of an environment"
print "4: The factors that effect the lifespan of an organism"

qr10 = input("Selection: ")

if qr10 == 1:
	print "correct!"
	score = score + 1
	print "Score:" + str(score)
else:
	print "Wrong!"
	print "Score:" + str(score)

print "Results:"
Percentage = score * 10

if Percentage >= 90:
	print "A"
else:
	if Percentage == 80:
		print "B"	
	else:
		if Percentage == 70:
			print "C"
		else:
			if Percentage == 60:
				print "D"
			else:
				print "F"

print "Bonus Questions!"

bscore = 0
bscore = int(bscore)

print "Question 1: what colour is red?"
print "1: the best colour"
print "2: the worst colour"
print "3: warm"
print "4: a dark pink"

qr = input("Selection: ")

if qr == 1:
	print "correct!"
	bscore = bscore + 1
	print "Score:" + str(bscore)
else:
	print "Wrong!"
	print "Score:" + str(bscore)

print "Question 2: If you have 2 buckets with 3 stones in them, and I have 7 buckets with 2 stones in each of them, how many buckets do you have?"
print "1: 10"
print "2: 3"
print "3: 2"
print "4: 1"

qr = input("Selection: ")

if qr == 3:
	print "correct!"
	bscore = bscore + 1
	print "Score:" + str(bscore)
else:
	print "Wrong!"
	print "Score:" + str(bscore)

print "Question 3: What is the best way to play Bastion?"
print "1: You don't"
print "2: For throwing purposes"
print "3: find the best position before engaging the opposition"
print "4: spray and pray in turret mode"

qr = input("Selection: ")

if qr == 3:
	print "correct!"
	bscore = bscore + 1
	print "Score:" + str(bscore)
else:
	print "Wrong!"
	print "Score:" + str(bscore)

print "Question 4: why do people hate Bastion so much?"
print "1: Becasue he was OP at game launch, and he was always killing everyone, which scared the Overwatch community and made them hate Bastion"
print "2: Because theyre always getting destroyed by him, and cant figure out how to counter him even though most people claim to know how"
print "3: Because all of the sheild heros (Reinhardt, Orisa, Winston, and Briggite) are always getting countered by him, causing them to spread lies about Bastion in hopes of having him gone from competitive Overwatch forever"
print "4: Because a lot of Overwatch players are toxic, and get mad when people play heros that they think are bad"

qr = input("Selection: ")

if qr == 4:
	print "correct!"
	bscore = bscore + 1
	print "Score:" + str(bscore)
else:
	print "Wrong!"
	print "Score:" + str(bscore)

print "Question 5: What Overwatch hero takes the most skill?"
print "1: Widowmaker"
print "2: Genji"
print "3: McCree"
print "4: Bastion"

qr = input("Selection: ")

if qr == 2:
	print "correct!"
	bscore = bscore + 1
	print "Score:" + str(bscore)
else:
	print "Wrong!"
	print "Score:" + str(bscore)

if bscore == 5:
	print "Not bad, kid!"

else:
	print "You need to: Seek help in many ways."


