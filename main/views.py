# main/views.py を以下に更新

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import firebase_admin
from firebase_admin import credentials, auth
from .models import User, ActionItem
import json

key_file = r"C:\Users\ohson\Desktop\practice\clsude_test\App_1\App_2\action_item_bot\fir-test-87458-firebase-adminsdk-fbsvc-e96539fc91.json"

# Firebase初期化
if not firebase_admin._apps:
    cred = credentials.Certificate(f"{key_file}")  # 既存のファイルを使用
    firebase_admin.initialize_app(cred)

def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'test.html') 
    # return HttpResponse("Hello World")

@csrf_exempt
def protected(request):
    if request.method != 'GET':
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return JsonResponse({"error": "No token provided"}, status=401)
    
    try:
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return JsonResponse({"error": "Invalid Authorization header"}, status=401)
        token = parts[1]
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        email = decoded_token.get('email', '')
        
        # ユーザー情報を取得または作成
        user, created = User.objects.get_or_create(
            firebase_uid=uid,
            defaults={'name': email.split('@')[0], 'email': email}
        )
        
        return JsonResponse({
            "message": "ログイン成功", 
            "uid": uid,
            "user_id": user.id,
            "name": user.name
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=401)

def action_items(request):
    """Action Item一覧取得"""
    items = ActionItem.objects.select_related('assigned_to').all()
    data = []
    for item in items:
        data.append({
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'assigned_to': item.assigned_to.name,
            'due_date': item.due_date.strftime('%Y-%m-%d'),
            'completed': item.completed
        })
    return JsonResponse({'items': data})