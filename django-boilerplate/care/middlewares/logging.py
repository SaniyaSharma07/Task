import time
from uuid import uuid4

from django.urls import resolve

from commons.utils.loggers import log_request, log_response
from commons.utils.json import is_json


class LoggingMiddleware:
    '''Middleware for logging the incoming request, outgoing response and errors (if any).
    '''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''Handler method for middleware

        Args:
            request: Django's request object.

        Returns:
            Response passed by next middleware or view.

        '''
        request_id = str(uuid4())
        setattr(request, 'request_id', request_id)
        request_epoch = time.time()*1000

        request_parameters = resolve(request.path_info)
        request.url_info = {
            'kwargs': request_parameters.kwargs,
            'url_name': request_parameters.url_name,
            'app_names': request_parameters.app_names,
            'app_name': request_parameters.app_name,
            'namespaces': request_parameters.namespaces,
            'namespace': request_parameters.namespace,
            'view_name': request_parameters.view_name
        }

        request = log_request(request_id, request, request_epoch, request_parameters.view_name)

        response = self.get_response(request)

        log_response(request_id, request, request_epoch, response)

        return response
