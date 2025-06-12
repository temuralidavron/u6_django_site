from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import When, Case, Value, Q
from django.db.models.aggregates import Sum, Max, Avg, Count
from django.db.models.fields import CharField
from django.shortcuts import render, redirect

from accounts.utils import check_user, admin_required
from book.forms import AuthorForm, BookForm
from book.models import Book, Author, Category, Product


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
            return redirect('book:author-list')

    else:
        form=AuthorForm(request.POST)

    return render(request,'author/author_create.html',{'form':form})


def update_author(request,pk):
    author=Author.objects.filter(pk=pk).first()
    if request.method=="POST":
        form=AuthorForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            return redirect('book:author-list')


    else:
        form=AuthorForm(instance=author)
    return render(request,'author/author_create.html',{'form':form})

# BOOK CRUD
def book_list(request):
    books = Book.objects.all()
    q=request.GET.get('q')
    print(q)
    if q:
        books=Book.objects.filter(
            Q (title__icontains=q) |
            Q(description__icontains=q) |
            Q(price__icontains=q)

        )
    paginator = Paginator(books, 2)
    page = request.GET.get('page')
    books = paginator.get_page(page)

    context = {
        'books': books,
    }
    return render(request, 'book/book_list.html', context)

# @admin_required
@check_user
@permission_required('book.add_book', raise_exception=True)
def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # print(form)
            return redirect('book:book-list')

    else:
        form=BookForm(request.POST)

    return render(request,'book/book_create.html',{'form':form})

@check_user
def update_book(request,pk):
    book=Book.objects.filter(pk=pk).first()
    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:book-list')


    else:
        form=BookForm(instance=book)
    return render(request,'book/book_create.html',{'form':form})



@login_required
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book:book-list')
    context = {
        'book': book

    }
    return render(request, 'book/delete_book.html', context)


@login_required
def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book/book_detail.html', context)





def unversal_orm(request):
    cat=Category.objects.annotate(pro=Count('products'))  # har bir obj uchun
    dic=Category.objects.filter(products__price__gt=150000).distinct()

    kuyov=Product.objects.annotate(
        price_label=Case(
            When(price__lte=10000, then=Value('Arzon')),
            When(price__lte=50000, then=Value('O‘rtacha')),
            default=Value('Qimmat'),
            output_field=CharField()
        )
    )
    new=Category.objects.filter(products__is_active=True)
    shoxa=Product.objects.only('name','price')
    defer=Product.objects.defer('price')  # kechikish
    old=Product.objects.values_list('name','price')



    context = {
        'cat': cat,
        'dic': dic,
        'kuyov': kuyov,
        'new': new,
        'shoxa': shoxa,
        'defer': defer,
        'old': old,

    }
    return render(request, 'book/unversal_orm.html', context)




