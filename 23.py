current_name = "moshe"
while current_name != "quit":
    current_name = input("what is your name:")
    if current_name == "eden":
        continue
    if current_name == "ronen":
        break
    print(f" hello {current_name}")

else:
    print("thank you for playing")

