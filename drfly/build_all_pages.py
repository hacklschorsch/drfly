#!/usr/bin/env python
# coding: utf-8

import sys
import os
import argparse

import build_page
import config
 

def build_all( source_directory ):
        
    cfg = config.config( source_directory )
    source_directory_realpath = os.path.realpath( source_directory )

    # iterate source directory and build all html and json files
    for dirName, subdirList, fileList in os.walk( source_directory_realpath , topdown=True ):

        ## exclude directories
        [subdirList.remove(d) for d in list(subdirList) if d in cfg['sourceexclude'] ]
        [subdirList.remove(d) for d in list(subdirList) if d in cfg['template'] ]

        for filename in fileList:
            sourcefile = os.path.realpath( os.path.join(dirName, filename) )
            build_page.build_html_json( sourcefile, source_directory )

if __name__ == "__main__":
    build_all( os.getcwd() )
