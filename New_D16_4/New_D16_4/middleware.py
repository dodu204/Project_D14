from django.utils.deprecation import MiddlewareMixin
import logging


class LoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_request(self, request):
        # Логирование запроса
        logger = logging.getLogger('django')
        logger.info('Request: %s %s', request.method, request.path)

    def process_response(self, request, response):
        # Логирование ответа
        logger = logging.getLogger('django')
        logger.info('Response: %s %s', response.status_code, request.path)
