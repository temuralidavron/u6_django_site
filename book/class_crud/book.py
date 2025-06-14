from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from book.forms import BookForm
from book.models import Book


# class BookCreateView(View):
#     def get(self, request):
#         form = BookForm()
#         print('shoxa qalbi qaynoq')
#         return render(request, 'book/book_create.html', {'form': form})
#
#     def post(self, request):
#         form = BookForm(request.POST)
#         print('shoxa qalbi muz')
#         if form.is_valid():
#             form.save()
#             return redirect('book:book-list')
#
#         return render(request, 'book/book_create.html', {'form': form})

#
# class BookListView(View):
#     def get(self, request):
#         books = Book.objects.all().order_by('-updated_at')
#         return render(request, 'book/book_list.html', {'books': books})

#
# class BookDetailView(View):
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         context = {
#             'book': book,
#         }
#         return render(request, 'book/book_detail.html', context)

# class BookUpdateView(View):
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         form = BookForm(instance=book)
#         return render(request, 'book/book_create.html', {'form': form})
#
#     def post(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book:book-list')
#         return render(request, 'book/book_create.html', {'form': form})

#
# class BookDeleteView(View):
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         context = {
#             'book': book,
#         }
#         return render(request, 'book/delete_book.html', context)
#
#     def post(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         book.delete()
#         return redirect('book:book-list')


from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from book.models import Book


class BookListView(ListView):
    print('baxtli bolalik shoxa ')
    model = Book
    context_object_name = 'books'
    template_name = 'book/book_list.html'


class BookCreateView(CreateView):
    print("shoxaning ko'z yoshlari")
    form_class = BookForm
    template_name = 'book/book_create.html'
    success_url = reverse_lazy('book:book-list')


class BookDetailView(DetailView):
    print("shoxa qizlarni ajali")
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'
    pk_url_kwarg = 'pk'


class BookUpdateView(UpdateView):
    print("shoxa yaxshiyam bola ")
    model = Book
    form_class = BookForm
    template_name = 'book/book_create.html'
    success_url = reverse_lazy('book:book-list')
    pk_url_kwarg = 'pk'

class BookDeleteView(DeleteView):
    print('shoxa delete')
    model = Book
    context_object_name = 'book'
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('book:book-list')
    pk_url_kwarg = 'pk'



