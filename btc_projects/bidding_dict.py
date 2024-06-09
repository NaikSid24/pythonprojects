logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


user_data = []
stop = False


def add_details():
  global stop
  while not stop:
    inputname = input("Enter your name: ")
    inputbid = float(input("Enter your bid: "))
    player_data = {'user_name': inputname, 'user_bid': inputbid}
    user_data.append(player_data)
    choice = input("Is there any other player? (yes/no): ").lower()
    if choice == "yes":
      stop = False
    elif choice == "no":
      stop = True
      highest_bid = 0
      winner = ""
      for user in range(0, len(user_data)):
        current_bid = user_data[user]["user_bid"]
        if current_bid > highest_bid:
          highest_bid = current_bid
          winner = user_data[user]['user_name']

      print(f"Winner is {winner} with bid amount {highest_bid}")
    else:
      print("Enter correct choice")


add_details()
