import io
from datetime import datetime
from mmap import PAGESIZE
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas

def printout(request):
    print('printout')
    # Create the HttpResponse object 
    response = HttpResponse(content_type='application/pdf') 

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"' 

    # READ Optional GET param
    get_param = request.GET.get('name', 'World')

    # Generate unique timestamp
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    p = canvas.Canvas(response, pagesize=(500, 500))

    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)
    # company name
    p.drawString(20,480, 'Damboya Woreda Animal Health and Quarentine Department')
    p.line(20,475,450,475)
    p.drawString(20,460,'Out drug form')
    """ p.drawString(30,735,'OF ACME INDUSTRIES')
    p.drawString(500,750,"12/12/2010")
    p.line(480,747,580,747)
    p.drawString(275,725,'AMOUNT OWED:')
    p.drawString(500,725,"$1,000.00")
    p.line(378,723,580,723)
    p.drawString(30,703,'RECEIVED BY:')
    p.line(120,700,580,700)
    p.drawString(120,703,"JOHN DOE") """

    p.save()

    # Show the result to the user    
    return response
