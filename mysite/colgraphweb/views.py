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
    path = '/home/aalok/code/coloring-graphs/in/hexmod.in'
    # path = '/home/aalok/code/coloring-graphs/in/bipartite_test_graph0.in'
    bg.load_txt(path)
    #mbg = bg.tarjans()
    
    cg = bg.build_coloring_graph(4)  
    print(type(cg))
    mcg = cg.tarjans()
    
    data = dict()
    data.update(lcg.viz.to_visjs(bg))
    data.update(lcg.viz.to_visjs(cg))
    data.update(lcg.viz.to_visjs(mcg))
    
    if request.method == 'GET':
        response = HttpResponse(template.render(context=data))
        # print(response.content)
        return response
        
    return HttpResponse("ERROR")
    
