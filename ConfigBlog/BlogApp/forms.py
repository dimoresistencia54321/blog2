from .models import Post

from django import forms



class FormularioPost(forms.ModelForm):

    class Meta: 
        model= Post 
        fields= [ 'title', 'description', 'body',  'author', 'category']
        Widgets= {
            'title' : forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.TextInput(attrs={'class': 'form-control', }), 
            'body': forms.Textarea(attrs={'class': 'form-control', }),
            'author': forms.Select(attrs= {'class': 'form-cotrol '}),
            'category': forms.Select(attrs= {'class': 'form-cotrol '}),
        }