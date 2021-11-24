from replit import clear
import art as art
#HINT: You can call clear() to clear the output in the console.

bidders = {}

highest_bid = {
  "name": "",
  "bid": 0
}

def add_bidders(name, bid):
  bidders[name] = bid

def high_bid():
  print(highest_bid)

def main():
  run = True
  while run:
    choice = input("Do you want to add another bidder? y or n: ")
    if choice == "y":
      name = input("Name: ")
      bid = int(input("Bid: "))
      add_bidders(name, bid)

      if bid > highest_bid["bid"]:
        highest_bid["name"] = name
        highest_bid["bid"] = bid
      clear()
    elif choice == "n":
      high_bid()
      run = False
    else:
      print("Wrong input ")
      continue

if __name__ == '__main__':
    main()

