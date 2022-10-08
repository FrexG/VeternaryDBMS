import io
from datetime import datetime
from mmap import PAGESIZE
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas

def printout(request,params):

    print(params)
    # Create the HttpResponse object 
    response = HttpResponse(content_type='application/pdf') 

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"' 

    # Creating Canvas
    c = canvas.Canvas(response,pagesize=(200,250),bottomup=0)

    # Logo Section
    # Setting th origin to (10,40)
    c.translate(10,40)
    # Inverting the scale for getting mirror Image of logo
    c.scale(1,-1)
    # Inserting Logo into the Canvas at required position
    #c.drawImage("logo.jpg",0,0,width=50,height=30)

    # Title Section
    # Again Inverting Scale For strings insertion
    c.scale(1,-1)
    # Again Setting the origin back to (0,0) of top-left
    c.translate(-10,-40)
    # Setting the font for Name title of company
    c.setFont("Helvetica-Bold",6)
    # Inserting the name of the company
    c.drawCentredString(100,20,"Damboya Woreda Animal Health and Quarentine Center")
    # For under lining the title
    c.line(5,45,195,45)

    # Changing the font size for Specifying Address
    c.setFont("Helvetica-Bold",5)
    c.drawCentredString(125,30,"Damboya, Kembata Tembaro Zone")
    c.drawCentredString(125,35,"SNNPR,Ethiopia")
    # Changing the font size for Specifying GST Number of firm
    c.setFont("Helvetica-Bold",6)
    c.drawCentredString(125,42,"+251-46-245-0298")

    # Line Seprating the page header from the body
    c.line(5,45,195,45)

    # Document Information
    # Changing the font for Document title
    c.setFont("Courier-Bold",8)
    c.drawCentredString(100,55,f"{params['invoice_type']}")

    # This Block Consist of Costumer Details
    c.roundRect(15,63,170,40,10,stroke=1,fill=0)
    c.setFont("Times-Bold",5)
    c.drawString(70,70,f"DESTINATION:{params['destination']}")
    c.drawString(70,80,f"DATE :{params['date']}")
    c.drawString(70,90,f"RECEIVER :{params['receiver']}")
    c.drawString(70,100,f"BATCH No. :{params['batch_number']}")
    #c.drawRightString(70,100,"PHONE No. :")

    # This Block Consist of Item Description
    c.roundRect(15,108,170,130,10,stroke=1,fill=0)
    c.line(15,120,185,120)
    c.drawCentredString(25,118,"SR No.")
    c.drawCentredString(75,118,"ITEM")
    c.drawCentredString(125,118,"UNIT $")
    c.drawCentredString(148,118,"QTY")
    c.drawCentredString(173,118,"TOTAL")
    # Item values
    c.setFont("Times-Bold",4)
    c.drawCentredString(25,125,"1")
    c.drawCentredString(75,125,params['item'])
    c.drawCentredString(125,125,params['unit_price'])
    c.drawCentredString(148,125,params['quantity'])
    c.drawCentredString(173,125,params['total'])
 
    # Drawing table for Item Description
    c.line(15,210,185,210)
    c.line(35,108,35,220)
    c.line(115,108,115,220)
    c.line(135,108,135,220)
    c.line(160,108,160,220)

    # Declaration and Signature
    c.line(15,220,185,220)
    c.line(100,220,100,238)
    c.drawString(20,225,"We declare that above mentioned")
    c.drawString(20,230,"information is true.")
    c.drawString(20,235,"(This is system generated invoive)")
    c.drawRightString(180,235,"Authorised Signatory")

    # End the Page and Start with new
    c.showPage()
    # Saving the PDF
    c.save()

    # Show the result to the user    
    return response

def abattoir_printout(request,params):
    response = HttpResponse(content_type='application/pdf') 

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"' 

    # Creating Canvas
    c = canvas.Canvas(response,pagesize=(200,250),bottomup=0)

    c.setFont("Helvetica-Bold",6)
    # Inserting the name of the company
    c.drawCentredString(100,20,"Abattori Exam Result")
    # For under lining the title
    c.line(5,25,195,25) 

    c.setFont("Helvetica",5)
    c.drawString(5,40,f"Hotel Name: {params['hotel']}")
    c.drawString(80,40,f"Hotel Code: {params['hotel_code']}")
    c.drawString(150,40,f"Date: {params['date']}")

    c.setFont("Helvetica-Bold",6)
    # Inserting the name of the company
    c.drawCentredString(100,50,"General Physical Examination")
    c.line(5,55,195,55)

    c.setFont("Helvetica",5)
    c.drawString(5,60,f"Species: {params['species']}")
    c.drawString(5,70,f"Sex: {params['sex']}")
    c.drawString(5,80,f"Origin: {params['origin']}")
    c.drawString(5,90,f"Color: {params['color']}")
    c.drawString(5,100,f"Weight: {params['weight']}")
    c.drawString(5,110,f"T0: {params['t0']}")
    c.drawString(5,120,f"PR: {params['pr']}")
    c.drawString(5,130,f"RR: {params['rr']}")
    c.drawString(5,140,f"Result: {params['result']}")
    c.drawString(5,160,f"Name and Signature: ____________________")
    c.save()
    return response

