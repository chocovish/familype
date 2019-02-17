from django.urls import path
from . import views

urlpatterns = [
    path("userretrive/<phone>/", views.UserRetriveView.as_view()),
    path("usercreate/", views.UserCreateView.as_view()),
    path("userhasparent/", views.UserHasParent.as_view()),
    path("invitemember/", views.InviteMember.as_view()),
    path("familymemberlist/", views.FamilyMemberList.as_view()),
    path("familydetail/", views.FamilyDetail.as_view()),
]