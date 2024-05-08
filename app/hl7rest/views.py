from django.shortcuts import render
from aniachi.systemUtils import Welcome as W
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
import json
import psutil
from django.views.decorators.csrf import csrf_exempt
from .utils import getDictFromHL7, value_or_default
from django.views.decorators.csrf import csrf_exempt
from json2html import json2html
from dicttoxml import dicttoxml
import yaml
from hl7apy.parser import parse_segment
from .forms import Simple_submit_Form


# Create your views here.


def serverInfoView(req):
    """
    for educational purposes


Returns:
    HttpResponse -- Response object with all intalled python modules
"""
    W.get_all_libs('json')
    return JsonResponse(json.loads(W.get_fetchdata(format='json')), safe=False)


"""
    for educational purposes


Returns:
    HttpResponse -- Response object with all intalled python modules
"""


def defaultHomeView(req):
    return render(req, 'home_page.html')


"""
    for educational purposes


Returns:
    HttpResponse -- Response object with all intalled python modules
"""


def processView(req):
    ps = list()
    for proc in psutil.process_iter():
        ps.append(proc.as_dict(
            attrs=['pid', 'name', 'cpu_percent', 'username']))


    return JsonResponse(ps, safe=False)


"""
    for educational purposes


Returns:
    HttpResponse -- Response object with all intalled python modules
"""


def installedModulesView(req):
    return HttpResponse(W.get_all_libs(), content_type='application/json')


#
# TODOS MORE INFO
#
@csrf_exempt
def hl7_web_view(req):
    d = {}
    format = value_or_default(req, 'format', 'json')
    data = value_or_default(req, 'data', '')
    try:

        d = getDictFromHL7(parse_segment(data))
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


def _403View(req):
    """[summary]

    Arguments:
        req {[type]} -- MORE TODOS

    Returns:
        [type] -- [description]
    """
    return HttpResponseForbidden()


def infoheadersView(req):
    """[summary]

    Arguments:
        req {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    return HttpResponse(json.dumps(dict(req.headers)), content_type='application/json')


def render_form_View(req):

    return render(req, 'display_form.html', {'form': Simple_submit_Form()})
