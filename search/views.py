from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import SearchForm

# Create your views here.
def search(request):
    if request.method == 'POST':
        query = SearchForm(request.POST)
        if query.is_valid():
            search_text = query.data['search_query']
            return HttpResponseRedirect(reverse('results', args=(search_text,)))
    else:
        query = SearchForm()

    query = SearchForm()
    return render(request, 'search.html', {'query' : query})

def results(request, search_text):
    return render(request, 'results.html', {'search_text' : search_text})
