with open("shopping_list.txt", "w",encoding = "utf-8") as f:
    f.write("milk\n")
    f.write("eggs\n")
    f.write("bread\n")

with open("shopping_list.txt","r",encoding = "utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")
