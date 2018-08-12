suits = ["hearts","clubs","diamonds","spades"]
values = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
count = 0
for value in values:
    for suit in suits:
        print(value + " of "+ suit)
        count = count +1
print(count)
