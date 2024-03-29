from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer,PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, generics, permissions
from .permissions import IsOwnerOrReadOnly




# class ProjectList(generics.ListAPIView):
#     projects = Project.objects.all()
#     serializer_class = ProjectSerializer
#     filter_fields = ('category', 'is_open')
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('category', 'owner')

#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def perform_create(self,serializer):
#         serializer.save(supporter=self.request.user)

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        # ordered_querset = sorted(Project.objects.all(), key=lambda p: p.raised)
        projects = Project.objects.all() #Query the database for all projects
        if request.data.get("category"):
            projects = projects.filter(category=request.data.get("category"))
        if request.data.get("owner"):
            projects = projects.filter(owner=request.data.get("owner"))
        serializer = ProjectSerializer(projects, many=True) # Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered.
        return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self, request):
        serializer = ProjectSerializer(data=request.data) #use the data that user has given
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):       
        try:                #only get the object
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):                     # go in the project
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk) #tells me which project we want to change
        data = request.data  #modification that the user is making
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class PledgeList(APIView):
#     def get(self, request):
#         pledges = Pledge.objects.all()
#         serializer = PledgeSerializer(pledges, many=True)
#         return Response(serializer.data)

    # def post(self, request):
    #     serializer = PledgeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_201_CREATED
    #         )

    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )


class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self,serializer):
        serializer.save(supporter=self.request.user)


# class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
   
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly
#     ]

#     # def get_object(self, pk):       
#     #     try:                #only get the object
#     #         pledge = Pledge.objects.get(pk=pk)
#     #         self.check_object_permissions(self.request, pledge)
#     #         return pledge
#     #     except Pledge.DoesNotExist:
#     #         raise Http404

#     queryset = Pledge.objects.all()
    # serializer_class = PledgeDetailSerializer

    # def get_object(self):
    #     return self.request.user

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def get_object(self, pk):       
        try:                #only get the object
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):                     # go in the project
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk) #tells me which project we want to change
        data = request.data  #modification that the user is making
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
