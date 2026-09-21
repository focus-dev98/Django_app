from django.http import HttpResponse
from .models import Product


def product_list(request):
	products = Product.objects.all()
	
	html = "<h1>Products</h1>"

	for product in products:
		html += f"<p>{product.name} - ${product.price}</p>"
		
	return HttpResponse(html)
