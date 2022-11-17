from .form import AdminForm
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Issued_book_db, Member,Book,Issued_book_db,return_book_db
from .form import MemberForm,BookForm,IssuedForm,Return_book_form


print("Testing Webhookkkkkkkkkkkkkkk.....")
def home(request):
    return render(request,'home.html')

def register_new_admin(request):
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')
    context = {'form':form}
    return render(request,'resgistration.html',context)


def login_admin(request):
    if request.method =='POST':
        uname = request.POST.get("email")
        passw = request.POST.get("password")
        user = authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return render(request,"Main_lib.html")
        else:
            messages.info(request,'Username or Password is incorrect!!!')
            return render(request,"login.html")
    # context = {"form":f}
    # return render(request,"login.html",context)
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('/')

def Main(request):
    book = Book.objects.all()
    print(book,'--------<<<<<<')
    return render(request,"Main_lib.html",{'book':book})

def addMember(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        form.save()
        return render(request,"Main_lib.html")
    d = {'form':form}
    return render(request,"addMember.html",d)

def addBook(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
        publisher = request.POST['publisher']
        Total_count = request.POST['Total_count']

        books = Book.objects.create(title=title, author=author, isbn=isbn, category=category, publisher=publisher, Total_count = Total_count)
        books.save()
        alert = True
        return render(request, "addBook.html", {'alert':alert})
    return render(request, "addBook.html")


from datetime import timedelta, date
def issued_book(request,id):
    bk_obj = Book.objects.get(id = id)
    # mem_obj = Member.objects.get(id=id)
    if request.method == 'POST':
        if bk_obj.Total_count>0:
            obj = Issued_book_db()
            obj.book = bk_obj
            # obj.member = mem_obj
            bk_obj.Total_count = bk_obj.Total_count-1
            # bk_obj.issue_date = date.today()
            # bk_obj.return_date = date.today() + timedelta(days=5)
            bk_obj.save()
            return render(request,"ThankYou.html")
    elif bk_obj.Total_count==0:
        return HttpResponse("Book is not available...:(")
    else:
        form = IssuedForm()
        context = {'form':form}
        return render(request,"issuedBook.html",context)

def return_book(request,id):
    bk_obj = Book.objects.get(id = id)
    print(bk_obj,'rrrrrr')
    # mem_obj = Member.objects.get(id=id)
    if request.method == 'POST':

        return_book = Return_book_form(request.POST)
        print(return_book,'.....')

        bk_obj.Total_count = bk_obj.Total_count+1
        return_book.save()
        bk_obj.save()
        return render(request,"ThankYou.html")
    else:
        form = IssuedForm()
        context = {'form':form}
        return render(request,"returnBook.html",context)

def deleteBook(request,id):
    book_obj = Book.objects.get(id=id)
    print(book_obj,'_____')
    book_obj.delete()
    return render(request,"ThankYou.html")
