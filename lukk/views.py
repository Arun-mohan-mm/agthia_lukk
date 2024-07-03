from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
from django.contrib.auth.models import User, auth
import csv
import io
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        civil_id = request.POST.get('civil_id')
        phone = request.POST.get('phone')
        receipt_number = request.POST.get('receipt_number')
        voucher_number = request.POST.get('voucher_number')
        bnb = Customer_details()
        bnb.name = name
        bnb.civil_id = civil_id
        bnb.phone = phone
        bnb.receipt_number = receipt_number
        bnb.voucher_number = voucher_number
        bnb.save()
        messages.success(request,'Details uploaded successfully')
        return redirect('home')
    return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username = username, password = password)
        if user is None:
            messages.success(request, 'Invalid credentials')
            return render(request, 'login.html')
        auth.login(request, user)
        return redirect('admin_home')
    else:
        return render(request, 'login.html')

@login_required
def admin_home(request):
    return render(request,'admin_home.html')

@login_required
def download_csv(request):
    # Create an in-memory CSV file
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)

    # Write BOM for UTF-8 encoding to support Excel
    csv_buffer.write(u'\ufeff'.encode('utf-8').decode())

    # Write headers
    writer.writerow([
        smart_str('Name'),
        smart_str('Civil ID'),
        smart_str('Phone'),
        smart_str('Receipt Number'),
        smart_str('Voucher Number'),
    ])

    # Fetch data from the database
    customers = Customer_details.objects.all()

    for customer in customers:
        # Encode each field to UTF-8 explicitly
        writer.writerow([
            smart_str(customer.name),
            smart_str(customer.civil_id),
            smart_str(customer.phone),
            smart_str(customer.receipt_number),
            smart_str(customer.voucher_number),
        ])

    # Create the HttpResponse object with the appropriate CSV header
    response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customer_details.csv"'

    return response


def logout(request):
    auth.logout(request)
    return redirect('home')