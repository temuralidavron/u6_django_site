from django.urls import path
from book.views import book_list, create_book, detail_book, update_book, delete_book, author_list, \
    create_author, update_author, unversal_orm

urlpatterns=[
    path('',book_list,name='book-list'),
    path('create/',create_book,name='create-book'),
    path('update/<int:pk>/', update_book, name='update-book'),
    path('detail/<int:pk>/',detail_book,name='detail-book'),
    path('delete/<int:pk>/',delete_book,name='delete-book'),


    # author crud url
    path('author-list/',author_list,name='author-list'),
    path('author-create/',create_author,name='author-create'),
    path('author-update/<int:pk>/',update_author,name='author-update'),

    #
    path('unver/',unversal_orm),
]