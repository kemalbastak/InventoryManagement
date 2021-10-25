from .models import Order, Product, User
def quantity_renderer(request):

    return {
       'order_quantity': Order.objects.all().count(),
       'product_quantity': Product.objects.all().count(),
       'worker_quantity': User.objects.all().count(),
    }