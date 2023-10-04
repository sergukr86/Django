from django.http import HttpResponse

from faker import Faker

from polls.models import Student


fake = Faker()


def create_st():
    Student.objects.create(
        first_name=fake.first_name(), last_name=fake.last_name(), birth_date=fake.date()
    )


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def gen_student(request):
    create_st()
    return HttpResponse("Student is ready!")


def students(request):
    count_param = request.GET.get("count", 100)
    if not count_param.isdigit():
        return HttpResponse(
            "Parameter 'count' is not a digit, please enter number parameter."
        )
    else:
        num = int(count_param)
        if num > 100:
            num = 100
        for i in range(0, num):
            create_st()
        return HttpResponse("Students are ready to work!")
