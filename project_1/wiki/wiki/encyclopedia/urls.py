from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_info, name="entry_info"),
    path("wiki/edit_entry/<str:title>/", views.edit_entry, name="edit_entry"),
    path("wiki/save_entry/<str:title>/", views.save_entry, name="save_edited_entry")
]
