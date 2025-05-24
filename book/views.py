from django.db.models.aggregates import Sum, Max, Avg
from django.shortcuts import render, redirect

from book.forms import AuthorForm, BookForm
from book.models import Book, Author


# def book_list(request):
#     books = Book.objects.all()
#     context = {
#         'books': books
#     }
#     return render(request, 'book/book_list.html', context)
#
#
# def create_book(request):
#     title = request.POST.get('title')
#     description = request.POST.get('description')
#     price = request.POST.get('price')
#     if title and description and price:
#         Book.objects.create(
#             title=title,
#             description=description,
#             price=price
#         )
#         return redirect('list')
#
#     return render(request, 'book/book_create.html')
#
#
# def detail_book(request, pk):
#     book = Book.objects.get(pk=pk)
#     context = {
#         'book': book
#     }
#     return render(request, 'book/book_detail.html', context)
#
#
# def title_book(request):
#     book = Book.objects.filter(title='salom').first()
#     context = {
#         'book': book
#     }
#     return render(request, 'book/title.html', context)
#
#
# def update_book(request, pk):
#     book = Book.objects.get(pk=pk)
#
#     title = request.POST.get('title', book.title)
#     description = request.POST.get('description', book.description)
#     price = request.POST.get('price', book.price)
#     if request.method == 'POST':
#         if title and description and price:
#             book.title = title
#             book.description = description
#             book.price = price
#             book.save()
#             return redirect('list')
#     context = {
#         'book': book
#
#     }
#     return render(request, 'book/update_book.html', context)
#

# def delete_book(request, pk):
#     book = Book.objects.get(pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('list')
#     context = {
#         'book': book
#
#     }
#     return render(request, 'book/delete_book.html', context)


# author crud function


def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/author_list.html', context)



def create_author(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('author-list')

    else:
        form=AuthorForm(request.POST)

    return render(request,'author/author_create.html',{'form':form})


def update_author(request,pk):
    author=Author.objects.filter(pk=pk).first()
    if request.method=="POST":
        form=AuthorForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')


    else:
        form=AuthorForm(instance=author)
    return render(request,'author/author_create.html',{'form':form})

# BOOK CRUD
def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/book_list.html', context)



def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # print(form)
            return redirect('book-list')

    else:
        form=BookForm(request.POST)

    return render(request,'book/book_create.html',{'form':form})


def update_book(request,pk):
    book=Book.objects.filter(pk=pk).first()
    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')


    else:
        form=BookForm(instance=book)
    return render(request,'book/book_create.html',{'form':form})




def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    context = {
        'book': book

    }
    return render(request, 'book/delete_book.html', context)



def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book/book_detail.html', context)





def unversal_orm(request):
    books = Book.objects.all()
    book_filter=Book.objects.filter(price__gt=12)
    obj_count=Book.objects.last()
    book_price=book_filter.aggregate(Sum('price'))['price__sum']
    java_list=list(range(1,100000))
    price_list_filter=Book.objects.filter(price__in=java_list)

    print(book_price)
    context = {
        'kuyov': books,
        'filters': book_filter,
        'obj_count': obj_count,
        'book_price': book_price,
        'price_list_filter': price_list_filter,
    }
    return render(request, 'book/unversal_orm.html', context)




