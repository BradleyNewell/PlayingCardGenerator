import random

"""
Generate a single random playing card with its numerical value used in blackjack.
if this program is run as a main program the numerical value is hidden by default, 
This can be changed by removing the [0] on the print function in the last line of the script,
doing so will return a list with two values, one being the name of the card as a string and the other
being its numerical value as used in blackjack.
"""

class cardGenerator:

	# The __init__ method contains two lists, one containing the names of the cards and the other contains their values.
	
	def __init__(self):

		self.values = ['Ace', 'Jack', 'Queen', 'King', 'Ten', 'Nine',
					'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']

		self.suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

		self.generate_card_name = random.choice(self.values)
		self.generate_suit = random.choice(self.suits)


	def format_card(self):
		formatted_card = self.generate_card_name, "of",  self.generate_suit
		return ' '.join(formatted_card)


if __name__ == "__main__":
	
	generate = cardGenerator()	
	print(generate.format_card())