import random #imports the random libray when choosing a random quote
import sys #used for testing the python version and quitting the program

class Quote(): #Declaring the object Quote to store all attributes needed
    def __init__(self, character, film, quote): #Initialising the object and allow entry of attributes
        self.character = character #setting the attribute character to the input
        self.film = film #setting the attribute film to the input
        self.quote = quote #setting the attribute quote to the input

def menu(): #Delcaring the menu function, used to effectivley restart the program
	print("#1 - Print all quotes") #Laying out basic menu info
	print("#2 - Enter a new quote")
	print("#3 - Show a quote from a specific film")
	print("#4 - Show a quote from a specific character")
	print("#5 - Quit")
	menuSelect = int(input("Enter your selection: ")) #Getting the user's selection as an integer (easier to compare in IF Statements)
	if(menuSelect == 1): #If the user selects entry #1
		print("Printing all quotes...") #Tell the user whats happening
		print(readFile()) #Call the read file function

	elif(menuSelect == 2): #If the user selects entry #2
		print("Entering a new quote...") #Tell the user whats happening
		char = input("Enter the character who said the quote: ") #Asks the user for the new character
		film = input("Enter the film the quote was in: ") #Asks the user for the new film
		quote = input("Enter the quote the quote was in: ") #Asks the user for the new quote
		addQuote(char, film, quote) #calls the add quote function and passes the three inputs in

	elif(menuSelect == 3): #If the user selects entry #3
		print("Getting quotes from film...") #Tell the user whats happening
		film = input("Enter the film you want quotes from: ") #Asks for the specific film
		printQuote(getFilmQuote(film)) #Calls the printQuote function and passes the result of getFilmQuote in

	elif(menuSelect == 4): #If the user selects entry #4
		print("Getting quotes from character...") #Tell the user whats happening
		char = input("Enter the character you want quotes from: ") #Asks for the specific character
		printQuote(getCharQuote(char)) #Calls the printQuote function and passes the result of getCharQuote in

	elif(menuSelect == 5): #If the user selects entry #5
		sys.exit() #Quits the program

	else: #If the input is invalid
		menu()#Restart

	menu()#Once task has been completed, restart menu

def readFile():#Declaration of the readFile function
	quotes = []#Creates an empty array for the quotes
	r = open("quotes.txt", "r") #Opens the quotes.txt file to read
	lines = r.readlines()#Creates an array, each value being a new line of text
	for line in lines: #Loops through each line in the file
		newLine = line.split("/")#Splits each line into another array, seperated by the '/'
		if(len(newLine) == 3): #If the line has the 3 specified data points (char/film/quote)
			quotes.append(Quote(newLine[0], newLine[1], newLine[2])) #Create a new instance of the Quote object and append it to the quotes array
		else: #If it has more than 3 data points
			print("Error in line: " + line) #Generate an error in that line and skip

	r.close() #Close the quotes.txt file
	return quotes #Return the quotes array to be used elsewhere

def addQuote(char, film, quote): #Declaration of the addQuote function, with 3 parameters
	quotes = readFile() #Quotes is set to the return of the readFile() function
	quotes.append(Quote(char, film, quote)) #Append a new instance of the Quote object to the array
	w = open("quotes.txt", "w") #Opens the quotes.txt file to write
	for quote in quotes: #Loops through each quote in the array
		w.write(quote.character + "/" + quote.film + "/" + quote.quote) #Writes each quote in the specified format a new line

	w.close() #Close the file
	return #Finish the function

def getFilmQuote(film): #Declaration of the getFilmQuote function that allows a film to be passed in
	quotes = readFile() #Quotes is set to the return of the readFile() function
	filmQuotes = [] #Creates an empty array for all the quotes with the specified film in it
	for quote in quotes: #Loops through every quote
		if quote.film == film: #If the quote is from the specified film
			filmQuotes.append(quote) #Append it to the filmQuotes array

	return filmQuotes #Returns the list of quotes the user wants

def getCharQuote(char): #Declaration of the getCharQuote function that allows a character to be passed in
	quotes = readFile() #Quotes is set to the return of the readFile() function
	charQuotes = [] #Creates an empty array for all the quotes with the specified character in it
	for quote in quotes: #Loops through every quote
		if quote.character == char: #If the quote is from the specified character
			charQuotes.append(quote) #Append it to the charQuotes array

	return charQuotes #Returns the list of quotes the user wants

def printQuote(quoteList): #Declaration of the printQuote function that has a quoteList passed into it
	repeat = True #Sets a boolean to keep repeating a quote
	while repeat: #While repeat is equal to true
		choice = input("Press enter to receive another quote! Enter Q to quit. ") #Asks the user whether they want another quote or to quit
		if(choice.upper() != "Q"): #If the user's choice was not to quit
			if(len(quoteList) <= 0): #If the quoteList has no more quotes
            	print("No more available quotes") #Tell the user this
            	repeat = False #Repeat is set to False
            	break #Break the while loop
		    quoteIndex = random.randint(0, len(quoteList)-1) #Sets a random number from 0 to the length of the array
            quoteChoice = quoteList[quoteIndex] #Gets the quote at random quoteIndex
            quoteList.remove(quoteChoice) #Remove the quote from the array
            print("Quote from " + quoteChoice.film + ", by " + quoteChoice.character + ": " + quoteChoice.quote) #Outputs the quote in the correct format

		else: #If the user chooses to quite
			repeat = False #Set repeat to False
			break #Breaks from the while loop

	return #End the function


menu() #Start the program by running the menu()
