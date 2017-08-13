# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def hashing_func(hash_key):
    # Create hashing function which generates index values from
    # hash_key modulo 10 remainder
    return hash_key%10
    
def hash_insert(table, hash_key, value):
    table[hashing_func(hash_key)].append(value)
    
def hash_search(table, hash_key):
    return table[hashing_func(hash_key)]
    
def hash_delete(table, hash_key):
    delete_list = []
    table[hashing_func(hash_key)] = delete_list
    
table = [[] for _ in range(0,10)]

hash_insert(table,24,'money')

hash_insert(table,35,'cash')

hash_insert(table,20,'credit')

hash_insert(table,30, 'invoice')
print table  

print hash_search(table,24)

hash_delete(table, 24)

print table