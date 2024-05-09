from django.shortcuts import render
from aniachi.systemUtils import Welcome as W
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
import json
import psutil
from django.views.decorators.csrf import csrf_exempt
from .utils import get_dict_from_HL7, value_or_default
from django.views.decorators.csrf import csrf_exempt
from json2html import json2html
from dicttoxml import dicttoxml
import yaml
from hl7apy.parser import parse_segment
from .forms import Simple_submit_Form
from django.core.handlers.wsgi import WSGIRequest
from datetime import datetime




def server_info_view(req: WSGIRequest) -> JsonResponse:
    W.get_all_libs('json')
    return JsonResponse(json.loads(W.get_fetchdata(format='json')), safe=False)



def server_date_view(req: WSGIRequest) -> JsonResponse:
    return JsonResponse({'date': str(datetime.now())})



def default_home_view(req: WSGIRequest) -> HttpResponse:
    return render(req, 'home_page.html')




def process_view(req: WSGIRequest) -> JsonResponse:
    ps = list()
    for proc in psutil.process_iter():
        ps.append(proc.as_dict(
            attrs=['pid', 'name', 'cpu_percent', 'username']))
    return JsonResponse(ps, safe=False)


def server_installed_modules_view(req: WSGIRequest) -> JsonResponse:
    return JsonResponse(W.get_all_libs(ft='json'), safe=False)


#
# TODOS MORE INFO
#
@csrf_exempt
def hl7_web_view(req: WSGIRequest)-> HttpResponse:
    d = {}
    format = value_or_default(req, 'format', 'json')
    data = value_or_default(req, 'data', '')
    try:

        d = get_dict_from_HL7(parse_segment(data))
    except Exception as e:
        d['error'] = str(e)

    if format == 'json':
        return HttpResponse(json.dumps(d), content_type='application/json')
    elif format == 'xml':
        return HttpResponse(dicttoxml(d, custom_root='hl7'), content_type='application/xml')
    elif format == 'html':
        return HttpResponse(json2html.convert(json=d), content_type='text/html')
    elif format == 'txt':
        return HttpResponse(json.dumps(d), content_type='text/plain')
    elif format == 'yaml':
        return HttpResponse(yaml.dump(d), content_type='text/yaml')

    else:
        return HttpResponse(' unavailable format', content_type='application/json')


def _403_view(req: WSGIRequest) -> HttpResponseForbidden:
    return HttpResponseForbidden()


def info_headers_view(req: WSGIRequest) -> HttpResponse:
    return HttpResponse(json.dumps(dict(req.headers)), content_type='application/json')


def render_form_view(req: WSGIRequest) -> HttpResponse:


    return render(req, 'display_form.html', {'form': Simple_submit_Form()})
