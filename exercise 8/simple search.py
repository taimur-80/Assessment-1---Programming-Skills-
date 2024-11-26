names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Enter the name you want to search for: ")

if search_name in names:
    print(f"Found {search_name}!")
else:
    print("Not found")