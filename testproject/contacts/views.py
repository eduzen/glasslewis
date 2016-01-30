from django.shortcuts import render
from .models import Company, Contact


def company_list(request):
    companies = Company.objects.all()
    results = []
    for c in companies:
        company = {}
        company['name'] = c.name
        company['address_line1'] = c.address_line1
        company['address_line2'] = c.address_line2
        company['phone_number'] = c.phone_number
        company['homepage'] = c.homepage
        company['contacts'] = Contact.objects.filter(company=c)
        results.append(company)

    return render(
        request,
        'contacts/company_list.html',
        {'results': results}
    )


def contacts(request):
    contacts = Contact.objects.all().order_by('last_name')

    return render(
        request,
        'contacts/contact_list.html',
        {'contacts': contacts}
    )


def contact_detail(request, pk=None):
    contact = Contact.objects.filter(id=pk)
    if contact.exists():
        contact = contact[0]

    return render(
        request,
        'contacts/contact_detail.html',
        {'contact': contact}
    )
