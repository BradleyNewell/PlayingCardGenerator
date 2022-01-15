import random

# Generate a single random playing card with its numerical value used in blackjack.

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