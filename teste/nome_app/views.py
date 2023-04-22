from django.template import loader
from django.http import HttpResponse
from .models import Member
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

# import view sets from the REST framework
from rest_framework import viewsets

from .serializers import MemberSerializer


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# create a class for the Todo model viewsets
class MemberView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = MemberSerializer
 
    # define a variable and populate it
    # with the Todo list objects
    queryset = Member.objects.all()

    @action(detail=True, methods=['Get'])
    def vote(self, request, id=None):
        queryset = Member.objects.filter(pk=id)
        serializer = MemberSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



#class MemberDetailsView(viewsets.ModelViewSet):

#    def retrieve(self,request,pk=None):
#      u = request.member
#      queryset = Member.objects.filter(member=u,id=pk)
#      if not queryset:
#          return Response(status=status.HTTP_400_BAD_REQUEST)
#      else:
#          serializer = MemberSerializer(queryset)
#          return Response(serializer.data,status=status.HTTP_200_OK)