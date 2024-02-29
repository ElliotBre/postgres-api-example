from app.viewsets import appViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('appRouter', appViewset)
