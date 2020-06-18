from django.urls import path
from . import views
from .views import redirect_view

urlpatterns = [
    path('',views.home,name='home'),
    path('parent/',views.parent,name='parent'),
    path('doc/',views.doc,name='doc'),
    path('form/',views.redirect_view,name='redirect_view'),
    path('form/result/',views.submit,name='submit'),
    path('About/',views.About,name='About'),
    # path('contact_us/',views.contact_us,name='contact_us'),
    path('',views.back,name='back'),
    path('',views.b,name='b')
    # path('')
]