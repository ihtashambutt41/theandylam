from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from apiclient.discovery import build
from os import environ
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
    #The api key is loaded in from environment vaiables
    api_key = environ['GOOGLE_API_KEY']
    service = build('books', 'v1', developerKey=api_key)
    book_request = service.volumes().list(source='public', q=search_text)
    response = book_request.execute()

    books_found = response.get('totalItems', 0)
    book_list = response.get('items', [])

    query = SearchForm()

    context = {
        'search_text' : search_text,
        'books_found' : books_found,
        'book_list' : book_list,
        'query' : query,
    }

    return render(request, 'results.html', context=context)
