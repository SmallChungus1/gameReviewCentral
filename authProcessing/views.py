from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import gamesCollection
from .models import userCollection
#django password hash from stackoverflow: https://stackoverflow.com/questions/25098466/how-to-store-django-hashed-password-without-the-user-object
from django.contrib.auth.hashers import make_password, check_password

# hashed_pwd = make_password("123")
# print("hashed password: ", hashed_pwd)
#check_password("plain_text",hashed_pwd)  # returns True
# Create your views here.

print("at authProcessing View")
def connectionTest(request):
    return HttpResponse("<h1>connected<h1>")

def userLoginProcess(request):
    if request.method == 'POST':
        username = request.POST["loginUsername"]
        password = request.POST["loginPassword"]
        userData = userCollection.find_one({'username':username})
        dbUsername = userData['username']
        dbUserpassword = userData['password']
        if(not userData):
           print("login failed: username not found")
           return redirect("/login")
    else:
        print("warning: authProcessing functions only accepts POST requests")
        
    if(username == dbUsername and check_password(password,dbUserpassword)):
        print('userAuth Passed')
        request.session['sessionUsername'] = username
        return redirect('/')
    else:
        
        print('login failed: incorrect passwrod')
        return redirect('/login')
    

def userRegProcessing(request):
    if request.method == 'POST':
        username = request.POST["signUpUserName"]
        password = request.POST["signUpPassword"]
        confirmPassword = request.POST["signUpPasswordConfirm"]
        currentUsers = userCollection.find()
    else:
        print("warning: authProcessing functions only accepts POST requests")
    
    for user in currentUsers:
        if(user['username'] == username):
            errorMsg = "Regsitration error: userName already exists"
            print(errorMsg)
            return redirect('/login')
    if(password == confirmPassword):
        hashedPassword = make_password(password)
        if(userCollection.insert_one({'username':username,'password':hashedPassword,})):
            print("user registration success")
            request.session['sessionUsername'] = username
            return redirect ('/')
        else:
            errorMsg = "Regsitration error: could not create account. Errors with insertion process to mongoDB"
            return redirect('/login')
        
    else:
        errorMsg = "Registration error: entered passwords do not match"
        print(errorMsg)
        
        print('login failed: incorrect passwrod')
        return redirect('/login')
    
def userLogout(request):
    try:
        del request.session["sessionUsername"]
    except KeyError:
        pass
    return redirect('/')
    
