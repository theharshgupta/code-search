from firebase import firebase
import pyrebase

firebase = firebase.firebase.FirebaseApplication("https://pythondbtest-c2b75.firebaseio.com/")

data = {'Filename': 'file_test',
        'Function_Name': 'function_test',
        'Docstring': 'docstring_test'}

result = firebase.post('pythondbtest-c2b75/Functions', data)
print(result)