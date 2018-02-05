'''
Created on Jan 30, 2018

@author: extre_000
'''

from __future__ import print_function
from argparse import ArgumentParser, FileType
from email import message_from_file
import shutil
import os
import quopri
import base64
import re


__author__ = ["extreme45nm","Minh Dinh"]
__date__ = 20170130
__description__ = "Util to classify email by sender"


#const.current_path = os.getcwd()
pattern = r'[<]+\w+[>]'

def create_user_folder_by_address(header,path):
    for key,value in header:
        if( key == 'From'):
            print("value = ",value)
            value = value.replace("<","_")
            value = value.replace(">","_")
            value = value.replace("\"","_")
            value = value.replace("\"","_")
            value = value.replace("\\","_")
            value = value.replace("'","_")
            value = value.replace(",","_")
            value = value.replace("|","_")
            value = value.replace("?","_")
            folder_name = create_folder_if_not_exist(value, path)
            return folder_name
    

def get_eml_header(input_file):
    return message_from_file(input_file)._headers


def get_string_before_signal(string,signal):
    output = ""
    for character in string:
        if character != ':':
            output += character
        else:
            return output
        
    
def print_to_field_in_header(header):
    for key,value in header:
        if key == "To":
            print("{} : {} ".format(key,value))    
    
    
def get_list_of_eml_file(path):    
    list_of_file = os.listdir(path)
    for element in list_of_file:
        if os.path.isdir(path+element):
            list_of_file.remove(element)
    
    return list_of_file


def create_folder_if_not_exist(folder_name,path):
    try:
        if os.path.isdir(os.path.join(path,folder_name)):
            print("%s already exists"%folder_name)
        else:
            os.makedirs(os.path.join(path,folder_name))        
    except TypeError as type_error:
        print("ERR: ",type_error)
        return"ERROR"
    return folder_name  


def alert_none_type(anything):
    if anything is None:
        print("\n\nfvck, this shit is None %s \n\n"%anything)

def main(path):
   list_of_eml_files = get_list_of_eml_file(path)
   print(path)
   for eml_file in list_of_eml_files:
       if(eml_file[-1] != 'l'):     #skip created folder
           continue
       else:    
           eml_file_pointer = open(os.path.join(path,eml_file),"r")
           eml_header = get_eml_header(eml_file_pointer)
           folder_name = create_user_folder_by_address(eml_header, path)
           print("eml file : %s"%os.path.join(path,eml_file)) 
           #alert_none_type(eml_file)
           alert_none_type(folder_name) 
           shutil.copy(os.path.join(path,eml_file), os.path.join(path,folder_name))
           print(">> %s "%(folder_name))
             
   print("done!")

#handle the opening of the file (in case of running from IDE):
if __name__ == '__main__':
    parser = ArgumentParser(
            description = __description__,
            epilog = "Developed by {} on {}".format(", ".join(__author__),__date__)
        )
    parser.add_argument("path_to_eml_folder",help="original_msg")
    args = parser.parse_args()
    
    main(args.path_to_eml_folder)
