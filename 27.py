for i in range(1,101):
    if  i % 7 == 0 or "7"  in str(i):
        continue
    print(i)

names = ["natan", "shay", "ronen", "aaron"]
result = [name.upper() for name in names if "n" in name]
print(result)
