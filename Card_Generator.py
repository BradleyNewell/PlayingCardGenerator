import random

class cardGenerator:
	def __init__(self):
		self.values = {
		'Ace': 1 or 11, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ten': 10, 'Nine': 9,
		'Eight': 8, 'Seven': 7, 'Six': 6, 'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2
		}

		self.suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']


	def generate_card(self):

			gen_value = random.choice(list(self.values.keys()))
			gen_suit = random.choice(self.suits)
			return(gen_value, gen_suit)



if __name__ == "__main__":
	generate = cardGenerator()
	print(generate.generate_card())