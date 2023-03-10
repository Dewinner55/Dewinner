from django.http import Http404
from rest_framework.views import APIView

from main.models import Task
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.
# 2 вида вьюшак
# function based view
# class based view(APIview, generics, ViewSet)
#
# @api_view(['GET', "POST"])
# def tasks_list_create_view(request):
#     if request.method == 'GET':
#         queryset = Task.objects.all()
#         task_serializers = serializers.Task_list_serializers(instance=queryset, many=True)
#         return Response(task_serializers.data, status=200)
#     else:
#         serializer = serializers.Task_detail_serializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def task_detail_view(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#     except Task.DoesNotExist:
#         return Response(f"Такой {pk} id нет!", status=404)
#     if request.method == "GET":
#         serializer = serializers.Task_detail_serializers(instance=task)
#         return Response(serializer.data, status=200)
#     elif request.method in ('PUT', 'PATCH'):
#         if request.method == 'PUT':
#             serializer = serializers.Task_detail_serializers(instance=task, data=request.data)
#         else:
#             serializer = serializers.Task_detail_serializers(instance=task, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     else:
#         task.delete()
#         return Response({'msg': 'Seccessfully deleted!'}, status=204)


# @api_view(['GET'])
# def tasks_list(request):
#     queryset = Task.objects.all()
#     task_serializers = serializers.Task_list_serializers(instance=queryset, many=True)
#     return Response(task_serializers.data, status=200)
#
# @api_view(['GET'])
# def task_detail(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         serializer = serializers.Task_detail_serializers(instance=task)
#         return Response(serializer.data, status=200)
#     except Task.DoesNotExist:
#         return Response(f"This task with {pk} id does not exist!", status=404)
#
# @api_view(["POST"])
# def task_create(request):
#     serializer = serializers.Task_detail_serializers(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)
#
# @api_view(["PUT", "PATCH"])
# def task_update(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         if request.method == "PUT":
#             serializer = serializers.Task_detail_serializers(instance=task, data=request.data)
#         else:
#             serializer = serializers.Task_detail_serializers(instance=task, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     except Task.DoesNotExist:
#         return Response(f"This task with {pk} id does not exist!", status=404)
#
# @api_view(["DELETE"])
# def task_delete(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         task.delete()
#         return Response({'msg': 'Seccessfully deleted!'}, status=204)
#     except Task.DoesNotExist:
#         return Response(f"Task, with {pk} id, does not exist!", status=404)

# ПИШЕМ ВЬЮШКИ НА КЛАССССАААААХХХХ
# class based view (APIView)
# class TaskListCreateView(APIView):
#     def get(self, request):
#         queryset = Task.objects.all()
#         serializer = serializers.TaskListSerializers(instance=queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = serializers.TaskDetailSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=202)
#
#
# class TaskDetailApiView(APIView):
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             raise Http404(f'Task, with {pk} id, does not exist!')
#
#     def get(self, request, pk):
#         queryset = self.get_object(pk)
#         serializer = serializers.TaskDetailSerializers(instance=queryset)
#         return Response(serializer.data, status=200)
#
#     def patch(self, request, pk):
#         queryset = self.get_object(pk)
#         serializer = serializers.TaskDetailSerializers(instance=queryset, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=206)
#
#     def put(self, request, pk):
#         queryset = self.get_object(pk)
#         serializer = serializers.TaskDetailSerializers(instance=queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#
#     def delete(self, request, pk):
#         queryset = self.get_object(pk)
#         queryset.delete()
#         return Response({'Удаленно'}, status=204)

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    # serializer_class = serializers.TaskDetailSerializers

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.TaskListSerializers
        return serializers.TaskDetailSerializers


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskDetailSerializers


