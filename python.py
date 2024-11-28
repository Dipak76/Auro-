import openai
import docker
from django.db import models
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.generic.websocket import WebsocketConsumer
from django.urls import path
import json

# --- Challenge Model ---
class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)

# --- Leaderboard Model ---
class Leaderboard(models.Model):
    user = models.CharField(max_length=50)
    score = models.IntegerField()

# --- AI Challenge Generation ---
def generate_challenge(skill_level):
    openai.api_key = 'your_openai_api_key'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a {skill_level} coding challenge.",
        max_tokens=200
    )
    return response['choices'][0]['text']
