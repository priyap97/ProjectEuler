with open("problem22names.txt", "r") as textfile:
    names = sorted(textfile.readline().split(","))
    total = 0
    i = 1
    for name in names: 
        name_score = 0
        for char in name: 
            if char != '"':
                name_score = name_score + ord(char) - 64
                # print(f'name {name} has char {char} and name_score is {name_score}')
        total = total + (name_score * i)
        i = i + 1 
        # print(f'name {name} has score {name_score} and total is {total}')
        # input()
    print(total)