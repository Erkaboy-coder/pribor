from datetime import datetime

from django import template
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as auth_logout
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

register = template.Library()

from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.
from index.models import Category, Appliance, Certificate, Profile, Subcategory, ResponsiblePerson, History, Departments
from django.db.models import Q


def index(request):
    categories = Category.objects.all()
    items = Appliance.objects.filter(category_id__in=categories).filter(is_delete=0)
    certificates =Certificate.objects.all()
    # paginator = Paginator(categories, 6)

    context = {'categories': categories,'items':items,'certificates':certificates}
    return render(request, 'index.html', context)

def profile(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    items = Appliance.objects.filter(category_id__in=categories).filter(is_delete=0)
    certificates =Certificate.objects.all()
    # paginator = Paginator(categories, 6)

    context = {'categories': categories,'items':items,'certificates':certificates,'subcategories':subcategories}
    return render(request, 'profile.html', context)

def edit_category(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('category_id')
        category = Category.objects.filter(pk=id).values()
        print(category)
        return JsonResponse({'category': list(category)},safe=False)

    else:
        return HttpResponse(0)

def edit_sub_category(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('sub_category_id')
        category = Subcategory.objects.filter(pk=id).values()
        print(category)
        return JsonResponse({'category': list(category)},safe=False)

    else:
        return HttpResponse(0)

def change_category(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        name = data.get('category_name')
        category = Category.objects.get(pk=id)
        print(category)
        category.name = name
        category.save()
        messages.success(request, "Toifa nomi o'zgartirildi !")

        return HttpResponse(1)

    else:
        return HttpResponse(0)

def change_sub_category(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        name = data.get('sub_category_name')
        category = Subcategory.objects.get(pk=id)
        print(category)
        category.name = name
        category.save()
        messages.success(request, "Quyi toifa nomi o'zgartirildi !")

        return HttpResponse(1)

    else:
        return HttpResponse(0)

def new_category(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('new_category_name')
        category = Category(name=name)
        category.save()
        messages.success(request, "Yangi toifa qo'shildi !")
        return HttpResponse(1)

    else:
        return HttpResponse(0)

def new_sub_category(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('new_sub_category_name')
        subcategory = Subcategory(name=name)
        subcategory.save()
        messages.success(request, "Yangi quyi toifa qo'shildi !")
        return HttpResponse(1)

    else:
        return HttpResponse(0)

def delete_category(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('category_id')
        category = Category.objects.filter(pk=id).values()
        print(category)
        return JsonResponse({'category': list(category)}, safe=False)

    else:
        return HttpResponse(0)

def delete_sub_category(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('sub_category_id')
        category = Subcategory.objects.filter(pk=id).values()
        print(category)
        return JsonResponse({'category': list(category)}, safe=False)

    else:
        return HttpResponse(0)

def delete_category_1(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        category = Category.objects.get(pk=id)
        print(category)
        category.delete()
        messages.error(request, "Toifa o'chirildi !")

        return HttpResponse(1)

    else:
        return HttpResponse(0)

def delete_sub_category_1(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        category = Subcategory.objects.get(pk=id)
        print(category)
        category.delete()
        messages.error(request, "Quyi toifa o'chirildi !")

        return HttpResponse(1)

    else:
        return HttpResponse(0)

def history(request):
    histories = History.objects.all().order_by('-id')
    context = {'histories': histories}
    return render(request, 'histories.html', context)

def items_with_category(request, id):
    items = Appliance.objects.filter(category_id=id).filter(is_delete=0)
    items_all = Appliance.objects.filter(category_id=id).filter(is_delete=0)
    category = Category.objects.filter(id=id).first()
    subcategories = Subcategory.objects.all()
    persons = ResponsiblePerson.objects.all()
    context = {'items':items, 'category':category,'items_all':items_all,'subcategories':subcategories,'persons': persons}
    return render(request, 'items_with_category.html', context)

def items(request):
    items_all = Appliance.objects.all().filter(is_delete=0)
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    persons = ResponsiblePerson.objects.all()

    # certificates = Certificate.objects.filter(item_id__in=items_all)
    # print(certificates)

    context = {'items_all':items_all, 'categories':categories, 'subcategories':subcategories, 'persons':persons}
    return render(request, 'items.html', context)


def add_pribor_page(request,id):
    category = Category.objects.filter(id=id).first()
    subcategories = Subcategory.objects.all()
    departments = Departments.objects.all()
    responsible_persons=ResponsiblePerson.objects.all()
    context = {'category': category,'departments':departments, 'subcategories': subcategories,'persons':responsible_persons}
    return render(request, 'add_pribor.html', context)

def add_pribor(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        name1 = request.POST.get('name1')
        inv_number = request.POST.get('inv_number')
        origin_country = request.POST.get('origin_country')
        origin_factory = request.POST.get('origin_factory')
        origin_year = request.POST.get('origin_year')
        used_year = request.POST.get('used_year')
        factory_number = request.POST.get('factory_number')
        exploit_department = request.POST.get('exploit_department')
        checked_organization = request.POST.get('checked_organization')
        responsible_user = request.POST.get('responsible_user')

        if responsible_user:
            if not ResponsiblePerson.objects.filter(name=responsible_user).first():
                person=ResponsiblePerson(name=responsible_user)
                person.save()

        status_passport_value = request.POST.get('status_passport_value')
        passport = request.FILES.get('passport',False)

        status_battery_value = request.POST.get('status_battery_value')
        status_battery = request.POST.get('status_battery')

        certificate_number = request.POST.get('certificate_number')
        user_id = request.POST.get('user_id')

        status_compatibility_file_value = request.POST.get('status_compatibility_file_value')
        compatibility_file = request.FILES.get('compatibility_file',False)

        issue_date = request.POST.get('issue_date')
        year = request.POST.get('year')
        expiry_date = request.POST.get('expiry_date')
        info = request.POST.get('info')

        certificate = request.FILES.get('certificate', False)

        href = request.POST.get('href')

        # import datetime
        from datetime import timedelta
        # current_year = datetime.datetime.now().year
        begindate = datetime.strptime(origin_year, "%Y-%m-%d")
        enddate = begindate + timedelta(weeks = 52)

        if status_passport_value == '1' and status_compatibility_file_value == '1':
            appliance = Appliance(category_id=category, subcategory_id=subcategory,
                                    name=name1, inv_number=inv_number,
                                    factory_number=factory_number, origin_country=origin_country,
                                    origin_factory=origin_factory, origin_year=origin_year,
                                    used_year=used_year, status_battery=status_battery,
                                    battery=status_battery_value, status_passport=status_passport_value,
                                    passport=passport, department_id=exploit_department,
                                    responsible_user=responsible_user,status=0, info=info,compatibility_file=compatibility_file,status_compatibility_file_value=status_compatibility_file_value)
            appliance.save()

            certificate = Certificate(issue_date=origin_year, expiry_date=enddate, status=1, appliance_id=appliance.id,last=1)
            certificate.save()

            history = History(date=datetime.now(), status=6, user_id=user_id, appliance_id=appliance.id)
            # status = 6 bolsa yangi pribor qoshgan
            history.save()

        else:
            appliance = Appliance(category_id=category, subcategory_id=subcategory,
                                  name=name1, inv_number=inv_number,
                                  factory_number=factory_number, origin_country=origin_country,
                                  origin_factory=origin_factory, origin_year=origin_year,
                                  used_year=used_year, status_battery=status_battery,
                                  battery=status_battery_value, status_passport=status_passport_value,
                                  passport=passport, department_id=exploit_department,
                                  responsible_user=responsible_user,status=0, info=info, compatibility_file=compatibility_file,
                                  status_compatibility_file_value=status_compatibility_file_value)
            appliance.save()
            certificate = Certificate(issue_date=issue_date, expiry_date=expiry_date, file=certificate, certificate_number=certificate_number, status=1,checked_organization=checked_organization, appliance_id=appliance.id,last=1)
            certificate.save()

            history = History(date=datetime.now(), status=6, user_id=user_id,appliance_id=appliance.id)
            # status = 6 bolsa yangi pribor qoshgan
            history.save()

        # status = 6 degani bu passport yangi 1 yil sroq bor degani
        messages.success(request, "Yangi pribor qo'shildi !")
        return HttpResponseRedirect(href)

def add(request):
    if request.method == 'POST':
        issue_date = request.POST.get('issue_date')
        expiry_date = request.POST.get('expiry_date')
        checked_organization = request.POST.get('checked_organization')
        user_id = request.POST.get('user_id')
        item_id = request.POST.get('item_id')
        href = request.POST.get('href')
        file = request.FILES['file']
        filess=Certificate.objects.filter(appliance_id=item_id)

        for i in filess:
            i.last=0
            i.save()

        certificate = Certificate(expiry_date=expiry_date, issue_date=issue_date,checked_organization=checked_organization, file=file,appliance_id=item_id,status=1,last=1)
        certificate.save()
        item = Appliance.objects.filter(id=item_id).first()
        item.status = 0
        item.save()

        history = History(date=datetime.now(), status=7, user_id=user_id,appliance_id=item_id)
        # status = 7 bolsa yangi sertifikat qoshish
        history.save()

        messages.success(request, "Yangi sertificat qo'shildi !")
        return HttpResponseRedirect(href)


def show(request,id):
    import datetime
    item = Appliance.objects.filter(id=id).first()
    certificates = Certificate.objects.filter(appliance=id)
    current_year = datetime.datetime.now().year
    current_day = datetime.datetime.now().day
    current_month = datetime.datetime.now().month

    user_type=Profile.objects.filter(user_id=request.user.id).first()
    # filter(file__isnull=False)
    count = Certificate.objects.filter(appliance=id).filter(~Q(file='')).count()
    context = {'item':item,'count':count,'certificates':certificates,'user_type': user_type,'current_year':current_year,'current_day':current_day,'current_month':current_month}
    return render(request, 'show.html', context)

def delete_item(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('data-id')
        user_id = data.get('data-user')


        item = Appliance.objects.filter(id=id).first()
        item.is_delete = True
        item.save()

        history = History(date=datetime.now(), status=8, appliance_id=id, user_id=user_id, comment="Priborni o'chirgan")
        history.save()
        messages.success(request, "Pribor o'chirildi !")
        return HttpResponse(1)
    else:
        return HttpResponse(0)

def send_comment(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        href1 = request.POST.get('href1')
        comment = request.POST.get('comment')
        user_name = request.POST.get('user_name')
        user_company = request.POST.get('user_company')

        item = Appliance.objects.filter(id=item_id).first()

        note = History(user_name=user_name, user_company=user_company,item_name=item.name,comment=comment,item_id=item_id)
        note.save()

        context = {'name': item.name, 'id_number': item.id_number,'comment':comment}

        template = render_to_string('email.html', context)
        text_content = strip_tags(template)
        email = EmailMultiAlternatives(
            'Hurmatli adminstartor sizga xabar bor !',
            text_content,
            'ravotcha1992@gmail.com',
            ['erkaboy756.5313@gmail.com']
        )

        email.attach_alternative(template, 'text/html')
        email.send()

        messages.success(request, "Tavfsilot adminstratorga yuborildi !")
        return HttpResponseRedirect(href1)

def action(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        invalid_comment = request.POST.get('invalid_comment')
        href1 = request.POST.get('href1_2')
        user_id = request.POST.get('user_id')
        status_obj = request.POST.get('status')
        time = request.POST.get('date')
        item=Appliance.objects.filter(id=id).first()

        if status_obj != '0':
            if status_obj == '1':
                history = History(date=time,status=1,appliance_id=id,user_id=user_id,comment=invalid_comment)
                item.status=1
                # status =1 bolsa vaqtincha yaroqsiz pribor
                item.save()
                history.save()

            elif status_obj == '2':
                history = History(date=datetime.now(), status=2, appliance_id=id, user_id=user_id,
                                  comment=invalid_comment, invalid_file=request.FILES['invalid_file'])
                item.status=2
                # status =2 bolsa pribor yaroqsiz hisoblanadi
                item.save()
                history.save()

            elif status_obj == '3':
                history = History(date=time, status=3, appliance_id=id, user_id=user_id, comment=invalid_comment)
                item.status=3
                # status = 3 bolsa pribor tuzatildi
                item.save()
                history.save()
        messages.success(request, "Pribor tavsilotadi yuborildi !")
        return HttpResponseRedirect(href1)
    else:
        return HttpResponseRedirect('/')

def do_valid(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        item = Appliance.objects.filter(id=id).first()
        item.status=0
        # status = 0 bolsa yaroqli
        item.save()

        messages.success(request, "Qurilma yaroqli deb belgilandi !")
        return HttpResponse(1)

    else:
        return HttpResponse(0)

def edit_certificate(request):
    if request.method == 'POST':
        data = request.POST
        issue_date_edit = data.get('issue_date_edit')
        expiry_date_edit = data.get('expiry_date_edit')
        checked_organization_edit = data.get('checked_organization_edit')
        certificate_id = data.get('certificate_id')
        id = data.get('id')
        file_edit = request.FILES.get('file_edit')
        user_id = data.get('user_id')

        # print(file_edit)

        certificate = Certificate.objects.filter(id=certificate_id).first()
        certificate.issue_date=issue_date_edit
        certificate.expiry_date=expiry_date_edit
        certificate.checked_organization=checked_organization_edit
        certificate.file=file_edit
        certificate.appliance_id=id
        certificate.save()

        history = History(date=datetime.now(), status=5, appliance_id=id, user_id=user_id,
                          comment='Sertificate o\'zgartirildi')
        # status = 5 bolsa sertificat o'zgartirilgan boladi'
        history.save()

        messages.success(request, "Ma'lumotlar o'zgartirildi !")
        return HttpResponse(1)

    else:
        return HttpResponse(0)

def edit_certificate_response(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('category_id')
        certificate = Certificate.objects.filter(pk=id).values()
        # print(certificate)
        return JsonResponse({'certificate': list(certificate)},safe=False)

    else:
        return HttpResponse(0)


def delete_certificate(request):
    if request.method == 'POST':
        data = request.POST
        certificate_id = data.get('certificate_id')
        user_delete_id = data.get('user_delete_id')
        appliance_id = data.get('appliance_id')

        certificate = Certificate.objects.filter(id=certificate_id).first()
        certificate.delete()

        certificate_last=Certificate.objects.filter(appliance_id=appliance_id).last()
        certificate_last.last=1
        certificate_last.save()

        history = History(date=datetime.now(),appliance_id=appliance_id,user_id=user_delete_id,status=4,comment="Sertifikat o'chirildi")
        history.save()
        messages.success(request, "Sertifikat o'chirildi !")
        return HttpResponse(1)

    else:
        return HttpResponse(0)

def search(request):
    if request.method == 'POST':
        import datetime
        category_id = request.POST.get('category_id')

        id_number_item = request.POST.get('id_number_item')
        name_item = request.POST.get('name_item')
        belongs_to_item = request.POST.get('belongs_to_item')
        responsible_user = request.POST.get('responsible_user')
        issue_date_item = request.POST.get('issue_date_item')
        expiry_date_item = request.POST.get('expiry_date_item')
        status_value = request.POST.get('status_value')
        status_passport_value = request.POST.get('status_passport_value')
        department_search = request.POST.get('department_search')
        category = Category.objects.filter(id=category_id).first()

        categories=Category.objects.all()

        subcategories = Subcategory.objects.all()
        persons = ResponsiblePerson.objects.all()
        certificates = 0

        current_year = datetime.datetime.now().year
        current_day = datetime.datetime.now().day
        current_month = datetime.datetime.now().month

        if status_value:
            if status_value == '1':
                # status_value == '1': barcha priborlar
                items = Appliance.objects.all()
            elif status_value == '2':
                # status_value == '2': yaroqli priborlar
                items = Appliance.objects.filter(Q(status=0) | Q(status=7))
            elif status_value == '5':
                items = Appliance.objects.filter(status=2)
                # status_value == '2': yaroqsiz priborlar
            elif status_value == '6':
                items = Appliance.objects.filter(status=1)
                # status_value == '6': vaqtincha yaroqsizlar

            elif status_value == '7':
                items = Appliance.objects.filter(status=3)
                # status_value == '7': tuzatilgan priborlar

            elif status_value == '3':
                certificates = Certificate.objects.filter(expiry_date__year=current_year,
                                                          expiry_date__month=current_month,
                                                          expiry_date__day__gt=current_day).filter(last=1)
                items = 0
            elif status_value == '4':
                certificates = Certificate.objects.filter(
                    expiry_date__year__lt=current_year).filter(last=1) or Certificate.objects.filter(
                    expiry_date__year=current_year,
                    expiry_date__month__lt=current_month).filter(last=1) or Certificate.objects.filter(
                    expiry_date__year=current_year,
                    expiry_date__month=current_month,
                    expiry_date__day__lte=current_day).filter(last=1)

                items = 0
                # 4 bosa tugaagan
            else:
                items = 0

        elif status_passport_value:
            if status_passport_value == '1':
                items = Appliance.objects.filter(status_passport=1)
            elif status_passport_value == '2':
                items = Appliance.objects.filter(status_passport=0)
            else:
                items = 0

        elif name_item:
            items = Appliance.objects.filter(name__contains=name_item)

        elif belongs_to_item:
            certificates = Certificate.objects.filter(checked_organization__contains=belongs_to_item).filter(last=1)
            items = 0

        elif responsible_user:
            items = Appliance.objects.filter(responsible_user=responsible_user)
        elif id_number_item:
            items = Appliance.objects.filter(inv_number__contains=id_number_item)

        elif issue_date_item and expiry_date_item:
            date_b = datetime.datetime.strptime(request.POST.get('issue_date_item'), '%Y-%m-%d')
            date_e = datetime.datetime.strptime(request.POST.get('expiry_date_item'), '%Y-%m-%d')
            certificates = Certificate.objects.filter(expiry_date__range=(date_b, date_e)).filter(last=1)
            items = 0

        elif category_id != '-1':
            items = Appliance.objects.filter(category_id=category_id)

        elif department_search != 0:
            items = Appliance.objects.filter(subcategory=department_search)
        else:
            items = 0
        context = {'items': items, 'category': category, 'certificates': certificates, 'subcategories': subcategories,
                   'persons': persons,'categories':categories}
        return render(request, 'items.html', context)
    else:
        return redirect('/')

def search_item(request):
    if request.method == 'POST':
        import datetime
        category_id = request.POST.get('category_id')
        id_number_item = request.POST.get('id_number_item')
        name_item = request.POST.get('name_item')
        checked_organization = request.POST.get('checked_organization')
        responsible_user = request.POST.get('responsible_user')
        issue_date_item = request.POST.get('issue_date_item')
        expiry_date_item = request.POST.get('expiry_date_item')
        status_value = request.POST.get('status_value')
        status_passport_value = request.POST.get('status_passport_value')
        department_search = request.POST.get('department_search')
        category = Category.objects.filter(id=category_id).first()

        subcategories = Subcategory.objects.all()
        persons = ResponsiblePerson.objects.all()
        certificates=0

        current_year = datetime.datetime.now().year
        current_day = datetime.datetime.now().day
        current_month = datetime.datetime.now().month

        if status_value:
            if status_value == '1':
                items = Appliance.objects.filter(category_id=category_id)
            elif status_value == '2':
                items = Appliance.objects.filter(Q(status=0) | Q(status=7)).filter(category_id=category_id)
            elif status_value == '5':
                items = Appliance.objects.filter(status=2).filter(category_id=category_id)

            elif status_value == '6':
                items = Appliance.objects.filter(status=1).filter(category_id=category_id)
                # 6 bolsa vaqtincha yaroqsiz

            elif status_value == '7':
                items = Appliance.objects.filter(status=3)
                # status_value == '7': tuzatilgan priborlar

            elif status_value == '3':
                # 3 bosa kam qolgan
                certificates = Certificate.objects.filter(expiry_date__year=current_year,
                                                          expiry_date__month=current_month,
                                                          expiry_date__day__gt=current_day).filter(appliance__category_id=category_id).filter(last=1)
                # items = Appliance.objects.filter(category_id=category_id).filter(appliances__expiry_date__year=current_year,
                #                                     appliances__expiry_date__month=current_month,
                #                                     appliances__expiry_date__day__gt=current_day)

                items = 0
            elif status_value == '4':
                certificates = Certificate.objects.filter(
                    expiry_date__year__lt=current_year).filter(appliance__category_id=category_id).filter(last=1) or Certificate.objects.filter(
                    expiry_date__year=current_year,
                    expiry_date__month__lt=current_month).filter(appliance__category_id=category_id).filter(last=1) or Certificate.objects.filter(
                    expiry_date__year=current_year,
                    expiry_date__month=current_month,
                    expiry_date__day__lte=current_day).filter(appliance__category_id=category_id).filter(last=1)

                items = 0
                # 4 bosa tugaagan
            else:
                items = 0

        elif status_passport_value:
            if status_passport_value == '1':
                items = Appliance.objects.filter(status_passport=1).filter(category_id=category_id)
            elif status_passport_value == '2':
                items = Appliance.objects.filter(status_passport=0).filter(category_id=category_id)

        elif name_item:
            items = Appliance.objects.filter(name__contains=name_item).filter(category_id=category_id)

        elif checked_organization:
            certificates = Certificate.objects.filter(checked_organization__contains=checked_organization).filter(appliance__category_id=category_id).filter(last=1)
            # items = Appliance.objects.filter(category_id=category_id).filter(certificates.appliances.filter(
            #     checked_organization__contains=checked_organization).last())
            items = 0

        elif responsible_user:
            items = Appliance.objects.filter(responsible_user=responsible_user).filter(category_id=category_id)

        elif id_number_item:
            items = Appliance.objects.filter(inv_number__contains=id_number_item).filter(category_id=category_id)

        elif issue_date_item and expiry_date_item:
            date_b = datetime.datetime.strptime(request.POST.get('issue_date_item'), '%Y-%m-%d')
            date_e = datetime.datetime.strptime(request.POST.get('expiry_date_item'), '%Y-%m-%d')
            certificates =Certificate.objects.filter(expiry_date__range=(date_b, date_e)).filter(last=1)
            items = 0
            # items = Appliance.objects.filter(category_id=category_id).filter(appliances__expiry_date__range=(date_b, date_e))

        elif department_search != 0:
            items = Appliance.objects.filter(subcategory=department_search).filter(category_id=category_id)
        else:
            items = 0
        context = {'items': items, 'category': category,'certificates':certificates,'subcategories':subcategories,'persons':persons}
        return render(request,'items_with_category.html',context)
    else:
        return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        if User.objects.filter(username=username).first() or User.objects.filter(email=email).first():
            messages.error(request, "Bu foydalanuvchi avval ro'yhatdan o'tgan!")
            return HttpResponseRedirect('/')

        else:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],password=request.POST['pwd'])
            profile = Profile(user_id=user.id, company=request.POST['company'], admin_type=0, permission=False)
            profile.save()
            messages.success(request, "Siz ro'yhatdan o'tdingiz adminstrator tasdiqlashini kuting!")
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        psw = request.POST.get('psw')
        user = authenticate(request, username=uname, password=psw)
        if user is not None:
            profile = Profile.objects.filter(user=user).first()
            if profile.permission:
                dj_login(request,user)
                messages.success(request, "Foydalanuvchi siz tizimga kirdingiz !")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Sizga ruhsat berilmagan ! Kutishingizni so'raymiz ! Adminga murojat qiling !")
                return HttpResponseRedirect('/')

        else:
            messages.error(request, "Bunday foydalanuvchi mavjud emas !")
            return HttpResponseRedirect('/')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
