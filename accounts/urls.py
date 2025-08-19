from django.urls import path

from accounts import views

urlpatterns=[
    path('',views.register,name="register"),
    path('google/login/', views.google_login, name='google_login'),
    path('google/login/callback/', views.google_callback, name='google_callback'),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('chat/',views.email_chat,name="chat"),
    path('forget/',views.forget_password_view,name="forget_password"),
    path('reset/',views.done_view,name="reset"),
    path('transaction/',views.transaction_post,name="transaction_post"),
    path('profile/',views.profile_view,name="profile"),
    path('set_ps/',views.set_password_view,name="set_password"),
]