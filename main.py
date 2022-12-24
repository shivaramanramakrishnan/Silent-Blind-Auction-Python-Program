from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

auctioners = {}

flag = 1
while flag:
  name = input("What is your name? ")
  amt = int(input("How much would you like to bid? "))

  auctioners[name] = amt

  choice = input("Are there other users who want to bid? ")
  if choice == "yes":
    clear()
  else:
    flag=0
    clear()
bids=[]
for key in auctioners:
  bids.append(auctioners[key])

max_bid = max(bids)

for key in auctioners:
  if max_bid == auctioners[key]:
    print(f"The winner of the bid is {key} with a bid amount of {max_bid}")
  
