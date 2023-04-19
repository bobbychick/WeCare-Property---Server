from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
import os
import openai

# Create your views here.

openai.api_key = "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"


class Ad_Generator(APIView):
    def get(self, request):
        result = "This is a test output - to return an actual response, uncomment the API code"

        # if request.method == "GET":
        #     home_attributes = request.POST.get("attributes")
        #     response = openai.Completion.create(
        #         model="text-davinci-003",
        #         prompt=self.generate_ad(home_attributes),
        #         temperature=0.6,
        #         max_tokens=200,
        #     )
        #     result = response.choices[0].text
        #     print(result)
        print(result)
        return Response(result)

    def generate_ad(self, home_attributes):

        rooms = 3
        baths = 2
        proximity = ["countdown", "sylvia park", "botany", "cafes"]
        school_zone = ["macleans college", "pakurange college", "sunnyhills primary"]
        transport = ["trains", "airport", "bus"]
        result = f"Create a 100 word ad for a house that is to be rented in Auckland, New Zealand. The house will have the following attributes. \
            Rooms: {rooms}\
            Baths: {baths}\
            Within proximity to: {','.join(proximity)}\
            It is also in these school zones: {','.join(school_zone)}\
            It also has easy access to these forms of transport: {','.join(transport)}"

        return result
