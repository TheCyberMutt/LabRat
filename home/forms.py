from django import forms
from .models import Profile, BlogPost


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image',)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image', 'content1', 'image1', 'content2', 'image2', 'content3', 'image3', 'content4', 'image4', 'content5', 'image5', 'content6', 'image6')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'slug': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),

        }
