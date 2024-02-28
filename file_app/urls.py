from django.urls import path, re_path

from . import views


urlpatterns = [
    path('journals/', views.JournalOrdersView.as_view(), name='journals'),
    path('journal-type-create', views.JournalTypeCreate.as_view(), name='journal-type-create'),
    path("journal-create/<int:pk>", views.JournalRowCreate.as_view(), name='journal-create'),
    path('journal-list/', views.JournalListView.as_view(), name='journal-list'),
    path('journal-detail/<int:pk>', views.JournalDetailView.as_view(), name='journal-detail')
]