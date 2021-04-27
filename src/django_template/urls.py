from django.urls import path
from . import views

urlpatterns = [
    path(
        "home",
        views.home_view,
        name="home_view"
    )
]

#Add Django site authentication urls (for login, logout, password management)
from django. urls import include
urlpatterns += [
    
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.urls import path

from .views import SignUpView


urlpatterns += [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]
