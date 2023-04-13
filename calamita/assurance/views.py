from os.path import join, exists

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from calamita.settings import STATICFILES_DIRS
from .models import Node


CHAIN_PATH = join(STATICFILES_DIRS[0], 'blockchain.json')


@method_decorator(csrf_exempt, name='dispatch')
class ChainView(View):

    def get(self, request):
        return HttpResponse(update_blockchain())

    def post(self, request: HttpRequest):
        print(request.POST.get('document'))
        update_blockchain(read=False, data=request.POST.get('document'))
        return HttpResponse()


@method_decorator(csrf_exempt, name='dispatch')
class NodesView(View):

    def post(self, request):
        pk = request.POST.get('public_key')
        host = request.POST.get('host')
        if Node.objects.filter(public_key=pk).exists():
            node = Node.objects.get(public_key=pk)
            node.host = host
            node.save()
        else:
            node = Node(public_key=pk, host=host)
            node.save()

        return JsonResponse(
            list(Node.objects.values('public_key', 'host')),
            safe=False
        )


def update_blockchain(read=True, data=''):
    if read:
        if not exists(CHAIN_PATH):
            return ''
        with open(CHAIN_PATH) as f:
            return f.read()
    with open(CHAIN_PATH, 'w') as f:
        return f.write(data)
