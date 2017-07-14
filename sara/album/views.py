from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from sara.album.models import Album,Song
from sara.album.forms import AlbumForm,SongForm



def index(request):
	if request.user.is_authenticated():
		albums=Album.objects.filter(user=request.user)
		return render(request,'album/index.html',{'albums':albums})
	else:
		return render(request,'album/main.html')


def addAlbum(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			form=AlbumForm(request.POST,request.FILES)
			if form.is_valid():
				post=form.save(commit=False)
				post.user=request.user
				post.save()
				return redirect("/")
		else:
			form=AlbumForm()
		return render(request,'album/create.html',{'form':form})
def details(request,album_id):
	if request.user.is_authenticated():
		detailObject=Album.objects.get(pk=album_id)
		songObject=Song.objects.filter(album=detailObject)
		return render(request,'album/details.html',{'detailObject':detailObject,'songObject':songObject})

def remove_album(request,album_id):
	if request.user.is_authenticated():
		if request.method=="POST":
			deleteObject=Album.objects.get(pk=album_id)
			deleteObject.delete()
			return redirect("/")
	else:
		return render(request,'album/main.html')
#def edit(request,album_id):

def add_song(request,album_id):
	if request.user.is_authenticated():
		detailObject=get_object_or_404(Album,pk=album_id)
		if request.method=="POST":
			form=SongForm(request.POST,request.FILES)
			if form.is_valid():
				post=form.save(commit=False)
				post.album=Album.objects.get(pk=album_id)
				post.save()
				return redirect('/')
		else:
			form=SongForm()
		return render(request,'album/song.html',{'form':form})
def remove_song(request,album_id,song_id):
	if request.user.is_authenticated():
		if request.method=='POST':
			detailObject=get_object_or_404(Album,pk=album_id)
			deleteObject=Song.objects.get(pk=song_id)
			deleteObject.delete()
			return render(request,'album/details.html',{'detailObject':detailObject})
	else:
		return render(request,'album/main.html')