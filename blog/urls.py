from django.urls import path

from .views import(
    IdeaListView,
)


urlpatterns = [
    path('', IdeaListView.as_view(), name = 'blog-home'),
    # path('about/', , name = 'about-home'),
]