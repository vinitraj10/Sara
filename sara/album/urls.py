from django.conf.urls import url
from sara.album import views
app_name='album'
urlpatterns =[

	url(r'^add/',views.addAlbum,name='addAlbum'),
	url(r'^details/(?P<album_id>[0-9]+)$',views.details,name='details'),
	url(r'^details/(?P<album_id>[0-9]+)/remove_album$',views.remove_album,name='remove_album'),
	url(r'^album/(?P<album_id>[0-9]+)/add/song/',views.add_song,name="add_song"),
	url(r'^album/(?P<album_id>[0-9]+)/remove_song/(?P<song_id>[0-9]+)$',views.remove_song,name='remove_song'),
	#url(r'^details/(?P<album_id>[0-9]+)/edit_album$',views.edit_album,name='edit_album'),
]