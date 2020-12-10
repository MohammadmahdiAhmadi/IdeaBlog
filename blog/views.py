from django.shortcuts import render

from django.views.generic import(
    ListView,
    DetailView,
)
from .models import Idea



class IdeaListView(ListView):
    model = Idea
    template_name = 'blog/home.html'
    context_object_name = 'ideas'
    ordering = ['-date_posted']
    paginate_by = 2
    


class IdeaDetailView(DetailView):
    model = Idea
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    

