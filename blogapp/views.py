from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogapp.forms import SignupForm,UploadForm
from blogapp.models import Upload
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def landingpage(request):
    return render(request,'blogapp/landingpage.html')

def home(request):
    return render(request,'blogapp/home.html')

@login_required
def postblog(request):
    return render(request,'blogapp/postblog.html')

@login_required
def viewallblogs(request):
    images = Upload.objects.all().order_by('-upload_date')
    return render(request,'blogapp/viewallblogs.html',{'images':images})

def Signuppage(request):
    signupform = SignupForm()
    mydict = {'signupform':signupform}
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user=signupform.save()
            user.set_password(user.password)
            user.save()
            subject = "Welcome to Pushpak Blog"
            message = "Hello, "+user.first_name+"! Thank you for registering on Pushpak Blogs. We welcome you and wish you Happy Blogging!"
            recipient_list = [user.email]
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            mydict.update({'msg':'Registered Successfully. Welcome mail sent'})
    return render(request, 'blogapp/signup.html',context=mydict)

@login_required
def UploadView(request):
    uploadform = UploadForm()
    mydict = {'uploadform':uploadform}
    if request.method == 'POST':
        uploadform = UploadForm(request.POST,request.FILES)
        if uploadform.is_valid():
            data = uploadform.save(commit=False)
            data.postedby = request.user
            data.save()
            mydict.update({'msg':'Uploaded Successfully'})
    return render(request, 'blogapp/postblog.html', context=mydict)

@login_required
def DetailView(request,id):
    images = Upload.objects.get(id=id)
    #images.delete()
    return render(request,'blogapp/detailview.html',{'images':images})




def DeleteProduct(request,id):
    images = Upload.objects.get(id=id)
    images.delete()
    images = Upload.objects.all().order_by('-upload_date')
    return render(request,'blogapp/viewallblogs.html',{'images':images, 'msg':'Product Successfully Deleted'})
