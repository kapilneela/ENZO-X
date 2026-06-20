from core.engine import Enzo

enzo=Enzo()

print("ENZO-X Started")

while True:
    user=input("You > ")

    if user.lower()=="exit":
        break

    response=enzo.think(user)

    print("Enzo >",response)
