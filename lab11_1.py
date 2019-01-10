#!/usr/bin/env pyhton3
#-*- codding: utf-8 -*-

def open_function ( file: str) -> int:
    """This function open file and find size """
    f = open(file, 'rt')
    for line in f:
        size = line.split()[9]
        yield int(size)

def output_function(bytes: list) -> int:
    """This function output size nginx"""
    byte_size = 0
    for byte in bytes:
        byte_size += byte
    print(byte_size)

output_function(open_function("2017_05_07_nginx.txt"))
