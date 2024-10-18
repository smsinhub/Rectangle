from django.shortcuts import render
from .models import Rectangle

def view(request):
    try:
        rectangle = Rectangle.objects.get(id=1) 
        length = rectangle.length
        width = rectangle.width
    except Rectangle.DoesNotExist:
        length = 86
        width = 54

    area = length * width
    perimeter = 2 * (length + width)

    context = {
        'length': length,
        'width': width,
        'area': area,
        'perimeter': perimeter
    }
    
    return render(request, 'rectangle.html', context)
