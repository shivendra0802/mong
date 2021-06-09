from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from mongoapp.models import  Tag
from .models import Customer
import uuid
# Create your views here.

def id_uuids():
    uid = uuid.uuid4()
    id_uid = str(uid)
    return id_uid


def cutomer(request):
    if request.method == 'POST':
        id = id_uuids()
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        tag_cus = request.POST.get('tag_cus')
        d = tag_cus.split(',')
        customer = Customer(id=id, name=name, age=age, address = address)
        tag_ = Tag(customer_id=id, tag_cus=d)
        customer.save()
        tag_.save()
        return render(request, 'sqliteapp/index.html')
    else:
        return render(request, 'sqliteapp/index.html')


def show_customer(request):
    customer = Customer.objects.values('id', 'name', 'age', 'address')
    tag = Tag.objects.values_list('customer_id', 'tag_cus')
    print(customer)
    print(tag)
    # id = Customer.objects.values('id', 'name', 'age', 'address')
    # u_id = Customer.objects.values('id')
    # # print(u_id)
    # cu_uid = print(str(u_id))
    # t_id = Tag.objects.values_list('customer_id', 'tag_cus')
    # # print(id)
    # # print(u_id)
    # print(t_id)
    # cus = {'id', id}
    # ta_cus = {'t_id', t_id}
    return render(request, 'sqliteapp/action.html', {'customer': customer, 'tag': tag})