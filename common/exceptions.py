from django.db import IntegrityError
from django.http import Http404
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed, ValidationError, NotAuthenticated
from rest_framework.response import Response

from .middleware import getStandardResponse, logger


def sys_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    logger.error(str(exc), exc_info=True)
    if isinstance(exc, Http404):
        return Response(getStandardResponse(404, '地址未找到'))
    elif isinstance(exc, PermissionDenied):
        return Response(getStandardResponse(403, '权限不够'))
    elif isinstance(exc, AuthenticationFailed):
        return Response(getStandardResponse(401, 'Token验证失败，需要重新注册'))
    elif isinstance(exc, NotAuthenticated):
        return Response(getStandardResponse(401, '未发现Token'))
    elif isinstance(exc, SysException):
        return Response(getStandardResponse(400, str(exc)))
    elif isinstance(exc, ValidationError):
        return Response(getStandardResponse(400, str(exc)))
    elif isinstance(exc, IntegrityError):
        return Response(getStandardResponse(400, str(exc)))

    return Response(getStandardResponse(500, '系统内部错误，请联系客服!'))


class SysException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
