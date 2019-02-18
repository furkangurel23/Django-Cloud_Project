from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('groups/', views.groups, name='groups'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('file/<int:pk>', views.FileDetailView.as_view(), name='file-detail'),
    path('folders/', views.file, name='folders'),
    path('folder/new/', views.FolderCreateView.as_view(), name='folder-create'),
    path('folder/<int:pk>/update/', views.FolderUpdateView.as_view(), name='folder-update'),
    path('folder/<int:pk>/delete/', views.FolderDeleteView.as_view(), name='folder-delete'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<int:pk>', views.ContactDetailView.as_view(), name='contract-detail'),
    path('folder/<int:pk>', views.FolderDetailView.as_view(), name='folder-detail'),
    path('share/<int:pk>', views.SharedFileDetailView.as_view(), name='share-detail'),
    path('file/new/', views.FileCreateView.as_view(), name='file-create'),
    path('file/move/', views.FileFolderCreate.as_view(), name='file-folder-create'),
    path('file/<int:pk>/update/', views.FileUpdateView.as_view(), name='file-update'),
    path('file/<int:pk>/delete/', views.FileDeleteView.as_view(), name='file-delete'),
    path('contactCreate/', views.ContactCreateView.as_view(), name='contactCreate'),
    path('contacts/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact-delete'),
    path('share/', views.ShareCreateView.as_view(), name='share-user'),
    path('groupCreate/', views.GroupCreateView.as_view(), name='group-create'),
    path('groupFill/', views.FillGroupView.as_view(), name='group-fill'),

]

"""urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('folders/', views.file, name='folders'),
    path('folder/<int:pk>/', views.FolderDetailView.as_view(), name='folder-detail'),
    path('folder/new/', views.FolderCreateView.as_view(), name='folder-create'),
    path('folder/<int:pk>/update/', views.FolderUpdateView.as_view(), name='folder-update'),
    path('folder/<int:pk>/delete/', views.FolderDeleteView.as_view(), name='folder-delete'),
    path('folder/<int:pk1>/file/<int:pk2>/', views.FileDetailView.as_view(), name='file-detail'),
]"""