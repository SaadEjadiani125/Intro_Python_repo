contacts = {}

while True:
    answer = input("choose what option you want to do: add(1), search(2), list(3), quit(0): ")
    if answer=="1":
      name = input("Name: ")
      phone = input("Phone: ")
      email = input("Email: ")
      contacts[name] = [phone, email]
      continue

    if answer=="2":
        search = input("Search: ")
        if search in contacts:
            phone, email = contacts[search]
            print(f"{search}: {phone} / {email}")
            continue
        else:
            print(search, "not found")
            continue
    if answer=="3":
        if len(contacts)==0:
            print("No contacts")
            continue
        for name, (phone, email) in sorted(contacts.items()):
            print(f"{name}: {phone} / {email}")
            continue
    
