from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
"""
rooms =[
    {
        'id':1,
        'name':'Apprendre python'
    },
    {
        'id':2,
        'name':'Apprendre php'
    },
     {
        'id':3,
        'name':'Apprendre java'
    }
]
"""
def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'salons':rooms})
def room(request,pk):
    """
    room = None  
    for salon in rooms:
        if salon['id'] == int(pk):
            room = salon"""
  
    room = Room.objects.get(id=pk)
    
    return render(request, 'base/room.html',{'salon' :room})   
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        #print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)
# Create your views here.
