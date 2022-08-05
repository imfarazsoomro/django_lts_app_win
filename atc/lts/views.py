from django.shortcuts import render, redirect

from .constants import ServiceRequestStatus
from .models import ServiceRequest


def index(request):
    return render(request, 'index.html')


def service_requests(request):
    all_requests = ServiceRequest.objects.count()
    open_requests = ServiceRequest.objects.filter(status=ServiceRequestStatus.request.name).order_by('id')
    offers = ServiceRequest.objects.filter(status=ServiceRequestStatus.offer.name).order_by('id')
    agreements = ServiceRequest.objects.filter(status=ServiceRequestStatus.agreement.name).order_by('id')
    # for agreement in agreements:
    #     due_date = agreement.due_date
    #     due_date_new = due_date.strftime("%m/%d/%Y")
        # print(due_date, due_date_new)
        # agreement.due_date = due_date_new
        # agreement.save()
    vals = {
        'all_req_count': all_requests,
        'requests': open_requests,
        'request_count': open_requests.count(),
        'offers': offers,
        'offer_count': offers.count(),
        'agreements': agreements,
        'agreement_count': agreements.count(),
        'user': request.user,
    }
    return render(request, 'request/service_request_page.html', vals)


def request_form(request):
    return render(request, 'request/request_form.html')


def add_new_request(request):
    if request.method == 'POST':
        ref = request.POST.get('ref')
        title = request.POST.get('title')
        price = request.POST.get('price')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        data = ServiceRequest(
            ref=ref,
            title=title,
            price=price,
            due_date=due_date,
            status=status
        )
        data.save()
    return redirect("/requests/")


def update_request(request, request_id):
    req_id = ServiceRequest.objects.get(id=request_id)
    vals = {
        "req_id": req_id,
        "due_date": str(req_id.due_date.strftime("%Y-%m-%d"))
    }
    if request.method == 'POST':
        obj = request.POST
        req_id.title = obj.get('title')
        req_id.price = obj.get('price')
        req_id.due_date = obj.get('due_date')
        req_id.status = obj.get('status')
        req_id.save()
        return redirect('/requests/')

    return render(request, 'request/request_form.html', vals)


def delete_request(request, request_id):
    req_id = ServiceRequest.objects.get(id=request_id)
    req_id.delete()
    return redirect('/requests/')