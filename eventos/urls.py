from django.urls import path

from . import views

app_name = 'eventos'
urlpatterns = [
    # ex: /
    path('', views.EventIndexView.as_view(), name='index'),
    # ex: /eventos/list
    path('list/', views.EventListView.as_view(), name='list'),
    # ex: /eventos/2/detail
    path('<int:pk>/detail/', views.EventDetailView.as_view(), name='detail'),
    # ex: /eventos/molinete/3/detail
    path('molinete/<int:pk>/detail', views.MolineteDetailView.as_view(),
        name='molinete-detail'),
    # ex: /eventos/register
    path('register-event/', views.EventRegisterView.as_view(), name='register-event'),
    path('register-molinete/', views.MolineteRegisterView.as_view(),
        name='register-molinete'),
    path('register-credential/', views.CredentialRegisterView.as_view(),
        name='register-credential'),
    path('read-credential/', views.CredentialReadView.as_view(),
        name='read-credential'),

    ]
