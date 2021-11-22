import difflib

villagers = {
    "Abigail": {
        "Loves": [
            "Amethyst",
            "Banana Pudding",
            "Blackberry Cobbler",
            "Chocolate Cake",
            "Golden Pumpkin",
            "Magic Rock Candy",
            "Pearl",
            "Prismatic Shard",
            "Pumpkin",
            "Rabbit's Foot",
            "Spicy Eel",
        ],
        "Likes": ["Decent"],
        "Neutral": ["Meh"],
        "Dislikes": ["Bad"],
        "Hates": ["Gross"],
    },
    "Alex": {
        "Loves": [
            "Complete Breakfast",
            "Golden Pumpkin",
            "Magic Rock Candy",
            "Pearl",
            "Prismatic Shard",
            "Rabbit's Foot",
            "Salmon Dinner",
        ],
        "Likes": ["Decent Alex"],
        "Neutral": ["Meh Alex"],
        "Dislikes": ["Bad Alex"],
        "Hates": ["Gross Alex"],
    }
    # too lazy to add the rest
}


usrvill = input("Enter villager: ")
usrrea = input("Enter response: ")

def output():
    if not villagers.get(usrvill):
        print(f"{usrvill} is not a valid villager, rip...")
        return

    if not villagers[usrvill].get(usrrea):
        print(f"{usrrea} is not a valid reaction? hello??!")
        return

    for item in villagers[usrvill][usrrea]:
        print(item)
        return


output()
