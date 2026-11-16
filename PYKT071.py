import pickle

with open("DATA1.in", "rb") as f:
    a = pickle.load(f)

print(type(a))
print(a[:10])