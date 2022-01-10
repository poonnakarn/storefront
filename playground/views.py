from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem



def say_hello(request):
    collection = Collection(pk=12)
    collection.delete()

    return render(request, 'hello.html', {'name': 'Poon'})
