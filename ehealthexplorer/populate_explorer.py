import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealthexplorer.settings')

import django
django.setup()

from explorer.models import Category, Page, User

def populate():

    jill = add_user('jill','jill@jill.com','jill')
    bob = add_user('bob','bob@bob.com','bob')
    joe = add_user('joe','joe@joe.com','joe')

    flu_cat = add_cat(jill,'Flu',True)
    add_page(cat=flu_cat,
             title="Protections from Seasonal Flu",
             summary="Summary 1",
             url="http://healthfinder.gov/HealthTopics/Category/doctor-visits/shotsvaccines/protect-yourself-from-seasonal-flu")
    add_page(cat=flu_cat,
             title="Flu Symptoms",
             summary="Summary 2",
             url="http://www.nhs.uk/Conditions/Flu/Pages/Symptoms.aspx")


    cancer_cat = add_cat(bob,'Cancer')
    add_page(cat=cancer_cat,
             title="Throat Cancer",
             summary="Summary 1",
             url="https://www.nlm.nih.gov/medlineplus/throatcancer.html")
    add_page(cat=cancer_cat,
             title="Tests for Breast Cancer",
             summary="Summary2",
             url="http://www.cancerresearchuk.org/about-cancer/type/breast-cancer/diagnosis/breast-cancer-tests")

    sclerosis_cat = add_cat(bob,'Sclerosis',True)
    add_page(cat=sclerosis_cat,
             title="Sclerosis topic",
             summary="Summary of scleroris",
             url="https://www.nlm.nih.gov/medlineplus/throatcancer.html")
    add_page(cat=sclerosis_cat,
             title="Symptoms of sclerosis",
             summary="Summary2",
             url="https://www.google.com")

    diabetes_cat = add_cat(joe,'Diabetes')
    add_page(cat=diabetes_cat,
             title="Type 1",
             summary="Summary",
             url="https://www.nlm.nih.gov/medlineplus/diabetestype1.html")
    add_page(cat=diabetes_cat,
             title="Type 2",
             summary="Summary1",
             url="https://www.nlm.nih.gov/medlineplus/diabetestype2.html")

def add_user(user,email,passwd):
    u = User(username=user,email=email)
    u.set_password(passwd)
    u.save()
    return u


def add_page(cat,title,summary,url):
    p = Page.objects.get_or_create(category=cat,title=title)[0]
    p.title = title
    p.summary = summary
    p.url = url
    p.save()
    return p

def add_cat(user,name,shared=False):
    c = Category.objects.get_or_create(user=user,name=name)[0]
    c.name = name
    c.shared = shared
    c.save()
    return c

if __name__ == '__main__':
    print "Starting Explorer population script..."
    populate()
