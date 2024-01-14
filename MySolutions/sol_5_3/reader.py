import csv
from typing import List, Iterable, Type, Dict, TypeVar
from sol_3_6.stock import Stock
from functools import partial

def csv_as_dicts(iterable: Iterable, types: List[TypeVar("T")], headers: List[str] = None) -> List[Dict[str, Type]]:
    make_row = partial(make_dict_with_types, types=types)
    return convert_csv(iterable, make_row, headers)


def csv_as_instances(iterable: Iterable, cls: Stock, headers: List[str]=None) -> List[Stock]:
    make_row = partial(make_instance, cls=cls)
    return convert_csv(iterable, make_row, headers)

def make_dict(headers, row):
    return dict(zip(headers, row))

def make_dict_with_types(headers, row, types):
    row = [func(val) for func, val in zip(types, row)]
    return dict(zip(headers, row))

def make_instance(headers, row, cls):
    return cls.from_row(row)

def convert_csv(iterable: Iterable, make_row, headers=None):
    rows = csv.reader(iterable)
    if headers is None:
        headers= next(rows)
    records = list(map(lambda row: make_row(headers, row), iterable))
    return records

def read_csv_as_dicts(filename: str, types: List[TypeVar("T")], headers: List[str] =None) -> List[Dict[str, Type]]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = csv_as_dicts(open(filename), types, headers)
    return records

def read_csv_as_instances(filename: str, cls: Stock, headers: List[str]=None) -> List[Stock]:
    '''
    Read CSV data into a list of instances
    '''
    records = csv_as_instances(open(filename), cls, headers)
    return records