def receipt_printout(request,params):

    print(params)
    # Create the HttpResponse object 
    response = HttpResponse(content_type='application/pdf') 

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"' 

    # Creating Canvas
    c = canvas.Canvas(response,pagesize=(200,250),bottomup=0)

    # Logo Section
    # Setting th origin to (10,40)
    c.translate(10,40)
    # Inverting the scale for getting mirror Image of logo
    c.scale(1,-1)
    # Inserting Logo into the Canvas at required position
    #c.drawImage("logo.jpg",0,0,width=50,height=30)

    # Title Section
    # Again Inverting Scale For strings insertion
    c.scale(1,-1)
    # Again Setting the origin back to (0,0) of top-left
    c.translate(-10,-40)
    # Setting the font for Name title of company
    c.setFont("Helvetica-Bold",6)
    # Inserting the name of the company
    c.drawCentredString(100,20,"Damboya Woreda Animal Health and Quarentine Center")
    # For under lining the title
    c.line(5,45,195,45)

    # Changing the font size for Specifying Address
    c.setFont("Helvetica-Bold",5)
    c.drawCentredString(125,30,"Damboya, Kembata Tembaro Zone")
    c.drawCentredString(125,35,"SNNPR,Ethiopia")
    # Changing the font size for Specifying GST Number of firm
    c.setFont("Helvetica-Bold",6)
    c.drawCentredString(125,42,"+251-46-245-0298")

    # Line Seprating the page header from the body
    c.line(5,45,195,45)

    # Document Information
    # Changing the font for Document title
    c.setFont("Courier-Bold",8)
    c.drawCentredString(100,55,f"{params['invoice_type']}")

    # This Block Consist of Costumer Details
    c.roundRect(15,63,170,40,10,stroke=1,fill=0)
    c.setFont("Times-Bold",5)
    c.drawString(20,70,f"DELIVERER/RECEIVER: {params['deliverer_receiver']}    SIGN: _________")
    c.drawString(20,80,"APPROVED BY :_________________________ SIGN:________")
    c.drawString(20,90,f"KEBELE:{params['kebele']}")
    c.drawString(20,100,f"DATE:{params['date']}")
    #c.drawRightString(70,100,"PHONE No. :")

    # This Block Consist of Item Description
    c.roundRect(15,108,170,130,10,stroke=1,fill=0)
    c.line(15,120,185,120)
    c.drawCentredString(25,118,"SR No.")
    c.drawCentredString(55,118,"TYPE")
    c.drawCentredString(80,118,"UNIT")
    c.drawCentredString(100,118,"QTY")
    c.drawCentredString(150,118,"SERIES")
    # Item values
    c.setFont("Times-Bold",4)
    c.drawCentredString(25,125,"1")
    c.drawCentredString(55,125,params['item'])
    c.drawCentredString(80,125,params['unit'])
    c.drawCentredString(100,125,params['quantity'])
    c.drawCentredString(120,125,params['serial_init'])
    c.drawCentredString(160,125,params['serial_last'])
 
    # Drawing table for Item Description
    c.line(15,210,185,210)
    c.line(35,108,35,220)
    c.line(70,108,70,220)
    c.line(90,108,90,220)
    c.line(110,108,110,220)
    c.line(150,120,150,220)

    # Declaration and Signature
    c.line(15,220,185,220)
    c.line(100,220,100,238)
    c.drawString(20,225,"We declare that above mentioned")
    c.drawString(20,230,"information is true.")
    c.drawString(20,235,"(This is system generated invoive)")
    c.drawRightString(180,235,"Authorised Signatory")

    # End the Page and Start with new
    c.showPage()
    # Saving the PDF
    c.save()

    # Show the result to the user    
    return response