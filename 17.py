e = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
f = []
ee = ""
names = ["vladi", "diana", "otir", "ofir"]
if "otir" in names:
    print("otir in name ")
if not ee:
    print("assad")
print(type(e))
if type(e) is list:
    print("e is list")
if isinstance(e, list):
    print("e is a list")
if len(e) > 8:
    print("enough items")

if e:
    print("e is not empty")
if not f:
    print("f is empty")