from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail

from accounts.models import RoleChoice, CustomUser
from book.forms import AuthorForm

from django.contrib.auth.models import User, Group, Permission

from django.contrib.contenttypes.models import ContentType

from book.models import Book
from config import settings


def check_user(func):
    def wrapper(request,*args, **kwargs):
        result = func(request,*args,**kwargs)
        if result:
            if request.user.is_authenticated:
                return result

        return redirect("login")

    return wrapper




def admin_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.role==RoleChoice.ADMIN:
                # print(request.user.role,'salomlar')
                return func(request,*args,**kwargs)
            return HttpResponse("Sizga mumkin emas ")
    return wrapper


# group,_=Group.objects.get_or_create(name='Tahrirchi')
# user=CustomUser.objects.get(username='man')
# user.groups.add(group)
#
#
#
#
#
# content_type = ContentType.objects.get_for_model(Book)
#
# permission = Permission.objects.get(codename='add_book')
#
#
#
# user = CustomUser.objects.get(username='man')
#
# user.user_permissions.add(permission)
#
#
# # Guruhga ruxsat berish
#
# group = Group.objects.get(name='Tahrirchi')
#
# group.permissions.add(permission)

# email send massage




def send_simple_email():

    send_mail(

        subject="Bugun bayram",

        message="SHu sababli darsimiz ertalab 8:30 da boshlanadi",

        from_email=settings.EMAIL_HOST_USER,

        recipient_list=["aliyertemur95@gmail.com","sinyor7414@gmail.com",'qambaraliyevrozimuhammad48@gmail.com',"eshjav86@gmail.com"],

        fail_silently=False,

    )


from django.core.mail import EmailMultiAlternatives


# def send_html_email():
#     subject = "HTML email sinovi"
#
#     from_email = settings.EMAIL_HOST_USER,
#
#     to = ["aliyertemur95@gmail.com","sinyor7414@gmail.com",'qambaraliyevrozimuhammad48@gmail.com',"eshjav86@gmail.com"],
#
#     text_content = "Bu oddiy email matni."
#
#     html_content =f"""
#     <!DOCTYPE html>
# <html lang="uz">
# <head>
#     <meta charset="UTF-8">
#     <title>Bayram Muborak! {text_content}</title>
# </head>
# <body style="font-family: Arial, sans-serif; background-color: #f7f7f7; padding: 20px;">
#     <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 10px; padding: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
#         <h2 style="color: #2c3e50; text-align: center;">🎉 Bayramingiz Muborak! 🎉</h2>
#         <p style="font-size: 16px; color: #333333; line-height: 1.6;">
#             Hurmatli foydalanuvchi,
#         </p>
#         <p style="font-size: 16px; color: #333333; line-height: 1.6;">
#             Sizni ushbu quvonchli bayram bilan chin qalbimdan muborakbod etamiz!
#             Yaqinlaringiz bilan birga sog‘-salomat, baxtli va omadli kunlarni boshdan kechirishni tilaymiz.
#         </p>
#         <p style="font-size: 16px; color: #333333; line-height: 1.6;">
#             Bayram sizga va oilangizga tinchlik, baraka va muhabbat olib kelsin!
#         </p>
#         <p style="font-size: 16px; color: #333333; line-height: 1.6;">
#             Eng ezgu tilaklar bilan,<br>
#             <strong>Kiberto jamoasi</strong>
#         </p>
#         <div style="text-align: center; margin-top: 30px;">
#             <img src="https://i.imgur.com/UtE7A5r.png" alt="Bayram" style="width: 100%; max-width: 400px; border-radius: 10px;">
#         </div>
#     </div>
# </body>
# </html>
# """
#
#     email = EmailMultiAlternatives(
#         subject=subject,
#         body=text_content,
#         from_email=settings.EMAIL_HOST_USER,
#         to=["aliyertemur95@gmail.com","sinyor7414@gmail.com",'qambaraliyevrozimuhammad48@gmail.com',"eshjav86@gmail.com"])
#
#     email.attach_alternative(html_content, "text/html")
#
#     email.send()
#


def send_html_view(request, subject, to_email, code,username):
    from_email = settings.EMAIL_HOST_USER
    text_content = code
    subject=subject

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h2 style="color: #333333;">Salom!</h2>
            <p style="font-size: 16px; color: #555555;">Parolni tiklash uchun quyidagi koddan foydalaning:</p>
            <div style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; font-size: 20px; text-align: center; font-weight: bold; color: #2c3e50;">
                {code}
            </div>
            <p style="font-size: 16px; color: #555555; margin-top: 20px;">Yoki quyidagi tugmani bosib parolingizni tiklashingiz mumkin:</p>
            <a href="http://127.0.0.1:8000/accounts/reset/?name={username}" 
            <b>{code}</b>
               style="display: inline-block; padding: 12px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
               Parolni tiklash
            </a>
            <p style="font-size: 14px; color: #999999; margin-top: 30px;">Agar bu siz emas bo‘lsangiz, bu xabarni e'tiborsiz qoldiring.</p>
        </div>
    </body>
    </html>
    """

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=[to_email] if isinstance(to_email, str) else to_email
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

    return HttpResponse("Email yuborildi!")

