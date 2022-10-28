questionsAndRebuses = {1: ["Vem är bäst?", "Jag är bäst", "Du", "Jag", "Vi"], 2: ["rebus2","svar2", "lättledtråd2", "mellanledtråd2", "svårledtråd2"], 3: ["rebus3", "svar3", "lättledtråd3", "lättledtråd3", "svårledtråd3"]}

users = {'user1':['Tove', 100]}
testuser = 0

def addUser(n):
    addlist = []
    addlist.append(n)
    addlist.append(100)
    users[f"user{len(users.keys())+1}"] = addlist
    return users

def login():
    i = input("Type your username: ")
    userlist = list(users.values())
    if i in userlist[0]:
        print(f'Welcome {i}')
    else:
        addUser(i)
        print(f'Welcome new player {i}')
    return f'user{len(users.keys())}'

def addPoints(user, p):
    users[user][1] += p
    return users[user][1]

def subPoints(user, p):
    users[user][1] -= p
    return users[user][1]

def rebus(r, u):
    while True:
        print(questionsAndRebuses[r][0])
        print()
        svar = input("Answer: ")
        print()
        if svar == (questionsAndRebuses[r][1]):
            print("Congratulations, you did it!")
            print(f"+10 points! Your new score is: {addPoints(u, 10)}")
            print()
            return users[u][1]

        else:
            print()
            print("Wrong answer, try again!")
            print(f"-1 points for wrong answer! Your new score is: {subPoints(u, 1)}")
            print()
            clue(r, u)
            
    
def clue(r, user):
    while True:
        c = input("Do you want a clue? yes/no: ")
        print()
        if c == "yes":
            print()
            while True:
                s = input("Easy, medium or hard? ")
                if s == "easy":
                    print(f"Clue: {questionsAndRebuses[r][2]}")
                    print(f"It cost you 5 points! Your new score is: {subPoints(user, 5)}")
                    print()
                    break
                if s == "medium":
                    print(f"Clue: {questionsAndRebuses[r][3]}")
                    print(f"It cost you 4 points! Your new score is: {subPoints(user, 4)}")
                    print()
                    break
                if s == "hard":
                    print(f"Ledtråd: {questionsAndRebuses[r][4]}")
                    print(f"It cost you 3 points! Your new score is: {subPoints(user, 3)}")
                    print()
                    break
                elif s == "no":
                    break
            break
        elif c == "no":
            break



cont = {'a':'Yes', 'b':'No'}

def continueAfterLeaderboard(title, prompt, choices):
    print(title)
    print()
    for x in choices:
        print(f'  {x}) {choices[x]}')
    print()
    while True:
        i = input(prompt)
        if i == 'b' or i == 'a':
            return i

        
def leaderboard():
    usernamesandpoints = dict((users.values()))
    toppoints = sorted(usernamesandpoints.values(), reverse = True)
    print("Leaderboard")
    n = 1
    toppoints2 = [i for n, i in enumerate(toppoints) if i not in toppoints[:n]]
    for x in toppoints2:
        username = [user for user, points in usernamesandpoints.items() if points == x]
        if len(username) == 1:
            print (f" {n}) {username[0]}: {x}")

        else:
           g = " and ".join([", ".join(username[:-1]),username[-1]] if len(username) > 2 else username)
           print(f" {n}) {g}: {x}")
        n += 1
        

choice = {'a':'New player', 'b':'Show leaderboard', 'c':'Terminate game'}

def menu(title, prompt, options):
    print(title)
    print()
    for x in options:
        print(f'  {x}) {options[x]}')
    print()
    while True:
        x = input(prompt)
        if x  == 'c':
            print('Goodbye!')
            break
        elif x == 'b':
            leaderboard()
            print()
            c = continueAfterLeaderboard('Want to play?', 'Answer: ', cont)
            if c == 'b':
                print()
                print('Goodbye!')
                break
            elif c == 'a':
                print()
                print('New player')
                main()
            break
        elif x == 'a':
            print()
            print('New player')
            main()

def main():
    u = login()
    for x in questionsAndRebuses:
        rebus(x, u)
    menu("Choices:", "What's your choice? ", choice)

main()