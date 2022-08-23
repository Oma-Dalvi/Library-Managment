from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class NewAdmin(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

# Creating Database for Member
# To add New Entry
class Member(models.Model):
    roll_no = models.CharField(max_length=10,unique=True)
    FullName = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=10)
    total_books_due=models.IntegerField(default=0)
    email=models.EmailField(unique=True)
    pic=models.ImageField(blank=True, upload_to='profile_image')
    def __str__(self):
        return str(self.roll_no)


# Creating Database for Book
# To add New Book
class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi')
        ]

    title=models.CharField(max_length=30,default="")
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    publisher = models.CharField(max_length=40,default="")
    Total_count = models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return str(self.title)+"["+str(self.isbn)+']'

# Creating Issued_book Database
class Issued_book_db(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,default="Not Specified")
    # issue_date = models.DateTimeField(null=True,blank=True)
    # return_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.member.roll_no+" Issued"+self.book.title
        
class return_book_db(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,default="Not Specified")

    def __str__(self):
        return self.member.roll_no+" Return Book"+self.book.title
