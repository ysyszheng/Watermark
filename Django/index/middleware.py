import logging
import time
logger = logging.getLogger('network_traffic')

class NetworkTrafficLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        response = self.get_response(request)

        # 记录请求的相关信息和时间
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log_message = f"{current_time} - IP: {request.META['REMOTE_ADDR']}, Method: {request.method}, " \
                      f"Path: {request.path}, Status Code: {response.status_code}"
        logger.info(log_message)

        return response