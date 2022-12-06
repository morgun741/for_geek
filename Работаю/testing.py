#with open("scoreboard.txt", "a") as f:

with open("scoreboard.txt", "r") as f:
    content = f.readlines()
    for line in content:
        for i in line:
            if i.isdigit() == True:
                print(i)


