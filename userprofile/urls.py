from django.urls import path
from .views import *

urlpatterns = [
    # path("<slug>/",ProfileView.as_view(),name = 'profileview'),
    path("search/<location>/",ProfileFilterView.as_view(),name = 'profilefilterview'),
    path("",UserProfileView.as_view(), name = 'userprofileview'),
    path("docprofile/<slug>/",ProfileView.as_view(), name = 'profileview'),

]
