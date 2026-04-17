from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage.as_view()),
    path('home',views.homepage.as_view()),


    path('create',views.displayform),


    path('add',views.blog_add),
    path('display',views.display_blog),
    path('edit/<int:id>',views.edit_blog),
    path('updatedata/<int:id>',views.update_blog),
    path('delete/<int:id>',views.delete_blog),
    path('search',views.search_blog),

]
