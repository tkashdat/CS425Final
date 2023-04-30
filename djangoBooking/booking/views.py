from django.shortcuts import render
from django.http import JsonResponse
from booking.models import Users, Discount
from django.core.serializers import serialize
import json

# Create your views here.
# user_id = 1
# user_payments = Payments.objects.all(pk=user_id)

# payment_id = 1
# payment = Payments.objects.get(pk=payment_id)
# payment.delete()

# def delete_payment(request):
#     post = Payments.objects.get(pk=request.body.post_id)
#     post.delete()

#     return render(request)

def booking(request):
    # user = Users.objects.get(pk=1)
    # return HttpResponse(user)
    # return HttpResponse(user)
    return JsonResponse({"Hello World"})

# def test(request):
#     # user = Users.objects.all()
#     user = Users.objects.get(user_id=1)
#     return render(request, 'test.html', {
#         'user': user
#     })

def test(request):
    user = Discount.objects.all()
    # return JsonResponse({'user': user})
    # return JsonResponse('{ "user": "apes" }', '', 0)
    
    # return print(user.__dict__)
    serialized_data = serialize("json", user)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, safe=False)