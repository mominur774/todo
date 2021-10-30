
from django.contrib import admin
from django.urls import path
from item import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AddTodo.as_view(), name="addtodo"),
    path('delete/<int:pk>', views.deleteTodo, name="delete")
]
