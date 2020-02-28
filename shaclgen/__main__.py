# -*- coding: utf-8 -*-
#!/usr/bin/env python

#%%
from .shaclgen import data_graph
from .schema import schema

import argparse
from argparse import RawDescriptionHelpFormatter
from argparse import RawTextHelpFormatter


parser = argparse.ArgumentParser(
     formatter_class=RawDescriptionHelpFormatter,
     description=("""
    ---------------------------Shaclgen------------------------------------------
   
    Shaclgen takes either a data graph(s) or schema(s) as input and generates 
    a basic shape file based on the classes and properties present. 
    
    Shape files from data graphs:
    By default, the input graph is processed as a data graph (instance triples).
    Three formats are possible for data grapghs: simple, nested, and extended.
    
    Simple: Each class and property generate individual Node- and PropertyShapes        
    Nested: Property shapes will be nested in nodeshapes iif 
            they occur with one class.
    Extended: Expands nested shapes to create individual property shapes for each 
            property, in addition to nesting them when appropriate. 
        
    Shape files from ontologies:
    If the input is a schema or ontology (-o), shaclgen will generate 
    a nested shape file: properties with rdfs:domain defined in the ontology 
    will be nested within the appropriate NodeShape. rdfs:range definitions
    for XML and rdfs datatypes are included."""))
    
parser.add_argument("graph", nargs='+',type=str, help="The data graph(s).")

group = parser.add_mutually_exclusive_group()
group.add_argument("-nf", "--nested", action="store_true", help='generates a nested shape file')
group.add_argument("-ef", "--extended", action="store_true", help='generates an expanded shape file')
parser.add_argument("-o", "--ontology", action="store_true", help='input file(s) or URL(s) is a schema or ontology')
parser.add_argument("-s", "--serialization", help='result graph serialization, default is turtle')
parser.add_argument("-ns","--namespace", nargs='+',help="optional shape namespace declaration")


args = parser.parse_args()

import os
def main():
    print(os.listdir())
    if args.ontology:      
        g = schema(args.graph)
        kwargs = {'serial': 'turtle'}
        if args.serialization:
            kwargs['serial'] = args.serialization
        if args.namespace:
            kwargs['namespace'] = args.namespace
        g.gen_graph(**kwargs)
    else:
        kwargs = {'serial': 'turtle'}
        g = data_graph(args.graph)
        if args.nested:
            kwargs['graph_format'] = 'nf'
        elif args.extended:
            kwargs['graph_format'] = 'ef'
        if args.serialization:
            kwargs['serial'] = args.serialization
        if args.namespace:
            kwargs['namespace'] = args.namespace
        print('## shape file generated by SHACLGEN')
        g.gen_graph(**kwargs)
#        g.extract_contraints()


if __name__ == '__main__':
    main()

