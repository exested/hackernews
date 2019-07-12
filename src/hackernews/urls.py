from django.contrib import admin
from django.urls import path

from .entries.api import EntryList

urlpatterns = [
    path('admin/', admin.site.urls),

    path('posts', EntryList.as_view(), name='post_list')
]
