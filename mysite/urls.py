from django.contrib import admin
from django.urls import include, path

from polls import views
from polls.views import show_home

from polls.views import PersonCreateView, PersonUpdateView

urlpatterns = [
    path('user/', include('django.contrib.auth.urls')),
    path('', show_home, name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('user/register/', views.register, name='register'),
    path('user/person/', PersonCreateView.as_view(), name='person'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
]
