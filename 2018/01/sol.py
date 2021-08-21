import functools

with open("input.txt") as f:   
    data = [int(l.strip()) for l in f.readlines()]

val = functools.reduce(lambda s, v: s+v, data)

print(val)
data = [3,3,4,-2,4]
value = 0
history = set()
def find():

    while True:

        for i in data:
            print(i,value)
            print(history)
            if value in history:
                print("HELLO")
                print(value, "seen twice")
                return 

            else: 
                history.add(value)


            value += i
