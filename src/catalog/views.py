from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_list(request):
    products = Product.objects.filter(is_active=True).select_related("category")
    categories = Category.objects.all()
    return render(
        request,
        "catalog/product_list.html",
        {"products": products, "categories": categories},
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("category"),
        slug=slug,
        is_active=True,
    )
    return render(request, "catalog/product_detail.html", {"product": product})
