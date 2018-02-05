'''
Created on Jan 29, 2018

@author: extre_000

create an eml-parser that:
1. accept an arg for an EML file
2. read values from headers
3. parse info from each of the section
4. display this info in the console

'''
from __future__ import print_function
from argparse import ArgumentParser, FileType
from email import message_from_file
import os
import quopri
import base64

__author__ = ["extreme45nm","Minh Dinh"]
__date__ = 20170129
__description__="Util to parse text & attachment from EML files"


def process_payload(payload):
    print(payload.get_content_type() + "\n" + "=" * len(payload.get_content_type()))
    body = quopri.decodestring(payload.get_payload())   #decode body data
    
    if(payload.get_charset()):
        body = body.decode(payload.get_charset())
    else:
        try:
            body = body.decode()
        except UnicodeDecodeError:
            body = body.decode('cp1252')
    
    #check content type
    if payload.get_content_type() == "text/html":   #MIME
        outfile = os.path.basename(args.EML_FILE.name) + ".html"
        open(outfile,'w').write(body)
    #if not MIME, then print the body
    elif payload.get_content_type().startswith('application'):
        outfile = open(payload.get_filename(),'wb')
        body = base64.b64decode(payload.get_payload())
        outfile.write(body)
        outfile.close()
        print("Exported: {}\n".format(outfile.name))
    else:
        print(body)        


#read File object into the email lib
def main(input_file):
    emlfile = message_from_file(input_file)
    
    #start w/ the headers
    print("\nHeader:\n")
    for key,value in emlfile._headers:
        #if(key == 'Received'):
            print("{} : {} ".format(key,value))
        #else:
        #    print("{}---".format(key))
        
    #read payload
    print("\nBodee\n")
    if emlfile.is_multipart():
        for part in emlfile.get_payload():
            process_payload(part)
    else:
        process_payload(emlfile[1])


#handle the opening of the file s
if __name__ == '__main__':
    parser = ArgumentParser(
            description=__description__,
            epilog = "Developed by {} on {}".format(", ".join(__author__),__date__)
        )
    parser.add_argument("EML_FILE",help="",type = FileType('r'))
    args = parser.parse_args()
    
    main(args.EML_FILE)