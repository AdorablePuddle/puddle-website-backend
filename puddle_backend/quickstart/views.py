from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .app import system

import time

def ping_response():
    return Response(data = {"responseTime" : time.time()}, status = status.HTTP_200_OK)

# Create your views here.

@api_view(http_method_names = ["GET"])
def ping(request : Request):
    return ping_response()

@api_view(http_method_names = ["GET"])
def get_question(request : Request):
    question_number = request.query_params.get("")