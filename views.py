from django.shortcuts import render
# Create your views here.
posts=[
    {
        'title':'Baahubali2',
        'author':'pravallika',
        'content':'super',
        'date_posted':'October 24,2018'
    },
    {
        'title':'Baahubali1',
        'author':'architha',
        'content':'super',
        'date_posted':'October 25,2018'
    }
]
def home(request):
    context={
        'posts':posts
    }

    return render(request,'review/home.html',context)
def about(request):
    return render(request,'review/about.html',{'title':'About'})

