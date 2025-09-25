from art import logo

print(logo)

# TODO-1: Ask the user for input

def sell_stuff():
    name = input("Tell me your name: ")
    price = int(input("Tell me your bid: $"))
# TODO-2: Save data into dictionary {name: price}

    auctioning[name] = price
    print(auctioning)

# TODO-4: Compare bids in dictionary
def make_money():
    highest_bid = 0
    highest_bidder = ""
    for key in auctioning:
        if auctioning[key] > highest_bid:
            highest_bidder = key
            highest_bid = auctioning[key]
    print(highest_bidder)
    print(highest_bid)

auctioning = {}
auction = True
while auction:
    sell_stuff()

# TODO-3: Whether if new bids need to be added

    again = input("Is there anyone else who would like to bid? Y/N")
    if again == 'n':
        auction = False
        make_money()




