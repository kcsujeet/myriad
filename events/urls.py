from django.urls import path
from events.views import *

app_name = 'events'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    ##homepage
    path('', HomePageView.as_view(), name="home"),

    ##Evetn Create/Update
    path('create/', EventCreate.as_view(), name="event_create"),
    path('update/<int:pk>', EventUpdate.as_view(), name="event_update"),

]