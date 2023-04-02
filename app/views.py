from django.shortcuts import render
from django.http import JsonResponse
from .models import Upload
from django.http import HttpResponseRedirect
from .forms import ImageUploadForm

# Create your views here.

def show_image(request):
    image = Upload.objects.first()
    data = image.get_image_data()
    context={
        'data': data ,
        'image':image,

    }
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = Upload(image=form.cleaned_data['image'])
            upload.save()
            image_data = upload.get_image_data()
            return JsonResponse(image_data, charset='utf-8')
    else:
        form = ImageUploadForm()
    
    return render(request, 'index.html', context)
