import os

test = os.listdir()

for item in test:
    if item.endswith(".pdf"):
        os.remove(item)
