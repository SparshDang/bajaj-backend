from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse

def getView(request):
    return JsonResponse({
        "operation_code" : 1
    })

class MainView(APIView):
    def get(self, request):
        return Response({"operation_code" : 1})
    
    def post(self, request):
        get_data = request.data
        data_ = get_data.get("data",None)
        numbers = []
        alphabets = []
        highest_alphabet = []
        for i in data_:
            if i.isdigit():
                numbers.append(i)
            else:
                alphabets.append(i)
                if len(highest_alphabet) > 0:
                    if i.lower() > highest_alphabet[0].lower():
                        highest_alphabet = [i]
                else:
                    highest_alphabet = [i]

        data = {
            "user_id":"sparsh_dang_22bct10093",
            "email":"dang.sparsh01@gmail.com",
            "is_success":True,
            "numbers":numbers,
            "alphabets":alphabets,
            "highest_alphabets":highest_alphabet
        }
        return Response(data)