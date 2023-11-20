from django.shortcuts import render,redirect
from vast.models import Course,Student,teacher
import  os
from django.contrib.auth import login
from django.contrib.auth.models import User,auth
from django.contrib import messages


from django.contrib.auth.decorators import login_required
# Create your views here.
def home3(request):
    
    return render(request,'start.html')
def reg(request):
    
    return render(request,'reg.html')
def home(request):
    
    return render(request,'home.html')
def home1(request):
    
    
    return render(request,'login.html')
def course(request):
    return render(request,'course.html')
def add_coursedb(request):
    if request.method=='POST':
        course_name=request.POST.get('cname')
        fee=request.POST.get('fee')
        course=Course(course_name=course_name,fee=fee)
        course.save()
        return redirect('course')


    return render(request,'course.html')


def student(request):

    courses=Course.objects.all()
    return render(request,'student.html',{'course':courses})

def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        jdate=request.POST.get('date')
        sel=request.POST.get('sel')
        course1=Course.objects.get(id=sel)
        student=Student(student_name=student_name,age=age,address=address,jdate=jdate,course=course1)
        student.save()
        return redirect('/')
# def showstudent(request):
#     return render(request,'studentshow.html')

def showteacher(request):
    student=teacher.objects.all()
    return render(request,'admintech.html',{'student':student})
# def editprofile(request):
#     return render(request,'teachedit.html')
def profile(request):
    return render(request,'profile.html')
def techhome(request):
    return render(request,'techhome.html')

def showstudent(request):
    student=Student.objects.all()
    return render(request,'studentshow.html',{'students':student})

def update(request,pk):
    c=Course.objects.all()
    prd=Student.objects.get(id=pk)
    return render(request,'updatestudent.html',{'prd':prd,'c':c})

# def update_product(request,pk):
#     if request.method=='POST':
#         prd=Student.objects.get(id=pk)
#         prd.product_name=request.POST.get('product_name')
#         prd.price=request.POST.get('price')
#         prd.quantity=request.POST.get('quantity')
#         if len(request.FILES)!=0:
#             if len(prd.image)>0:
#                 os.remove(prd.image.path)
#             prd.image =request.FILES.get('image')
#         prd.save()
#         return redirect('show')
#     return render(request,"update.html")
def delete(request,pk):
    prd=Course.objects.get(id=pk)
    prd.delete()
    return redirect('showstudent')
def delete2(request,pl):
    prdt=teacher.objects.get(id=pl)
    prdt.delete()
    return redirect('showteacher')


def reg(request):
   
    courses=Course.objects.all()
    return render(request,'reg.html',{'course':courses})
  

def addteacher(request):
    if request.method=='POST':
        first_name=request.POST['frname']
        last_name=request.POST['lrname']
        username=request.POST['urname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        address=request.POST['address']
        age=request.POST['age']
        phn=request.POST['phn']
        sel=request.POST.get('sel')
        course1=Course.objects.get(id=sel)
        # if 'image' in request.FILES:
        #     photo=request.FILES['image']
        # else:
        #     photo='ab.jpg'
        image=request.FILES.get('image')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This USer name Exists...!!')
                return redirect('reg')
            else:

                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email
                )
                
                tech=teacher(user=user,age=age,address=address,number=phn,image=image,course=course1)
                tech.save()
                user.save()

        else:
            messages.info(request,'Password doesnt Match...!!')
            print("password is not Matching")
            return redirect('reg')
        return redirect('login1')
    else:
        return render(request,'login1')

def profile(request):
    profile = teacher.objects.get(user=request.user)
    profile1 = Course.objects.get(id=profile.course_id)
    name = request.user.first_name
    lname = request.user.last_name
    username = request.user.username
    age = profile.age
    image =profile.image
    
    email = request.user.email
    qul = profile.number
    cor = profile1.course_name
    add = profile.address
    context = {
        'name':name,'lname':lname,'username':username,'age':age,'mail':email,'qual':qul,'address':add,'cor':cor,'image':image
    }
    return render(request,'profile.html',context)



def editprofile(request):
    profile = teacher.objects.get(user=request.user)
    pro1 = Course.objects.get(id=profile.course_id)
    name = request.user.first_name
    lname = request.user.last_name
    username = request.user.username
    age = profile.age
    
    
    email = request.user.email
    qul = profile.number
    cor = pro1.course_name
    # co = profile.course_id
    
    add = profile.address
    course = Course.objects.all()
    photo = profile.image
    context = {
        'photo':photo,'course':course, 'cor':cor ,'name':name,'age':age,'mail':email,'qual':qul,'address':add,'lname':lname,'username':username
    }
    return render(request,'teachedit.html',context)

def login1(request):
    return render(request,'login.html')
def login2(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
            # request.session['uid']=user.id
                auth.login(request,user)
                messages.info(request, f'welcome {username}')
                return redirect('techhome')
        else:
            messages.info(request,'Invalid UserName of Password.Try Again')
            return redirect('login1')
        
    return redirect('home3')



def updatestd(request,p):
    if request.method=='POST':
        std=Student.objects.get(id=p)
        std.student_name=request.POST.get('name')
        std.address=request.POST.get('address')
        std.age=request.POST.get('age')
       
        
        std.jdate=request.POST.get('date')
        std.course_id = request.POST['course']
        std.save()
        return redirect('showstudent')
    return render(request,"edit_student.html")

def updatetec(request):
    if request.method == 'POST':
        usr = User.objects.get(id=request.user.id)
        tec = teacher.objects.get(user_id=request.user.id)
        # pro1 = Course.objects.get(id=tec.course_id)
        usr.first_name = request.POST['frname']
        usr.last_name = request.POST['lrname']
        usr.username = request.POST['urname']
        usr.email = request.POST['email']
        tec.address = request.POST['address']
        tec.age = request.POST['age']
   
        tec.contactnumber = request.POST['phn']
        if len(request.FILES)!=0:
            if len(tec.image)>0:
                os.remove(tec.image.path)
            tec.image = request.FILES['image']
       
        # tec.course_id = request.POST['cours']
        usr.save()
        tec.save()
        return redirect('techhome')

# @login_required(login_url='login1')
def logout1(request):
    # if request.user.is_authenticated:
    # request.session['uid']=''
        auth.logout(request)
        return redirect('login1')   