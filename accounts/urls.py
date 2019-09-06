from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('',views.home,name='home'),
    path('profile/<int:pk>/',views.profile, name='profile'),
  	path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('comments/<int:pk>/',views.comments, name='comments'),
  	path('savecomment/<int:pk>/',views.savecomment, name='savecomment'),
    path('replycomments/<int:pk>/',views.replycomments, name='replycomments'),
    path('replysavecomment1/<int:pk>/',views.replysavecomment1, name='replysavecomment1'),
    path('replysavecomment/<int:pk>/',views.replysavecomment, name='replysavecomment'),
  	path('search',views.search,name='search'),
  	path('autocomplete',views.autocomplete,name='ajax_autocomplete'),
  	path('followers_page/<int:pk>/',views.followers_page, name='followers_page'),
  	path('following_page/<int:pk>/',views.following_page, name='following_page'),
    path('about/',views.about,name='about'), 
]
