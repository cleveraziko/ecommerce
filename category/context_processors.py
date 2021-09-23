from .models import Category


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

# def links(request):
#     link = Category.objects.all()
#     return dict(link=link)