# Intentionally flawed Python program

# Importing modules
import itertools
import random

# Make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# Shuffle the cards
random.shuffle(deck)

# Draw five cards
print("You got:")
for i in range(5):
    rank, suit = deck[i]
    # Convert rank to face cards if applicable
    if rank == 1:
        rank = "Ace"
    elif rank == 11:
        rank = "Jack"
    elif rank == 12:
        rank = "Queen"
    elif rank == 13:
        rank = "King"
    print(f"{rank} of {suit}")
