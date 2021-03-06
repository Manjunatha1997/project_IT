import os
from random import *
from faker import Faker
from random import randrange, randint
from datetime import datetime

f = Faker()

os.environ['DJANGO_SETTINGS_MODULE'] = 'Tracker.settings'
import django
django.setup()

from login.models import *
from leave.models import *
from django.contrib.auth.models import User


# below are managers employee id
managers = (
            ('1000'),
            ('1010'),
            ('1020'),
            ('1040'),
            ('1030'),
)

# below are different designation available in company
designations = (
            ('Trainee Engineer'),
            ('Software Engineer'),
            ('Lead Engineer'),
            ('Analyst'),
            ('Admin'),
)

# primary skill
PS = (
    'Python',
    'C#',
    'Perl',
    'Java',
    'Scala',
)

# Qualifications
Qual = (('BE'), ('ME'), ('MTech'), ('CA'), ('MA'))

# Birth years for each employee
years = [1984, 1985, 1989, 1983, 1982]

# list of projects
projects = (
    ('Flow Development', 'Flow Development'),
    ('Flow Tester', 'Flow Tester'),
    ('Project Tracker', 'Project Tracker'),
    ('Clearcase Developer', 'Clearcase Developer'),
    ('Regression Tool', 'Regression Tool'),
)

#################################################
## create the user and profile for every user
## username will be <userid>
## password will be 'resu@<userid>'
#################################################
def populate_profile(start, end):
    for i in range(start, end+1):
        out = 'resu' + '@' + str(i)
        user = User.objects.create_user(username=str(i), email='user' + str(i) + '@gmail.com', password=out)
        uid = str(i)
        name = f.name()
        profile = "images/" + str(i) + ".jpg"
        mobile = "9845" + str(randrange(100000, 999999))
        manager = managers[randint(0,4)]
        primary = PS[randint(0,4)]
        project = projects[randint(0,4)][0]
        designation = designations[randint(0,4)]
        qual = Qual[randint(0,4)]
        dob = datetime(randrange(1980, 1995), randrange(1,13), randrange(1, 28))
        doj = datetime(randrange(2010, 2018), randrange(1,13), randrange(1, 28))
        email = 'lovelymanju198@gmail.com'
        Profile.objects.create(user=uid, name=name, profile=profile, mobile=mobile, manager=manager, primary_skill=primary, designation=designation, doj=doj, dob=dob, qual=qual, project=project, email=email)

######################################################
## add leaves to every employee created
######################################################
data = {
	'Sick Leave' : [0, 8, 0, 8],
	'Earned Leave' : [5, 20, 0, 25],
	'Paternity Leave' : [0,0,0,0],
	'Loss of Pay' : [0,0,0,0],
	'Relocation Leave': [0,0,0,0],
}

def populate_leaves(x, y): # 1000, 1100
    for i in range(x, y + 1):
        user = str(i) # user = 1000
        for leave_type in data:
            preivous_balance = data[leave_type][0]
            total = data[leave_type][1]
            used = data[leave_type][2]
            balance = data[leave_type][3]
            Leave.objects.create(user=user, leave_type=leave_type, preivous_balance=preivous_balance,
                                        total=total, used=used, balance=balance)

emp_start = 1000 # resu@1000
emp_end = 1100

populate_profile(emp_start, emp_end)
populate_leaves(emp_start, emp_end)

"""
populate_profile
Above script going to create 100 users(in the backend, 
otherwise we have create user by using signup) or by using python manage.py createsuperuser
employee id 1000 to 1100
password for each employee will be resu@<empid>
Ex: to login to 1010, userid will be 1010 password will resu@1010
Apart from creating users, it will populate leaves for every user..
login to mysql and check data inside login_profile

populate_leaves
Inserts leave information to every employee
login to mysql and asee -> sick_leave to relocation leave.. check in table leave_leave
"""