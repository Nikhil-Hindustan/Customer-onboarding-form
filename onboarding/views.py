from django.shortcuts import render, redirect
from .forms import CustomerModelForm, CustomerDocumentForm
from .models import CustomerModel


def home(request):
    context = {}
    return render(request, "onboarding/home.html", context)


def create_customer(request):
    if request.method == 'POST':
        customer_form = CustomerModelForm(request.POST)
        document_form = CustomerDocumentForm(request.POST, request.FILES)
        if customer_form.is_valid() and document_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.created_by = request.user
            customer.save()

            document = document_form.save(commit=False)
            document.customer = customer
            document.save()

            return redirect('list_customer')
    else:
        customer_form = CustomerModelForm()
        document_form = CustomerDocumentForm()

    return render(request, 'onboarding/create_customer.html', {'customer_form': customer_form, 'document_form': document_form})


def list_customer(request):
    # Fetch and display list of customers
    customers = CustomerModel.objects.all()
    return render(request, 'onboarding/list_customer.html', {'customers': customers})
