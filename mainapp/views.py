from django.shortcuts import render
from .serializers import UserCreateSerializer,InviteMemberSerializer,MemberDetailSerializer,FamilyDetailSerializer
from .models import User
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
#from django.db.models.Model import DoesNotExist

class UserRetriveView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    lookup_field = 'phone'
    serializer_class = MemberDetailSerializer

class UserCreateView(CreateAPIView):
    model=User
    serializer_class = UserCreateSerializer

class UserHasParent(APIView):
    def get(self,request):
        parents= request.user.family.user_set.filter(usertype='Parent')
        if parents: return Response({"hasparents":True},status=200)
        else: return Response({"hasparents":False},status=404)

class InviteMember(APIView):
    def post(self, request):
        if not request.user.is_authenticated: return Response({'message':'You Must Login First'},status=401)
        phno = InviteMemberSerializer(request.data).data['phone']
        print(phno)
        u = User.objects.create(phone=phno,username=phno,setup_completed=False,family=request.user.family)
        return Response(status=201)

class FamilyMemberList(ListAPIView):
    def get_queryset(self):
        if not self.request.user.is_authenticated: return {}
        return self.request.user.family.user_set.all()
    serializer_class = MemberDetailSerializer

class FamilyDetail(APIView):
    def get(self, request):
        if not request.user.is_authenticated: return Response({'message':'You Must Login First'},status=401)
        family = request.user.family
        return Response(FamilyDetailSerializer(family).data)