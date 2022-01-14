import random

"""
Generate a single random playing card with its numerical value used in blackjack.
if this program is run as a main program the numerical value is hidden by default, 
This can be changed by removing the [0] on the print function in the last line of the script,
doing so will return a list with two values, one being the name of the card as a string and the other
being its numerical value as used in blackjack.
"""

class cardGenerator:

	# The __init__ method contains a dictionary and a list, the dictionary holds the names of the cards and their values.
	
	def __init__(self):

		self.values = {
		'Ace': 1 or 11, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ten': 10, 'Nine': 9,
		'Eight': 8, 'Seven': 7, 'Six': 6, 'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2
		}

		self.suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

	# generate_card_name() is used to 'randomly' return a key, value pair from the dictionary created in the __init__() method
	
	def generate_card_name(self):
			card_name = random.choice(list(self.values.items()))		
			return card_name


	# generate_suit() method is used similarily to the above generate_card_name function but is seperate as it is instead selecting from a list

	def generate_suit(self):
		gen_suit = random.choice(self.suits)
		return gen_suit

# Main function to return a clean string with just the card name and its suit
if __name__ == "__main__":
	generate = cardGenerator()
	print(generate.generate_card_name()[0],"of" ,generate.generate_suit())