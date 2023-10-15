from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import jobs
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.urls import reverse

# Create your views here.
def job_list(request):
    job_list = jobs.objects.all()
    paginator = Paginator(job_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = jobs.objects.get(slug=slug)
    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = ApplyForm()
    context = {'jobs': job_detail, 'form': form}
    return render(request, 'job/job_detail.html', context)

def job_add(request):
    if request.method == 'POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm() 
    return render (request, 'job/job_add.html',{'form': JobForm})