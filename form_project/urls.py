
from django.contrib import admin
from django.urls import path
from form_example import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('simple-form/', views.simple_form),
    path('form-example-get/', views.form_example_get),
    path('form-example-post/', views.form_example_post),
    path('name-form/', views.get_name),
    path('contact-form/', views.contact_form),
    path('order-form/', views.order_form)
]
