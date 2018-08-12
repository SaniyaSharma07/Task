import os
import traceback

from django.conf import settings

from commons.utils.http_error import Unauthorized
from commons.utils.request_client import make_request


class AuthenticationMiddleware:
    '''Middleware for authenticating the user using authorization token and appending
    authorized user's information in Django's request object.

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
            Unauthorized http error if request could not be authorized.

        '''

        setattr(request, 'user_data', {})

        try:
            auth_token = request.META.get('HTTP_AUTHORIZATION')

        except Exception:
            raise Unauthorized

        response_json, response_content, response_code, error = make_request(
            url=settings.AUTHENTICATION_URL,
            method='GET',
            headers={'Authorization': auth_token}
        )

        if int(response_code)/100 != 2:
            raise Unauthorized

        if not response_json.get('data', {}).get('user_id'):
            raise Unauthorized('The request could not be authorized. The sent token could not be validated.')

        setattr(request, 'user_data', response_json.get('data', {}))
        response = self.get_response(request)
        return response
