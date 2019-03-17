from firebase import firebase
from crypting import cryptage


def connect(username,password):
    firebaseObj = firebase.FirebaseApplication('https://python-test-f77c7.firebaseio.com/', None)
    result = firebaseObj.get('/Users/', '')
    connSucc = False

    for key in result:
        
        if result[key]['Username'] == username and  result[key]['Password'] == password:
            print('Connection successful')
            connSucc = True
            break;
    return connSucc
