
# Define the characters with their attributes using arrays
aria = [100, 50, 70, 80]  # [health, strength, intelligence, charm]
spencer = [100, 60, 90, 70]
hanna = [100, 55, 65, 85]
emily = [100, 75, 60, 75]

while True:
    # Aria's turn
    print("\nAria Montgomery's turn.")
    print("Ezra: 'Aria, have you heard anything new about Alison?'")
    print("1. Yes, I found a clue in her diary.")
    print("2. No, I haven’t. But I’m still looking.")
    print("3. Why do you care so much?")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        print("You and Ezra found a clue in Alison's diary.")
        aria[2] += 5  # Increase intelligence
    elif choice == 2:
        print("Ezra looks disappointed but supportive.")
    elif choice == 3:
        print("Ezra looks suspicious but says nothing.")
        aria[3] -= 5  # Decrease charm
    else:
        print("Invalid choice. Nothing happens.")

    # Display updated attributes
    print("\nUpdated attributes for Aria:")
    print(f"Health: {aria[0]}, Strength: {aria[1]}, Intelligence: {aria[2]}, Charm: {aria[3]}")

    # Spencer's turn
    print("\nSpencer Hastings's turn.")
    print("Toby: 'I think I saw someone watching us last night.'")
    print("1. Who do you think it was?")
    print("2. You’re being paranoid.")
    print("3. We need to be careful.")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        print("You and Toby decided to investigate further.")
        spencer[2] += 5  # Increase intelligence
    elif choice == 2:
        print("Toby looks hurt by your words.")
        spencer[3] -= 5  # Decrease charm
    elif choice == 3:
        print("Toby nods in agreement.")
    else:
        print("Invalid choice. Nothing happens.")

    # Display updated attributes
    print("\nUpdated attributes for Spencer:")
    print(f"Health: {spencer[0]}, Strength: {spencer[1]}, Intelligence: {spencer[2]}, Charm: {spencer[3]}")

    # Hanna's turn
    print("\nHanna Marin's turn.")
    print("Caleb: 'I found something in Alison’s email account.'")
    print("1. What did you find?")
    print("2. Can you hack it?")
    print("3. Leave it alone, Caleb.")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        print("You and Caleb discovered a suspicious email.")
        hanna[2] += 5  # Increase intelligence
    elif choice == 2:
        print("Caleb smiles and starts working on it.")
        hanna[1] += 5  # Increase strength
    elif choice == 3:
        print("Caleb looks disappointed but respects your decision.")
    else:
        print("Invalid choice. Nothing happens.")

    # Display updated attributes
    print("\nUpdated attributes for Hanna:")
    print(f"Health: {hanna[0]}, Strength: {hanna[1]}, Intelligence: {hanna[2]}, Charm: {hanna[3]}")

    # Emily's turn
    print("\nEmily Fields's turn.")
    print("Jenna: 'I know something about Alison’s last day.'")
    print("1. Tell me everything you know.")
    print("2. Why should I trust you?")
    print("3. Let's talk somewhere private.")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        print("Jenna reveals some crucial information.")
        emily[2] += 5  # Increase intelligence
    elif choice == 2:
        print("Jenna gets defensive.")
        emily[3] -= 5  # Decrease charm
    elif choice == 3:
        print("Jenna agrees and you learn more.")
        emily[3] += 5  # Increase charm
    else:
        print("Invalid choice. Nothing happens.")

    # Display updated attributes
    print("\nUpdated attributes for Emily:")
    print(f"Health: {emily[0]}, Strength: {emily[1]}, Intelligence: {emily[2]}, Charm: {emily[3]}")

    # Check if the player wants to continue
    cont = input("\nDo you want to continue playing? (yes/no): ").lower()
    if cont != 'yes':
        break

print("\nGame over! Thank you for playing.")
