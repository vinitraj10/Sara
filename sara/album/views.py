from django.shortcuts import render
from django.http import HttpResponse



def index(request):
	return HttpResponse("This is Album Page")

'''	def addAlbum(request):
		this view will be responsible for adding albums

	def albumDetails(request):
		this will provide the album details 
	def addSongs(request):  
		this is for adding songs and we need to create similar functions for deleting as well

	
'''
