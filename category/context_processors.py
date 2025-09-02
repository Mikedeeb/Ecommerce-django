from category.models import Category

def menu_links(request):
    """
    Context processor to add menu links to the context.
    """
    links = Category.objects.all()
    
    return dict(links=links)