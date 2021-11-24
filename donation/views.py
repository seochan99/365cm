from django.shortcuts import render, redirect ,get_object_or_404
from .models import Donate
from django.utils import timezone

# Create your views here.
def donate(request):
    donations = Donate.objects.all()
    return render(request, 'donation/donate.html', {'donations':donations})

def donate_detail(request, id):
    donation = get_object_or_404(Donate, pk=id)
    return render(request, 'donation/donate_detail.html', {'donation':donation})

def donate_new(request):
    return render(request, 'donation/donate_new.html')

def donate_create(request):
    new_donation = Donate()
    new_donation.writer = request.user
    new_donation.pub_date = timezone.now()
    new_donation.hair_length = request.POST['hair_length']
    new_donation.hair_condition = request.POST['hair_condition']
    new_donation.body = request.POST['body']
    new_donation.image = request.FILES['image']
    new_donation.save()
    return redirect('donation:donate_complete')

def donate_edit(request, id):
    edit_donation = Donate.objects.get(id=id)
    return render(request, 'donation/donate_edit.html', {'donation':edit_donation})

def donate_update(request, id):
    update_donation = Donate.objects.get(id=id)
    update_donation.writer = request.user
    update_donation.pub_date = timezone.now()
    update_donation.hair_length = request.POST['hair_length']
    update_donation.hair_condition = request.POST['hair_condition']
    update_donation.body = request.POST['body']
    update_donation.save()
    return redirect('donation:donate_detail', update_donation.id)

def donate_delete(request, id):
    delete_donation = Donate.objects.get(id=id)
    delete_donation.delete()
    return redirect('donation:donate')

def donate_complete(request):
    return render(request, 'donation/donate_complete.html')