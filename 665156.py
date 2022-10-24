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
    i = input("Skriv in ditt användarnamn: ")
    userlist = list(users.values())
    print(userlist)
    if i in userlist[0]:
        print(f'Välkommen {i}')
    else:
        addUser(i)
        print(f'Välkommen ny spelare {i}')
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
        svar = input("Svar: ")
        print()
        if svar == (questionsAndRebuses[r][1]):
            print("Du klarade den")
            print(f"+10 poäng! Din nya poäng är: {addPoints(u, 10)}")
            return users[u][1]

        else:
            print()
            print("Fel svar, försök igen!")
            print(f"-1 poäng för fel svar! Din nya poäng är: {subPoints(u, 1)}")
            print()
            clue(r, u)
            
    
def clue(r, user):
    while True:
        c = input("Vill du ha en ledtråd? ja/nej: ")
        print()
        if c == "ja":
            print()
            while True:
                s = input("Lätt, mellan eller svår? ")
                if s == "lätt":
                    print(f"Ledtråd: {questionsAndRebuses[r][2]}")
                    print(f"Det kostade 5 poäng! Din nya poäng är: {subPoints(user, 5)}")
                    print()
                    break
                if s == "mellan":
                    print(f"Ledtråd: {questionsAndRebuses[r][3]}")
                    print(f"Det kostade 4 poäng! Din nya poäng är: {subPoints(user, 4)}")
                    print()
                    break
                if s == "svår":
                    print(f"Ledtråd: {questionsAndRebuses[r][4]}")
                    print(f"Det kostade 3 poäng! Din nya poäng är: {subPoints(user, 3)}")
                    print()
                    break
                elif s == "nej":
                    break
            break
        elif c == "nej":
            break



cont = {'a':'Yes', 'b':'No'}

def continueAfterLeaderboard(prompt, choices):
    print(prompt)
    for x in choices:
        print(f'  {x}) {choices[x]}')
    while True:
        i = input()
        if i == 'b':
            break
        elif i == 'a':
            main()

def leaderboard():
    usernamesandpoints = dict((users.values()))
    toppoints = sorted(usernamesandpoints.values(), reverse = True)  
    print("Topplista")
    n = 1
    for x in toppoints:
        username = [user for user, points in usernamesandpoints.items() if points == x]
        print (f" {n}) {username}: {x}")
        n = n + 1
        
        

choice = {'A':'New player', 'B':'Show leaderboard', 'C':'Terminate game'}

def menu(title, prompt, options):
    print(title)
    print()
    for x in options:
        print(f'  {x}) {options[x]}')
    print()
    while True:
        x = input(prompt)
        if x  == 'C':
            print("Goodbye!")
            break
        elif x == 'B':
            leaderboard()
            if continueAfterLeaderboard('Want to play?', cont) == 'b':
                break
            break
        elif x == 'A':
            print('New player')
            main()

def main():
    u = login()
    for x in questionsAndRebuses:
        rebus(x, u)
    menu("Choices:", "What's your choice? ", choice)

main()