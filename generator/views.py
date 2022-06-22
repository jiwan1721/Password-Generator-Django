from django.shortcuts import render
from django.http import HttpResponse
import random,string

# Create your views here.
def randpassword():
        number = string.digits
        punc=string.punctuation
        randomPassword = list(string.ascii_letters+number+punc)

        length_password = random.randrange(8,15)
        random.shuffle(randomPassword)
        password = ''.join(random.choice(randomPassword)for i in range(length_password))
        last_value=password[-1]
        if last_value in number or last_value in punc :
            print('------')
            return randpassword()
        else:
            return password
def home(request):
    password=randpassword()
    return render(request, 'generator/home.html', {'password':password})

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    password=randpassword()

    return render(request, 'generator/password.html', {'password':password})
