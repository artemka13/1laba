from django.contrib import admin
from django.urls import include, path

from polls import views
from polls.views import show_home

from django.conf import settings
from django.conf.urls.static import static
from polls.views import RegisterView

from polls.views import CustomLoginView
from polls.forms import LoginForm
from django.contrib.auth import views as auth_views
from polls.views import ResetPasswordView
from polls.views import profile

urlpatterns = [
    path('', show_home, name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('user/', include(('polls.urls', 'user'), namespace='user')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='user/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name='password_reset_complete'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
