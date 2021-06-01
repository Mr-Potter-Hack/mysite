from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'author','body', 'snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'This is The Title Of Your Post'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'user','type':'hidden'}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':'This is the Short Detail About Blog'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'This is the body of your post'}),

     }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'This is The Title Of Your Post'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'This is the body of your post'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            
        }