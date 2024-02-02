from django.shortcuts import render

posts = [
    {
        'author': 'Deepanshu',
        'title': 'Iron Man',
        'content': 'Technology',
        'date_posted': 'Feburary 2, 2024'
    },
    {
        'author': 'Rishi',
        'title': 'War Machine',
        'content': 'Weapons',
        'date_posted': 'Feburary 1, 2024'
    }
]

def home(request):
    context = {
        'posts': posts    #key - value
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
