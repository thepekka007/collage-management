from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
       path('',views.home3,name='home3'),
       path('home',views.home,name='home'),
        path('reg',views.reg,name='reg'),
           path('addteacher',views.addteacher,name='addteacher'),
           path('login1',views.login1,name='login1'),
            path('login2',views.login2,name='login2'),
  path('techhome',views.techhome,name='techhome'),
path('editprofile',views.editprofile,name='editprofile'),
path('profile',views.profile,name='profile'),

       path('home1',views.home1,name='home1'),
       path('course',views.course,name='course'),
         path('add_coursedb',views.add_coursedb,name='add_coursedb'),
           path('student',views.student,name='student'),
          path('add_studentdb',views.add_studentdb,name='add_studentdb'),
           path('showstudent',views.showstudent,name='showstudent'),
             path('delete/<int:pk>',views.delete,name='delete'),
              path('delete2/<int:pl>',views.delete2,name='delete2'),
               path('update/<int:pk>',views.update,name='update'),
                path('updatestd/<int:p>',views.updatestd,name='updatestd'),
                path('updatetec',views.updatetec,name='updatetec'),
  path('showteacher',views.showteacher,name='showteacher'),
                 path('logout1',views.logout1,name='logout1'),
       #     path('update_student/<int:pk>',views.update_student,name='update_student'),
       # path('login1',views.login1,name='login1'),
       # path('login2',views.login2,name='login2'),
     
]  
