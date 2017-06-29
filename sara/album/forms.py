from django import forms
from sara.album.models import Album,Song

class AlbumForm(forms.ModelForm):
	class Meta:
		model=Album
		fields=['logo','title','artist','genre','details']
class SongForm(forms.ModelForm):
	class Meta:
		model=Song
		fields=['song_title','file']