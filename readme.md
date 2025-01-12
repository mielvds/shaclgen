SHACLGEN
========

Shaclgen takes either a instance graph(s) or schema(s) as input and
generates a basic shape file based on the classes and properties
present.

**Shape files from instance data:** By default, the input graph is
processed as a instance triples. 

**Shape files from ontologies:** If the input is a schema or ontology,
shaclgen generates a nested shape file: properties with rdfs:domain
defined in the ontology will be nested within the appropriate NodeShape.
rdfs:range definitions for XML and rdfs datatypes are included.

       
        
Added support for OWL constructions is planned.


 
    
    

* * * * *

Installation
------------

Using pip: :

    pip install shaclgen


Command line use:
-----------------

    $ shaclgen [graph] [optional arguments]

Example usage: :

    $ shaclgen https://www.lib.washington.edu/static/public/cams/data/datasets/uwSemWebParts/webResource-1-0-0.nt 

Command line arguments: :

    positional arguments:
    graph                 The data graph(s).

    optional arguments:
    -h, --help            show this help message and exit
    -o, --ontology        input file(s) or URL(s) is a schema or ontology
    -ns, --namespace      optional shape namespace declaration. ex: http://www.example.com exam
    -i, --implicit        use implicit class targets with RDFS
    -s SERIALIZATION, --serialization SERIALIZATION
                          result graph serialization, default is turtle. example:. -s nt

Serialization options:
        turtle = turtle
        ntriples = nt
        rdfxml = xml
        n3 = n3

Namespace Example usage: :

    $ shaclgen https://www.lib.washington.edu/static/public/cams/data/datasets/uwSemWebParts/webResource-1-0-0.nt -s nt

        
Namespace argument:
    The namespace argument is takes a full URL and prefix.

Namespace Example usage: :

    $ shaclgen https://www.lib.washington.edu/static/public/cams/data/datasets/uwSemWebParts/webResource-1-0-0.nt -ns http://www.example.org uwlib

Implicit class usage :

SHACL interprets shapes typed as `rdfs:Class` as the target class of that shape. This is called [Implicit Class Targets](https://www.w3.org/TR/shacl/#implicit-targetClass). 
By setting `-i` or `--implicit`, shaclgen will reuse the class definitions in the ontology (ie. instances of `rdfs:Class` or `owl:Class`) as shapes and not create new URIs.
Instances of `owl:Class` will be typed as `rdfs:Class` in the output.
Triples that tie the class to one of its parent classes with `rdfs:subclassOf` will be copied by default.

Example ontology input:

    ex:Person a owl:Class.

Example output without `-i`:

    ex:PersonShape a sh:NodeShape;
        sh:targetClass ex:Person .

Example output with `-i`:

    ex:Person a rdfs:Class; sh:NodeShape.


* * * * *

This project is still in development. Comments, questions, and issues
are welcome!

Contact alexiskeelie at gmail.com
