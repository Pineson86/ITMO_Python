from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        if name and email:
            User.objects.create(name=name, email=email)
            return redirect("index")  # Перенаправляем на главную страницу

    users = User.objects.all()  # Получаем всех пользователей для отображения
    return render(request, "user_data_app/index.html", {"users": users})

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect("index")
