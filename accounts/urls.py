from django.urls import path

from accounts import views

urlpatterns=[
    path('',views.register,name="register"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('chat/',views.email_chat,name="chat"),
    path('forget/',views.forget_password_view,name="forget_password"),
    path('reset/',views.done_view,name="reset"),
    path('transaction/',views.transaction_post,name="transaction_post"),
]