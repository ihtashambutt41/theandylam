from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import SearchForm
from .search_google_books import search_for_books

class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    # Runs this when a valid form input is received
    def form_valid(self, form):
        search_text = form.data['search_query']
        return HttpResponseRedirect(reverse('results', args=(search_text,)))

class ResultsView(ListView):
    template_name = 'results.html'
    total_books = 0
    book_list = []
    search_text = ''

    def get_queryset(self):
        self.search_text = self.kwargs['search_text']
        (self.book_list, self.total_books) = search_for_books(self.search_text)
        return self.book_list

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Adding the search results to the context dictionary
        context.update({
            'search_text' : self.search_text,
            'total_books' : self.total_books,
            'book_list' : self.book_list,
        })
        return context