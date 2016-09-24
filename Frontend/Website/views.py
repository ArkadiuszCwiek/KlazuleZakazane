from django.http import HttpResponse
from django.template import loader
from .helper import handle_uploaded_text_file, handle_uploaded_pdf_file


def index(request):
    if request.method == 'POST':
        return handlePost(request)
    else:
        template = loader.get_template('Website/index.html')
        return HttpResponse(template.render({'text': ''}, request))

def handlePost(request):
    template = loader.get_template('Website/index.html')
    if request.FILES == {}:
        agreementContent = request.POST.get('pastedAgreement')
    else:
        f = request.FILES['fileToUpload']
        if f.name[-3:] == "pdf":
            agreementContent = handle_uploaded_pdf_file(f)
        else:
            agreementContent = handle_uploaded_text_file(f)
    return HttpResponse(template.render({'agreementContent': agreementContent}, request))