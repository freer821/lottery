from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
import logging

logger = logging.getLogger('sys')


def getStandardResponse(status, msg='', data=''):
    return {
        'status': status,
        'msg': msg,
        'data': data
    }


class SysRequestResponseMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(SysRequestResponseMiddleware, self).__init__(*args, **kwargs)

    def process_template_response(self, request, response):
        if not response.is_rendered and isinstance(response, Response):
            if isinstance(response.data, dict):

                keys = response.data.keys()
                if "swagger" in keys:
                    return response

                if "status" in keys and "msg" in keys:
                    return response
                else:
                    if response.status_code < 300:
                        response.data = getStandardResponse(200, '', response.data)
                    else:
                        response.data = getStandardResponse(response.status_code, response.data)

                    response.status_code = 200
            elif response.status_code < 300:
                response.status_code = 200
                response.data = getStandardResponse(200)
            else:
                response.status_code = 200
                response.data = getStandardResponse(500)

        return response


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
