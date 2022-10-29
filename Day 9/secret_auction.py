from os import system

from art import logo

print(logo)
end_bid = False
while not end_bid:
    auction = {}
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: ₹"))
    auction[name] = bid
    continue_bid = input("Are there any other bidders? Type 'no' if there are no bidders: ").lower()

    if continue_bid == "no":
        end_bid = True
        winner_names = list(auction.keys())
        winner_bids = list(auction.values())
        winner = winner_names[winner_bids.index(max(winner_bids))]
        print(f"The Winner is {winner} with a bid of ₹{max(winner_bids)}")
    else:
        end_bid = False
        system("cls")
