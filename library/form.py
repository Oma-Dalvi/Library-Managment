from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import NewAdmin,Member,Book,Issued_book_db,return_book_db
from django import forms


class AdminForm(UserCreationForm):
    class Meta:
        model = NewAdmin
        fields = ['email','first_name','last_name','password1','password2']


# Creating Form to add Member
class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields='__all__'
    
# Creating Form to add Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'



# Creating Issued_book Form
class IssuedForm(forms.ModelForm):
    class Meta:
        model = Issued_book_db
        fields = ['member','book']

class Return_book_form(forms.ModelForm):
    class Meta:
        model=return_book_db
        fields = '__all__'