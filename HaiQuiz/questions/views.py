from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import serializers,status

@api_view(['GET'])
def ApiOverview(request):
    api_urls={
        'all_questions': '/',
        'Add': '/add',
        'Update': '/update/pk',
        'Delete': 'question/pk/delete',
    }
    return Response(api_urls)


@api_view(['POST'])
def add_question(request):
    question=QuestionSerializer(data=request.data)

    if Question.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Question already exists')
    if question.is_valid():
        question.save()
        return Response(question.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_questions(request):
    if request.query_params:
        questions=Question.objects.filter(**request.query_params.dict())
    else:
        questions=Question.objects.all()
    if questions:
        data=QuestionSerializer(questions, many=True)
        return Response(data.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_questions(request,pk):
    question=Question.objects.get(pk=pk)
    data=QuestionSerializer(instance=question, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_questions(request, pk):
    question=get_object_or_404(Question, pk=pk)
    question.delete()
    return Response(status=status.HTTP_202_ACCEPTED)