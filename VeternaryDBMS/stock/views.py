from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import DateForm,SelectPrintOutForm,SelectKebeleForm
# import models
from drug_in_out.models import DrugIn,DrugOut
from vaccine_in_out.models import VaccineIn,VaccineOut
from equipment_in_out.models import ClinicalEquipmentIn,ClinicalEquipmentOut
from receipt_in_out.models import ReceiptIn,ReceiptOut
# utils
from utils.printout import printout,receipt_printout
# Create your views here.

class StockPrintOutView(LoginRequiredMixin,View):
    login_url = "/"
    templateUrl = "stock/printouts.html"

    def get(self,request):
        date_form = DateForm()
        select_printout_form = SelectPrintOutForm()
        select_kebele_form = SelectKebeleForm()
        context = {
            'date_form':date_form,
            'select_prinout_form':select_printout_form,
            'select_kebele_form':select_kebele_form
        }

        return render(request,self.templateUrl,context = context)

    def post(self,request):
        date_form = DateForm(request.POST)
        select_printout_form = SelectPrintOutForm(request.POST)
        select_kebele_form = SelectKebeleForm(request.POST)

        # get values from post request
        selected_date = date_form['date'].value()
        selected_type = select_printout_form['choice_field'].value()
        selected_kebele = select_kebele_form['kebele'].value()

        if selected_type == "drug_in":
            print("Drug in")
            in_drugs = DrugIn.objects.filter(date=selected_date)
            if len(in_drugs) > 0:
                in_drugs_list = []
                for obj in in_drugs:
                    params = {
                        'invoice_type':'DRUG IN',
                        'item':obj.drug.drug_type,
                        'receiver':obj.receiver.username,
                        'destination':'--------',
                        'quantity':str(obj.quantity),
                        'unit_price':obj.unit_price.__str__(),
                        'total':obj.total.__str__(),
                        'batch_number':obj.batch_number,
                        'date':obj.date,
                        'expiration_data':obj.expiration_data,
                        }
                    in_drugs_list.append(params)
                return printout(request,in_drugs_list)

        elif selected_type == "drug_out":
            out_drugs = DrugOut.objects.filter(date=selected_date,kebele=selected_kebele)
            if len(out_drugs) > 0:
                out_drugs_list = []
                for obj in out_drugs:
                    params = {
                        'invoice_type':'DRUG OUT',
                        'item':obj.drug.drug_type,
                        'kebele':obj.kebele.name,
                        'receiver':obj.received_by,
                        'destination':obj.destination,
                        'quantity':str(obj.quantity),
                        'unit_price':obj.drug.stock_price.__str__(),
                        'total':obj.total.__str__(),
                        'batch_number':obj.batch_number,
                        'date':obj.date,
                        'expiration_data':'--------',
                        'invoice-number':obj.batch_number+"-"+str(obj.id)
                        }
                    out_drugs_list.append(params)
                return printout(request,out_drugs_list)

        elif selected_type == "vaccine_in":
            in_vaccines = VaccineIn.objects.filter(date=selected_date)
            if len(in_vaccines) > 0:
                in_vaccines_list = []
                for obj in in_vaccines:
                    params = {
                        'invoice_type':'VACCINE IN',
                        'item':obj.vaccine.vaccine_type,
                        'receiver':obj.receiver.username,
                        'destination':'--------',
                        'quantity':str(obj.quantity),
                        'unit_price':obj.unit_price.__str__(),
                        'total':obj.total.__str__(),
                        'batch_number':obj.batch_number,
                        'date':obj.date,
                        'expiration_data':obj.expiration_data,
                        }
                    in_vaccines_list.append(params)
                return printout(request,in_vaccines_list)
        elif selected_type == "vaccine_out":
            out_vaccines = VaccineOut.objects.filter(date=selected_date,kebele=selected_kebele)
            if len(out_vaccines) > 0:
                out_vaccines_list = []
                for obj in out_vaccines:
                    params = {
                        'invoice_type':'VACCINE OUT',
                        'item':obj.vaccine.vaccine_type,
                        'kebele':obj.kebele.name,
                        'receiver':obj.received_by,
                        'destination':obj.destination,
                        'quantity':str(obj.quantity),
                        'unit_price':obj.vaccine.stock_price.__str__(),
                        'total':obj.total.__str__(),
                        'batch_number':obj.batch_number,
                        'date':obj.date,
                        'expiration_data':'--------',
                        }
                    out_vaccines_list.append(params)
                return printout(request,out_vaccines_list)
        elif selected_type == "equipment_in":
            in_equipments = ClinicalEquipmentIn.objects.filter(date_received=selected_date)
            if len(in_equipments) > 0:
                in_equipments_list = []
                for obj in in_equipments:
                    params = {
                        'invoice_type':'EQUIPMENT IN',
                        'item':obj.equipment.name,
                        'receiver':obj.receiver.username,
                        'destination':'--------',
                        'quantity':str(obj.quantity),
                        'unit_price':'-',
                        'total':'0',
                        'batch_number':obj.batch_number,
                        'date':obj.date_received,
                        'expiration_data':'--------',
                        }
                    in_equipments_list.append(params)
                return printout(request,in_equipments_list)
        elif selected_type == "equipment_out":
            out_equipments = ClinicalEquipmentOut.objects.filter(date=selected_date,kebele=selected_kebele)
            if len(out_equipments) > 0:
                out_equipments_list = []
                for obj in out_equipments:
                    params = {
                        'invoice_type':'EQUIPMENT OUT',
                        'item':obj.equipment.name,
                        'kebele':obj.kebele.name,
                        'receiver':obj.received_by,
                        'destination':obj.destination,
                        'quantity':str(obj.quantity),
                        'unit_price':'-',
                        'total':'0',
                        'batch_number':obj.batch_number,
                        'date':obj.date,
                        'expiration_data':'--------',
                        'invoice-number':obj.batch_number+"-"+str(obj.id)
                        }
                    out_equipments_list.append(params)
            return printout(request,out_equipments_list)
        elif selected_type == "receipt_in":
            in_receipts = ReceiptIn.objects.filter(date=selected_date,kebele=selected_kebele)
            if len(in_receipts) > 0:
                in_receipts_list = []
                for obj in in_receipts:
                    params = {
                    'invoice_type':'RECEIPT IN',
                    'item':obj.receipt_type.receipt_type,
                    'deliverer_receiver':obj.deliverer_name,
                    'quantity':str(obj.quantity),
                    'kebele':obj.kebele.name,
                    'unit':obj.unit,
                    'date':obj.date,
                    'serial_init':obj.serial_num_init,
                    'serial_last':obj.serial_num_last,
                    }
                    in_receipts_list.append(params)
                return receipt_printout(request,in_receipts_list)
        else:
            out_receipts = ReceiptOut.objects.filter(date=selected_date,kebele=selected_kebele)
            if len(out_receipts) > 0:
                out_receipts_list = []
                for obj in out_receipts:
                    params = {
                        'invoice_type':'RECEIPT OUT',
                        'item':obj.receipt_type.receipt_type,
                        'deliverer_receiver':obj.receiver_name,
                        'quantity':str(obj.quantity),
                        'kebele':obj.kebele.name,
                        'unit':obj.unit,
                        'date':obj.date,
                        'serial_init':obj.serial_num_init,
                        'serial_last':obj.serial_num_last,
                        }
                    out_receipts_list.append(params)
                return receipt_printout(request,out_receipts_list)
        context = {
            'date_form':date_form,
            'select_prinout_form':select_printout_form,
            'select_kebele_form':select_kebele_form
        }
        return render(request,self.templateUrl,context = context)
