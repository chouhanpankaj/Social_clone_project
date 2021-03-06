from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):


    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        # fields = '__all__'
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # for customized form label
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'Email address'
