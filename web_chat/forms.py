
'''
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs ={"class":"form-control"}),
            'email':forms.EmailInput(attrs ={"class":"form-control"}),
            'password1':forms.PasswordInput(attrs ={"class":"form-control"}),
            'password2':forms.PasswordInput(attrs ={"class":"form-control"}),
            }
      
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs ={"class":"form-control"})
        self.fields['email'].widget = forms.EmailInput(attrs ={"class":"form-control"})
        self.fields['password1'].widget = forms.PasswordInput(attrs ={"class":"form-control"})
        self.fields['password2'].widget = forms.PasswordInput(attrs ={"class":"form-control"})
'''