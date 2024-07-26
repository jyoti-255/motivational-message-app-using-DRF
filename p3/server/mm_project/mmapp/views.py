from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import choice

@api_view(["GET"])
def home(request):
    msgs = [
        "Believe in yourself.",
        "Stay focused, stay.",
        "Dream, believe, achieve.",
        "You can do.",
        "Never give up.",
        "Be the best.",
        "Stay positive, always.",
        "Push your limits.",
        "Keep moving forward.",
        "Dream big, act.",
        "Embrace the journey.",
        "Be fearless, persist.",
        "Challenge yourself daily.",
        "Your time is now.",
        "Believe, achieve, succeed."
    ]
    m = choice(msgs)
    return Response({"m": m})
