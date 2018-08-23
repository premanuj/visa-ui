from sqlalchemy.sql import text
from app import dbsession
from flask import jsonify
from flask import json

def list_of_stations():
    sql = text('select * from visaui.station_list')
    data = dbsession.execute(sql).fetchall()
    # print(json.dumps(data))
    result = json.dumps([dict(r) for r in data])
    return result


def list_of_stations_procedure():
    sql = text('use [epg] EXEC [visaui].[get_headends]')
    data = dbsession.execute(sql).fetchall()
    return get_json(data)

def list_of_stations_name():
    sql = text('select * from visaui.station_list_name')
    data = dbsession.execute(sql).fetchall()
    return get_json(data)

def get_json(datas):
    result = json.dumps([dict(data) for data in datas])
    return result