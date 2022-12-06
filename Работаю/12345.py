a = [1, 3, 3, 3, 2, 2, 5, 5, 2, 2, 2, 2]
key = 
new_passage = 0
max_passage = 0
for score in a:
    if score == key:
        if new_passage != max_passage:
            new_passage += 1
        else:
            new_passage +=1
            max_passage = new_passage

    else:
        new_passage = 0
print(max_passage)