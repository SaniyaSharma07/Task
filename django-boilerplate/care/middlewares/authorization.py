from django.conf import settings

from commons.utils.http_error import Forbidden, NotFound
from commons.utils.request_client import make_request


class AuthorizationMiddleware:
    '''Middleware to check if logged in user has access to the requested route.

    Attributes:
        get_response: handler method of next middleware or view
    '''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''Handler method for middleware

        Args:
            request: Django's request object.

        Returns:
            Response passed by next middleware or view.

        Raises:
            NotFound: if route could not be found.
            Forbidden: if logged in user does not have necessary permissions to access the resource.
        '''

        response_json, response_content, response_code, error = make_request(
            url=settings.AUTHORIZATION_URL.format(name=request.url_info["view_name"], method=request.method),
            method='GET',
            headers={'Authorization': request.META.get('HTTP_AUTHORIZATION')}
        )

        if int(response_code) == 404:
            raise NotFound

        elif int(response_code)/100 != 2:
            raise Forbidden

        response = self.get_response(request)
        return response
