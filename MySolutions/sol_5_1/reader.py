import csv
from typing import List, Iterable, Type, Dict, TypeVar
from sol_3_6.stock import Stock

def csv_as_dicts(iterable: Iterable, types: List[TypeVar["T"]], headers: List[str] = None) -> List[Dict[str, Type]]:
    if headers is None:
        headers= next(iterable)
        if isinstance(headers, bytes):
            headers = headers.decode("utf-8")
        headers = headers.strip("\n").split(",")
    records = []
    for row in iterable:
        if isinstance(row, bytes):
            row = row.decode("utf-8")
        row = row.strip("\n").split(",")
        record = { name: func(val) 
                    for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records


def csv_as_instances(iterable: Iterable, cls: Stock, headers: List[str]=None) -> List[Stock]:
    if headers is None:
        headers= next(iterable)
    records = []
    for row in iterable:
        if isinstance(row, bytes):
            row = row.decode("utf-8")
        row = row.strip("\n").split(",")
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str, types: List[TypeVar["T"]], headers: List[str] =None) -> List[Dict[str, Type]]:
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