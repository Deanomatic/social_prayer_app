from django.shortcuts import render

posts = [
    {
        'user': 'Dean Smith',
        'title': 'First post',
        'content': 'First post content',
        'date_posted': 'May 9th, 2020'
    },
    {
        'user': 'Yoda',
        'title': 'Second post',
        'content': 'Second post content',
        'date_posted': 'May 11th, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'prayer_wall/home.html', context)

def about(request):
    return render(request, 'prayer_wall/about.html', {'title': 'About'})
