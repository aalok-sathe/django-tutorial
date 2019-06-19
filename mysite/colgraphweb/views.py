#!/usr/bin/env python3

# stdlib imports
# django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# our package
import libcolgraph as lcg



def index(request):
    template = loader.get_template('viewtemplate.html')
    
    bg = lcg.BaseGraph()
    bg.load_txt('/home/aalok/code/coloring-graphs/in/hexmod.in')
    cg = bg.build_coloring_graph(4)    
    mg = cg.tarjans()
    
    data = lcg.viz.to_visjs(mg)
    
    if request.method == 'GET':
        response = HttpResponse(template.render(context=data))
        print(response.content)
        return response
        
    return HttpResponse("ERROR")
    
