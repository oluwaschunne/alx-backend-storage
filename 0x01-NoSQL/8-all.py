#!/usr/bin/env python3
"""0x01. NoSQL"""


def list_all(mongo_collection):
    """
    Prototype: def list_all(mongo_collection)
    Return an empty list if no document in the collection
    """
    cursor = mongo_collection.find()
    return cursor
