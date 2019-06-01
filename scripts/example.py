import scripts.other_module as om
from h3 import h3

om.get_me()

translate_statistic = {'Med': 'Median', 'Mean': 'Mean'}
translate_pollutant = {'BC': 'BC', 'NO': 'NO', 'NO2': r'NO$_2$'}
concentration_labels = {
    'BC': r'$\mu$g m$^{-3}$',
    'NO': r'ppb',
    r'NO$_2$': r'ppb'
}

def to_geojson(df, h3_address='h3_address'):
    
    swipe = lambda x: [x[1], x[0]]

    df['h3_bound'] = df[h3_address].apply(h3.h3_to_geo_boundary)
    df['h3_bound'] = df['h3_bound'].apply(lambda x: list(map(swipe, x)))
    df['h3_bound'] = df['h3_bound'].apply(lambda x: [x + [x[0]]])
    
    geojson = {'features': [],
           'type': 'FeatureCollection'}
    
    feature = {'geometry': 
           {'coordinates': None,
            'type': 'Polygon'},
           'properties': {'id': None},
           'type': 'Feature'}
    
    for i, row in enumerate(df['ready']):
    
        _feature = deepcopy(feature)

        _feature['geometry']['coordinates'] = row
        _feature['properties']['id'] = str(i)

        geojson['features'].append(_feature)
    
    return geojson