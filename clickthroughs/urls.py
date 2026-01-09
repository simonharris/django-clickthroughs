from django.urls import path

from . import views


app_name = 'clickthroughs'

urlpatterns = [

    path('go', views.ClickthroughView.as_view(), name='go'),

]
