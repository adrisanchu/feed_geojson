import os
import json
import csv
from helper_functions import *


def run_feeder():
    print('Grab geoJSON file and load as dict...')
    geojson_filename = 'custom.geo.json'
    geojson = get_json(name=geojson_filename)

    print('Read csv files...')
    csv_filename = 'dummy_data.csv'
    csv_data = get_csv(name=csv_filename)

    print('Loop through each field in geoJSON...')
    features = geojson['features']
    # features is a list of dicts, we loop through it
    for feature in features:
        name = feature['properties']['sovereignt']
        print('Working in {0}...'.format(name))
        # find country in data from csv
        val = find_value_by_key(list_of_dicts=csv_data, find=name, default='null')
        # add new field to geoJSON
        feature['properties']['dummy_data'] = val

    print('-----------------')
    print('Dumping geoJSON into folder...')
    # generate new geoJSON with dummy data
    out_folder = os.path.join(get_route(), 'result')
    to_json(data=geojson, folder=out_folder, name='new_json.json')
    print('Done!')


if __name__ == '__main__':
    run_feeder()
