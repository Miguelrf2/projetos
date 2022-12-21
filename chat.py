import random 
import os
from sty import fg, bg, ef, rs

idServer = ''

for i in range(0,9):
    idServer += str(random.randint(0, 9))
inIntId = int(idServer)

roots = [
    {'name': 'room 1', 'numberPeople': 0, 'connection': 0, 'maxConnection': 5 , 'id': inIntId},   
    {'name': 'room 2', 'numberPeople': 0, 'connection': 0, 'maxConnection': 5, 'id': inIntId}
]

rootsNum = len(roots)
user = dict()
password = ''
nameRoot = []
rootFind = ''
messages = [{}]
indice = 0
isOrNot = False

for i in range(0,9):
    password += str(random.randint(0,9))

for i in roots:
    nameRoot.append(i['name'])

def createUser(name):
    user['name'] = name
    user['id'] = id(user)
    user['password'] = password
    user['serverIdLogged'] = int()

def requestCall(y):
    def desconnect(x):
        print(f'you have been disconnected from {x}')
        user['serverIdLogged'] = ''
        print('When you wanna join in a chat, write here the name him.\n' )
        for i in roots:
            print(i['name'])

        callToJoin = input('> ').lower() #call 1

        if callToJoin in nameRoot:
            os.system(command='cls')
            isOrNot = True
            return requestCall(callToJoin) 
        else:
            print(False)
    
    def MsgFunction(user):
        message = input('> ')
        os.system(command='cls')

        if isOrNot:
            for i in messages:
                username = i.get('user')
                userMsg = i.get('message')
                print(f': {userMsg}')

        if message == '.exit':
            return desconnect(y) #função pra desconectar o usuário do chat

        else:
            messages.append({'user': user, 'message': message})
            for i in messages:
                username = i.get('user')
                userMsg = i.get('message')
                print(fg.blue + str(username) + ': ' + fg.rs + str(userMsg))

        return MsgFunction(name)

    def joinCall():
        print("You're connected in", y)

        for i in range(0, rootsNum):
            user['serverIdLogged'] = roots[i].get('id')
        print(user['serverIdLogged'])

        for i in range(0, rootsNum): 
            idIsEquale = user['serverIdLogged'] == roots[i].get('id')
            if idIsEquale:
                os.system(command='cls')
                return MsgFunction(name) ###################

    def findCall(x):
        for i in range(0, rootsNum):
            rootFind = roots[i].values()   
            if x in rootFind:
                return joinCall()
        else:
            print('You entered something wrong. Try again.')
            print('When you wanna join in a chat, write here the name him.\n' )
            for i in roots:
                print(i['name'])
                callToJoin = input('> ').lower() #call
                return requestCall(callToJoin)

    return findCall(y)

name = input("What's your name ? \n > ")

if name != '':
    createUser(name)
    print('User created!')
    print('When you wanna join in a chat, write here the name him.\n' )

    for i in roots:
        print(i['name'])

    callToJoin = input('> ').lower() #call
    requestCall(callToJoin)
