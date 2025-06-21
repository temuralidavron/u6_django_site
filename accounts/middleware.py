from django.http import HttpResponseForbidden
import time

class RequestCount:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request = {}

    def __call__(self, request):
        ip = self.get_client_id(request)
        now = time.time()

        if ip not in self.request:
            self.request[ip] = []

        self.request[ip] = [timestamp for timestamp in self.request[ip] if now - timestamp < 10]

        if len(self.request[ip]) >= 5:
            return HttpResponseForbidden("SIz kop request jonatdingiz 5 ta mumkin 10 sekundda")

        self.request[ip].append(now)
        response = self.get_response(request)
        return response

    def get_client_id(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            print(x_forwarded_for)
            ip = x_forwarded_for.split(',')[0]
            print(ip)
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip