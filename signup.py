from firebase import firebase
from crypting import cryptage

def signup(username,password,email):  
    firebaseObj = firebase.FirebaseApplication('https://python-test-f77c7.firebaseio.com/', None)  
    data = {
            'Username': username,
            'Password': password,
            'Email' : email,
            'Score': 0,
        }

    result = firebaseObj.post('/Users',data)
    print('Subscription successful')

