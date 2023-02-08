from rest_framework import serializers
from.models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"



class TurnirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turnir
        fields = "__all__"


class SportsmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportsmen
        fields = "__all__"


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class AchieveEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchieveEvents
        fields = "__all__"


class AchieveEventsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchieveEventsImage
        fields = "__all__"


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = "__all__"

