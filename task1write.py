import pickle

T1 = {12, 15, 18, 21, 24, 27, 30}

with open("setOfThreeMultiples.dat", "wb") as f:
    pickle.dump(T1, f)
