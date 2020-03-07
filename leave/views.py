from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail

from leave.forms import *
from leave.models import *

import calendar
from datetime import timedelta, date, datetime
import re
from login.models import *

# to find day of a given date(Monday-Sunday)
def find_day(date):
    date = datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[date])

# given 2 dates, below function expands the dates
# Example: 20/12/2019 -> 24/12/2019, return list is below
# [20/12/2019, 21/12/2019, 22/12/2019 .. 23/12/2019 23/12/2019]
def date_range(start_date, end_date):
    all_dates = []
    for n in range(int((end_date - start_date).days)):
        all_dates.append(start_date + timedelta(n))
    return all_dates


def apply_leave(request):
    form = ApplyLeaveForm()
    if request.method == "POST":
        form = ApplyLeaveForm(request.POST)
        if form.is_valid():
            # get start and end date of leaves
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']

            # get leave type to know which leave is applied
            # assume, sick leave applied
            leave_type = form.cleaned_data['leave_type']
            remark = form.cleaned_data['remark']

            # count of leave
            days = (end - start).days + 1

            if days<1:
                messages.error(request,'don not allows negative cases' )
                return redirect('/leave/apply_leave')

            # find all dates between select start and end date
            # Example: 20/12/2019 -> 25/12/2019
            # [20/12/2019, 21/12/2019, 22/12/2019 .. 25/12/2019]
            all_dates = date_range(start, end)

            for d in all_dates:

                # check if leave date is already a holiday
                #if Holidays.objects.filter(date=d).count() > 0:
                #    days = days - 1
                #    continue
                if d.weekday() == 5 or d.weekday() == 6:
                    days = days - 1
                #d = d.strftime('%d %m %Y')
                # check if leave date is Saturday/Sunday
                #if re.search("Sat|Sun", find_day(d), flags=re.I):
                #    days = days - 1

            # get the manager for currently logged-in user
            profile = Profile.objects.get(user=request.user)
            manager = profile.manager

            # default status will be pending
            status = "Pending"

            user = str(request.user)

            # before applying leave check leave.balance >= days
            # get sick leave for currently logged-in user
            leave = Leave.objects.get(user=user, leave_type=leave_type)
            # Assume, user has applied 3 days leave
            # leave.used should be increased by 3 days
            leave.used = leave.used + days
            # leave.used should be descreased by 3 days
            leave.balance = leave.balance - days
            leave.save()

            messages.info(request, 'Successfully applied leave!!')

            # insert leave data to the table
            AppliedLeaves.objects.create(user=str(request.user), start_date=start, end_date=end, days=days, leave_type=leave_type,
                                         remark=remark, status=status, approver=manager)

            # code to send email
            manager_data = Profile.objects.get(user=str(manager))

            recepient = [manager_data.email]
            subject = 'Leave ' + str(request.user)
            message = str(request.user) + " applied leave for " + str(days) + " days from " + str(start) + " to " + str(end)
            email_from = 'django.training.2019@gmail.com'

            send_mail(subject, message, email_from, recepient)
            #return redirect("/")
            return redirect("/leave/apply_leave/")
    # get all available leaves of currently logged-in user
    leaves = Leave.objects.filter(user=str(request.user))
    return render(request, r'leave/apply_leave.html', {'leaves': leaves, 'form': form})


def approve_leave(request):
    # executes for manager
    # get all applied leaves from AppliedLeaves where approver is logged-in_user(manager)
    # and status is Pending
    leaves = AppliedLeaves.objects.filter(approver=str(request.user), status='Pending')

    if request.method == "POST":
        for i in range(1, len(leaves) + 1):
            id = leaves[i - 1].__dict__['id']
            # get the changed status(by manager) and update
            leave = AppliedLeaves.objects.get(id=id)
            status = request.POST.get('status' + str(i))
            leave.status = status
            leave.save()
    return render(request, r'leave/approve_leave.html', {'leaves': leaves})
