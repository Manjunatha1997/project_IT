from django.shortcuts import render
from login.models import *
from datetime import datetime, timedelta, date
from timer.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/auth/login/")
def home(request):
    # get currently logged in user profile
    profile_info = Profile.objects.get(user=str(request.user))
    name = profile_info.name
    profile = profile_info.profile.url

    # getting todays date
    today = date.today()
    # today - 4 days before
    start_date = today - timedelta(days=4)

    # today + 4 days after
    end_date = today + timedelta(days=4)

    print(start_date, end_date)

    # find the start date
    start_day = start_date.day
    # find end day
    end_day = end_date.day

    print("DAY =>", start_day, end_day)

    # current month
    month = datetime.now().month # 02
    # current year
    year = datetime.now().year

    birthday_users = []
    ann_users = {}
    # get all employees/users
    all_users = Profile.objects.all()
    for user in all_users:
        # get user's date of birth
        bday = user.dob
        # find day
        birth_day = bday.day
        # find month
        birth_month = bday.month
        #print(user.name, user.dob)
        # check if this user's birthday is in this month
        if month == birth_month: # 02
            # check if birthday is in this week
            if birth_day >= start_day and birth_day <= end_day:
                birthday_users.append(user)


        doj = user.doj # 2017-12-09
        ann_month = doj.month
        ann_day = doj.day
        ann_year = doj.year

        # skip if user has joined this year
        if ann_year != year:
            # if if user joined in this month of previous years
            if ann_month == month:
                # ann_users.append(user)
                ann_users[user] = year - ann_year
    ##############################################################
    ## create project report
    ##############################################################
    projects = list(TimeSheetData.objects.all().values_list('project').distinct())
    projects = [i[0] for i in projects]
    ##############################################################

    # pass name, profile pic, all users whose birthday is this week
    return render(request, "home/home.html", {'name': name, 'profile': profile, 'users': birthday_users, 'ann_users': ann_users})


def project_data(request, name):
    name = 'Project Tracker'
    projects = TimeSheetData.objects.filter(project=name)
    count = 0

    time = {}
    for project in projects:
        user = project.user
        time[user] = time.get(user, 0) + project.hours
        count = count + project.hours

    return render(request, "home/project.html", {'users': time, 'count': count})