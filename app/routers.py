from app.viewsets import app
from rest_framework import routers

router = routers.DefaultRouter()
router.register('app', app)
