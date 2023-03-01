from django.http import HttpResponse
from django.shortcuts import redirect


def unautheticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authenticated to access this page!')

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'staff':
            return redirect('staffDashboard')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func
