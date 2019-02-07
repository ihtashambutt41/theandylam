from apiclient.discovery import build
from os import environ

def search_for_books(search_text):
        # Get API key stored in an environment variable
        api_key = environ['GOOGLE_API_KEY']

        # Querying the Google Books API with the users search text
        service = build('books', 'v1', developerKey=api_key)
        book_request = service.volumes().list(source='public', q=search_text)
        response = book_request.execute()

        # Storing the response from the API
        total_books = response.get('totalItems', 0)
        book_list = response.get('items', [])

        return (book_list, total_books)