from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from apiclient.discovery import build
from os import environ
from .forms import SearchForm

class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    # Runs this when a valid form input is received
    def form_valid(self, form):
        search_text = form.data['search_query']
        return HttpResponseRedirect(reverse('results', args=(search_text,)))

class ResultsView(ListView):
    template_name = 'results.html'

    books_found = 0
    book_list = []
    search_text = ''

    # Needed for the search box at the bottom of results page
    form = SearchForm()

    def get_queryset(self):
        # Get API key stored in an environment variable
        api_key = environ['GOOGLE_API_KEY']

        # Querying the Google Books API with the users search text
        service = build('books', 'v1', developerKey=api_key)
        self.search_text = self.kwargs['search_text']
        book_request = service.volumes().list(source='public', q=self.search_text)
        response = book_request.execute()

        # Storing the response from the API
        self.books_found = response.get('totalItems', 0)
        self.book_list = response.get('items', [])
        return self.book_list

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Adding the search results to the context list
        context['search_text'] = self.search_text
        context['books_found'] = self.books_found
        context['book_list'] = self.book_list
        context['form'] = self.form
        return context