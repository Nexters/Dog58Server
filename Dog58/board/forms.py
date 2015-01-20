from django import forms
from board.models import Board
from ckeditor.widgets import CKEditorWidget

class BoardAdminForm(forms.ModelForm):
	content = forms.CharField(label='', widget=CKEditorWidget())
	class Meta:
        		model = Board