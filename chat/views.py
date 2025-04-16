
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# class ChatAPIView(APIView):
#     def post(self, request):
#         try:
#             message = request.data.get("message", "")

#             response = client.chat.completions.create(
#                 model="gpt-4-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": message}
#                 ]
#             )

#             reply = response.choices[0].message.content
#             return Response({"reply": reply}, status=status.HTTP_200_OK)

#         except Exception as e:
#             print("❌ خطا:", str(e))
#             return Response({"reply": "خطا در پاسخ ❌", "error": str(e)}, status=500)

# def chat_ui(request):
#     return render(request, "chat/chat.html")


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ این ویو صفحه‌ی HTML رو نشون می‌ده
def chat_ui(request):
    return render(request, "chat.html")

# ✅ این ویو API هست
class ChatAPIView(APIView):
    def post(self, request):
        try:
            message = request.data.get("message", "")

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": message}
                ]
            )

            reply = response.choices[0].message.content
            return Response({"reply": reply}, status=status.HTTP_200_OK)

        except Exception as e:
            print("❌ خطا:", str(e))
            return Response({"reply": "خطا در پاسخ ❌", "error": str(e)}, status=500)

