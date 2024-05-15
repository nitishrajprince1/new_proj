from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import User
import json
from datetime import datetime, timedelta


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        user = User.objects.create(username=username, email=email)
        user.save()

        return JsonResponse({'message': 'User created successfully'}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'PUT' or request.method == 'PATCH':
        data = json.loads(request.body)
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'time_remaining' in data:
            user.time_remaining = data['time_remaining']
        user.save()
        return JsonResponse({'message': 'User updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return JsonResponse({'message': 'User deleted successfully'}, status=200)


def forced_logout_status(request, user_id):
    try:
        user = User.objects.filter(id=user_id).first()
    except Exception as e:
        response_data = {
            'error': 'unable to connect to database'
            }
        return JsonResponse(response_data, status=500)
    try:
        if not user:
            response_data = {
                'Error': 'User Not found'
                }
            return JsonResponse(response_data, status=404)
        current_time = datetime.now()
        time_difference = current_time - user.last_time_remaining_update.replace(tzinfo=None)

        if time_difference > timedelta(minutes=5):
            user_status = 'inactive'
        else:
            user_status = 'active'

        response_data = {
            'time_remaining': user.time_remaining,
            # 'last_time_remaining_update': user.last_time_remaining_update,
            'user_status': user_status
        }
        return JsonResponse(response_data)
    except Exception as e:
        response_data = {
            'messeges': f'{e}'
        }
        return JsonResponse(response_data)
