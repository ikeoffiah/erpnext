import json
from django.core.exceptions import ValidationError

def _(text, *args, **kwargs):
    """Translation stub"""
    return text

def throw(msg, exc=ValidationError):
    """Exception throwing stub"""
    raise exc(msg)

def get_doc(doctype, name=None):
    """Doc retrieval stub"""
    return None

def get_all(doctype, filters=None, fields=None):
    """List retrieval stub"""
    return []

# Common ERPNext root utilities
def get_default_company(): pass
def get_company_currency(company): pass
