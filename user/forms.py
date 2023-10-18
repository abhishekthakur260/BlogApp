from djagno.contrib.auth.forms import UserCreationForm
from djagno.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username','email','password1','password2']:
            self.fileds[fieldname].help_text =None
    
        
        