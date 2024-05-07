"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from search import views as search_views
from forum import views as forum_views
from logs import views as logs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', users_views.register, name= 'signup'),
    path('profile/', users_views.profile, name= 'profile'),
    path('signin/', auth_views.LoginView.as_view(redirect_authenticated_user = True,
        template_name = 'users/signin.html'), name= 'signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'website/logout.html'), name= 'logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), 
        name= 'password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), 
        name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
        (template_name = 'users/password_reset_confirm.html'), name= 'password_reset_confirm'),
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view
        (template_name = 'users/password_reset_complete.html'), name= 'password_reset_complete'),
    path('change-password/', users_views.change_password, name= 'change_password'),
    path('search/', search_views.search, name= 'searchpage'),
    path('advanced-search/', search_views.advanced_search, name= 'advanced_searchpage'),
    path('details/<str:cve_id>/', search_views.details, name= 'detailspage'),
    path('pdf/<str:cve_id>/', search_views.get_pdf, name= 'pdfpage'),
    path('advanced-search-details/<str:cve_id>/', search_views.advancedsearch_details, name= 'advanceddetailspage'),
    path('forum/', forum_views.forum, name= 'forumpage'),
    path('forum-create/', forum_views.thread_create, name= 'forumcreate'),
    path('forum/<int:thread_id>/', forum_views.thread_detail, name= 'forumidspage'),
    path('forum/<int:thread_id>/edit/', forum_views.thread_edit, name= 'forumedit'),
    path('forum/<int:thread_id>/delete/', forum_views.thread_delete, name= 'forumdelete'),
    path('forum/<int:thread_id>/add-comment/', forum_views.add_comments, name= 'addcomment'),
    path('forum/<int:comment_id>/edit-comment/', forum_views.edit_comments, name= 'editcomment'),
    path('forum/<int:comment_id>/delete-comment/', forum_views.delete_comments, name= 'deletecomment'),
    path('forum/<int:comment_id>/add-reply/', forum_views.add_reply, name= 'addreply'),
    path('forum/<int:reply_id>/edit-reply/', forum_views.edit_reply, name= 'editreply'),
    path('forum/<int:reply_id>/delete-reply/', forum_views.delete_reply, name= 'deletereply'),
    path('history/', logs_views.history, name= 'historypage'),
    path('updates/', search_views.updates, name= 'updatepage'),
    path('', include('website.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)