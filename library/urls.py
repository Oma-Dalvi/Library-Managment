from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('register',v.register_new_admin,name="register"),   
    path('login',v.login_admin,name="login"),
    path('logout',v.logoutuser,name="logout"),
    path('Main_lib',v.Main,name="Main_lib"),
    path('addMember',v.addMember,name="addMember"),
    path('addBook',v.addBook,name="addBook"),
    path('issueBook/<int:id>',v.issued_book,name="issueBook"),
    path('returnBook/<int:id>',v.return_book,name="returnBook"),
    path('delete/<int:id>',v.deleteBook,name="delete"),
]