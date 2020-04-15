from django import forms
from user_list_app.models import Users

# custom validator:
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name need to start with z")

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 50) #(validators=[check_for_z]
    last_name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 200)

    class Meta:
        model = Users
        fields = '__all__'