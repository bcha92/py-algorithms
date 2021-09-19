def guessNumber():
	answer = ""
	while answer != "q":
		list = [4, 21, 45, 69, 99]
		answer = input("Guess a number between 1 to 100 (or press \"q\" to quit): ")
		if answer == "q":
			print("You pressed \"q\" to exit the program")
		else:
			answer = int(answer)
			for i in list:
				if answer == i:
					print("You have guessed the correct number")
					print("Program is now exiting...")
					answer = "q"
					break;
			if answer == "q":
				break;
			else:
				print("Guess was not correct. Try again!")
