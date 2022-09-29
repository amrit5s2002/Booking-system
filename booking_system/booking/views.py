from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def welcome(request):
    sum = 0
    total = 500
    if request.method == 'POST':
        
        
        seq = []
        print(request)
        form = BookingForm(request.POST)
        
        
        if form.is_valid():
            numOfSeats = form.cleaned_data.get('numOfSeat')
            rows = form.cleaned_data.get('rows')
            columns = form.cleaned_data.get('column')
            Lst = [rows,columns]
            seq = []
            booked_seats = Booking.objects.all()
            for i in booked_seats:
                row = i.rows
                col = i.column
                lst = [row,col]
                seq.append(lst)
                # print(lst)
                
            for i in booked_seats:
                sum += i.numOfSeat
            total_seats = sum + numOfSeats
            left = 500-total_seats
    
            if total_seats <= total:
                if Lst not in seq:
                    form.save()
                    return render(request,'booking/bookform.html',{'form':form,'total':sum + numOfSeats,'left':left})
            else:
                return HttpResponse('number of seats are exeeding the limit. <br> Please reduce number of seats to make it under the limit')
    
    else:
        form = BookingForm()
        print(request.method)
        return render(request,'booking/bookform.html',{'form':form})


    
