import pickle

def divisibleByTwo(n):
    if n % 2:
        return False
    else:
        return True

with open("setOfThreeMultiples.dat", "rb") as f:
    unfilteredSet = pickle.load(f)
filteredSet = [x for x in unfilteredSet if not divisibleByTwo(x)]

print(filteredSet)
