from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TelegramUser
from datetime import datetime

@api_view(['POST'])
def sync_user(request):
    data = request.data
    telegram_id = data.get("id")
    if not telegram_id:
        return Response({"error": "no id"}, status=400)

    TelegramUser.objects.update_or_create(
        telegram_id=telegram_id,
        defaults={
            "username": data.get("username"),
            "is_bot": data.get("is_bot", False),
            "last_active": datetime.now(),
        },
    )
    return Response({"status": "ok"})
