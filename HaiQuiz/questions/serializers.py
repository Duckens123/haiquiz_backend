from typing import ItemsView
from django.db.models import fields
from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields =('pk','libelle', 'ops1', 'ops2', 'ops3','ops4', 'ans')