import qrcode

from django.http import HttpResponse

from django.shortcuts import render
from django.urls import reverse
from .forms import UploadForm
from .models import Verification

# Create your views here.
def verification(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'verificationform.html', {'form': form, 'message': 'Form successfully submitted.'})
        else:
            return render(request, 'verificationform.html', {'form': form, 'message': 'Form is invalid.'})
    else:
        form = UploadForm()
        return render(request, 'verificationform.html', {'form': form})

def displayVerForms(request):
    all_verforms = Verification.objects.filter(isChecked=False)
    return render(request, 'displayverforms.html', {'all_verforms': all_verforms})

def generate_qr(request, data):
    # Generate QR code image
    img = qrcode.make(data)

    # Return image as HTTP response
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response

# def generate_qr(request):
#     if request.method == 'POST':
#         id_num = request.POST['id_num']
#         qr_url = f"../../verification/generate-qr/{id_num}"
#         return render(request, 'qrCodeGenerator.html', {'qr_url': qr_url})

#     return render(request, 'qrCodeGenerator.html')