from rest_framework.routers import SimpleRouter
from products.views import ProductModelViewSet


router = SimpleRouter()

router.register('products', ProductModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls
