# import os
# import json
# import requests
# from dotenv import load_dotenv
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# chat_history = []  # حافظه چت ساده

# @csrf_exempt
# def chat_view(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             user_message = data.get("message")

#             if not user_message:
#                 return JsonResponse({"error": "No message provided"}, status=400)

#             # اضافه کردن پیام کاربر به تاریخچه
#             chat_history.append({"role": "user", "content": user_message})

#             headers = {
#                 "Authorization": f"Bearer {GROQ_API_KEY}",
#                 "Content-Type": "application/json",
#             }

#             payload = {
#                 "model": "mixtral-8x7b-32768",
#                 "messages": chat_history,
#             }

#             response = requests.post(
#                 "https://api.groq.com/openai/v1/chat/completions",
#                 headers=headers,
#                 json=payload
#             )

#             result = response.json()

#             if response.status_code != 200:
#                 return JsonResponse({"error": result}, status=500)

#             ai_reply = result["choices"][0]["message"]["content"]
#             chat_history.append({"role": "assistant", "content": ai_reply})

#             return JsonResponse({"reply": ai_reply})

#         except Exception as e:
#              import traceback
#              traceback.print_exc()
#              return JsonResponse({"error": str(e)}, status=500)


#     return render(request, "chat.html")
import os
import json
import requests
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

chat_history = []


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message")

            if not user_message:
                return JsonResponse({"error": "No message provided"}, status=400)

            chat_history.append({"role": "user", "content": user_message})

            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "llama3-8b-8192",  # مدل جدید و سالم
                "messages": chat_history
            }

            groq_response = requests.post(GROQ_API_URL, headers=headers, json=payload)

            if groq_response.status_code != 200:
                print("❌ خطا از سمت Groq:", groq_response.json())  # نمایش خطا در کنسول
                return JsonResponse({
                    "error": "Groq API Error",
                    "status": groq_response.status_code,
                    "detail": groq_response.json()
                }, status=500)

            response_data = groq_response.json()
            ai_reply = response_data['choices'][0]['message']['content']
            
            # 👇 چاپ پاسخ در کنسول سرور
            print("✅ پاسخ AI:", ai_reply)

            chat_history.append({"role": "assistant", "content": ai_reply})

            return JsonResponse({"reply": ai_reply})

        except Exception as e:
            print("❌ Exception:", str(e))  # نمایش خطا در کنسول
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "chat.html")
