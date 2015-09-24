from django import forms

from .models import User, UserProfile


class SignupForm(forms.Form):
    username = forms.CharField(required=True, label='Username*', widget=forms.TextInput(attrs={'placeholder':'Username','class':'inputText required'}))
    email = forms.EmailField(required=True, label='Email*', widget=forms.TextInput(attrs={'placeholder':'Your email','class':'inputText required'}))
    password = forms.CharField(required=True, label='Choose a Password*', widget=forms.PasswordInput(attrs={'placeholder':'Choose a Password','class':'inputText password required'}, render_value=False))
    confirm_password = forms.CharField(required=True, label='Confirm Password*', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'inputText password required'}, render_value=False))
    artist_type = forms.ChoiceField(choices=UserProfile.TYPES, required=True, label='Artist Type*')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'name', 'artist_name', 'website', 'bio',
            'influences', 'location', 'facebook', 'twitter'
        )

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name','class':'inputText'}),
            'artist_name': forms.TextInput(attrs={'placeholder':'Artist Name','class':'inputText'}),
            'website': forms.TextInput(attrs={'placeholder':'Website','class':'inputText'}),
            'bio': forms.Textarea(attrs={'placeholder':'About The Artist','class':'inputText large'}),
            'influences': forms.TextInput(attrs={'placeholder':'Influences','class':'inputText'}),
            'location': forms.TextInput(attrs={'placeholder':'Location', 'class':'inputText'}),
        }