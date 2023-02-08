from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailListView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TurnirListView(generics.ListAPIView):
    queryset = Turnir.objects.all()
    serializer_class = TurnirSerializer


class TurnirDetailListView(generics.RetrieveUpdateAPIView):
    queryset = Turnir.objects.all()
    serializer_class = TurnirSerializer


class CoachListView(generics.ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class CoachDetailListView(generics.RetrieveUpdateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankDetailListView(generics.RetrieveUpdateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class AchieveEventsListView(generics.ListAPIView):
    queryset = AchieveEvents.objects.all()
    serializer_class = AchieveEventsSerializer


class AchieveEventsDetailListView(generics.RetrieveUpdateAPIView):
    queryset = AchieveEvents.objects.all()
    serializer_class = AchieveEventsSerializer


class NewsImageListView(generics.ListAPIView):
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer


class AchieveImageListView(generics.ListAPIView):
    queryset = AchieveEventsImage.objects.all()
    serializer_class = AchieveEventsImageSerializer

