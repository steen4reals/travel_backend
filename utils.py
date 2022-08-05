from flask import request, redirect

from user_management import username_available


def should_be_signed_in(route_func):
    def decorated_route_func(*args, **kwargs):
        if request.cookies.get('user_id') is None:
            return redirect('/signin')
        return route_func(*args, **kwargs)
    decorated_route_func.__name__ = route_func.__name__
    return decorated_route_func


def should_be_signed_out(route_func):
    def decorated_route_func(*args, **kwargs):
        if request.cookies.get('user_id') is not None:
            return redirect('/')
        return route_func(*args, **kwargs)
    decorated_route_func.__name__ = route_func.__name__
    return decorated_route_func


def get_query_values(*keys):
    if len(keys) == 1:
        return request.args.get(keys[0])
    return map(request.args.get, keys)


def get_form_values(*keys):
    if len(keys) == 1:
        return request.form.get(keys[0])
    return map(request.form.get, keys)


def get_account_creation_error(username, display_name, pin):
    if not 1 <= len(username) <= 20:
        return 'Username must be between 1 and 20 characters long'
    if not username.isalnum():
        return 'Username must only include letters and numbers'
    if not 1 <= len(display_name) <= 20:
        return 'Display name must be between 1 and 50 characters long'
    if not pin.isdigit() or len(pin) != 4:
        return 'Pin must consist of 4 digits'
    if not username_available(username):
        return f'Username {username} is already taken'