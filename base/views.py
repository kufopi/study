from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic, Message,User

from .forms import RoomForm, UserForm, MyUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    q =request.GET.get('q') if request.GET.get('q')!= None else ''
    topics = Topic.objects.all()[:5]
    topic_count = topics.count()
    rooms =Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q))
    counter = rooms.count()
    stories = Message.objects.filter(Q(room__topic__name__icontains=q)).order_by("-created")[:5]

    context = {'rooms':rooms,
    'topics':topics,
    'counter':counter,
    'stories':stories,
    'topic_count':topic_count}

    return render(request,'base/home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    conversations = room.message_set.all().order_by('-created') #query child objects of room
    guys = room.participants.all()

    if request.method == 'POST':
        body = request.POST.get('body')
        messbody = Message.objects.create(room = room, user=request.user, body=body)
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'conversations':conversations,'guys':guys
    
    }
    return render(request,'base/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    topics = Topic.objects.all()
    word='Create'
    form = RoomForm()

    if request.method == 'POST':
        # interesting way of adding a topic into the database with create form
        topic_name= request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        return redirect('home')
        


    context={'form':form, 'word':word, 'topics':topics}

    return render(request,'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request,pk):
    topics = Topic.objects.all()
    word='Update'
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!")

    if request.method =='POST':
        topic_name= request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        # form = RoomForm(request.POST,instance=room)
        # if form.is_valid():
        #     form.save()
        return redirect('home')
    context={'form': form, 'word':word, 'topics':topics, 'room':room}

    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!")

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request,'base/delete.html', {'obj':room})



def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user= authenticate(request,email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or Password is incorrect")

    context={
        'page':page
    }

    return render(request,'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def joinuser(request):
    page ='join'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Opps! Something smells fishy!!! durin registration')
    context = {
        'form':form
    }
    return render(request, 'base/login_register.html', context)


login_required(login_url='login')
def deleteComment(request,pk):
    comment = Message.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse("You are not allowed here!")

    if request.method == 'POST':
        comment.delete()
        return redirect('home')

    return render(request,'base/delete.html', {'obj':comment})


def userProfile(request,pk):
    boss = User.objects.get(id=pk)
    rooms = boss.room_set.all()
    stories = boss.message_set.all().order_by('-created')[:7]
    hold=[]
    topics =[]
    
    for t in rooms:
        hold.append(t)
    for m in hold:
        if m.topic in topics:
            continue
        else:
            topics.append(m.topic)
    mum=list(set([m.topic for m in hold])) #Shortcut  not used but Sets remove duplicates
    topic_count = len(topics)
    print(mum)
    
    context ={'boss':boss, 'rooms':rooms, 'stories':stories, 'topics':topics, 'topic_count':topic_count

    }

    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def updateUser(request):
    form = UserForm(instance=request.user)
    if request.method=='POST':
        form=UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile' ,pk= request.user.id)

    context={'form':form}
    return render(request,'base/update-user.html', context)



def topicsPage(request):
    q =request.GET.get('q') if request.GET.get('q')!= None else ''
    topics = Topic.objects.filter(name__icontains=q)
    topic_count = topics.count()
    

    context={'topics':topics, 'topic_count':topic_count }
    return render(request,'base/topics.html', context)


def activist(request):
    stories = Message.objects.all().order_by("-created")[:5]
    context={'stories':stories}
    return render(request, 'base/activity.html', context)