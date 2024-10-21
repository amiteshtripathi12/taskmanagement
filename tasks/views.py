from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, Customuser  
from .serializers import *
from rest_framework import generics


# API for creating a user
class CreateUserView(generics.CreateAPIView):
    queryset = Customuser.objects.all()
    serializer_class = CustomuserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# API for getting the list of users
class UserListView(generics.ListAPIView):
    queryset = Customuser.objects.all()
    serializer_class = CustomuserSerializer

# API for creating a task and assigning it to users
@api_view(['POST'])
def create_new_task(request):
    task_serializer = TaskSerializer(data=request.data)
    if task_serializer.is_valid():
        task_serializer.save()
        return Response(task_serializer.data, status=status.HTTP_201_CREATED)
    return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API for assigning a task to multiple users
@api_view(['POST'])
def assign_users_to_task(request, task_id):
    try:
        existing_task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    user_ids = request.data.get('user_ids', [])
    if not user_ids:
        return Response({'error': 'No users specified'}, status=status.HTTP_400_BAD_REQUEST)

    assigned_users = Customuser.objects.filter(id__in=user_ids)
    existing_task.assigned_users.set(assigned_users)  
    existing_task.save()

    return Response({'message': 'Users assigned to task successfully'}, status=status.HTTP_200_OK)

# API to retrieve tasks assigned to a specific user
@api_view(['GET'])
def retrieve_user_tasks(request, user_id):
    try:
        target_user = Customuser.objects.get(id=user_id)
    except Customuser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user_tasks = target_user.tasks.all() 
    task_serializer = TaskSerializer(user_tasks, many=True)
    return Response(task_serializer.data, status=status.HTTP_200_OK)
