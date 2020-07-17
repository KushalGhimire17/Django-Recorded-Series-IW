from django.http import HttpResponse, JsonResponse
# from django.http import HttpResponseNotFound

def home(request):
    return HttpResponse("Hi, from Home")

def profile(request, username):
    data = {
        'ram': 'Ram Bahadur',
        'shyam': 'Shyam Bahadur',
        'hari': 'Hari Bahadur'
    }

    # full_name = data[username]
    # dict.get() returns None by default
    full_name = data.get(username)
    if not full_name:
        # return HttpResponseNotFound("The username doesn't exists.")
        return HttpResponse("The username doesn't exists.", status=404)
    string_data = f"Your fullname is: {full_name}."
    
    return HttpResponse(string_data)

def profile_json(request, username):
    data = {
        'ram': 'Ram Bahadur',
        'shyam': 'Shyam Bahadur',
        'hari': 'Hari Bahadur'
    }

    full_name = data.get(username)

    if not full_name:
        return HttpResponse("The username doesn't exists.", status=404)

    dict_data = {
        'full_name': full_name
    }
    return JsonResponse(dict_data)

def int_converter_view(request, int_data):
    print("int_data is :", int_data)
    print(type(int_data))
    try:
        _ = int(int_data)
    except ValueError:
        return HttpResponse(status=404)
    return HttpResponse("OKOKOK")

def debug_request(request):
    print("Request Method: ", request.method)
    print("Request Scheme: ", request.scheme)
    print("Request Headers: ", request.headers)
    # 127.0.0.0.0:8000/test-path
    # 127.0.0.0.0:8000/test-path?name=kushal
    print("Request GET: ", request.GET)
    return HttpResponse("Ok from debug")