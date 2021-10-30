from rest_framework import routers

from orders.views import OrderView

router = routers.SimpleRouter()
router.register('orders', OrderView)

urlpatterns = [

]
urlpatterns += router.urls
