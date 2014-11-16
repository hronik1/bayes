import xmltodict
import requests

ZWS_ID = "X1-ZWz1b1kf436ia3_2xcn2"
CITY_STATE = "High Point, NC"
REQUEST_URL = "http://www.zillow.com/webservice/GetDeepSearchResults.htm"

def fetch_from_address(address):
    payload = {
        "zws-id": ZWS_ID,
        "address": address,
        "citystatezip": CITY_STATE
    }
    response = requests.post(REQUEST_URL, params=payload)
    to_write = address
    if response.ok:
        try:
            response_dict = xmltodict.parse(response.content)
            results = response_dict.get('SearchResults:searchresults', {}).get('response', {}).get('results', {})
            if isinstance(results, list):
                result = restults[0]
            else:
                result = results.get('result', {})
            if isinstance(result, list):
                result = result[0]
            # result = response_dict.get('SearchResults:searchresults', {}).get('response', {}).get('results', {}).get('result', {})
            to_write += ', ' + result.get('address',{}).get('zipcode', '')
            to_write += ', ' + result.get('useCode', '')
            to_write += ', ' + result.get('yearBuilt', '')
            to_write += ', ' + result.get('lotSizeSqFt', '')
            to_write += ', ' + result.get('finishedSqFt', '')
            to_write += ', ' + result.get('zestimate', {}).get('amount', {}).get("#text", '')
        except Exception as e:
            print address
            print to_write
            print e
            to_write += ',,,,,,'
    else:
        print address + ' fail'
        to_write += ',,,,,,'

    return to_write

def write_address_data(address_file, out_file='../data/fetched_housing_data.csv'):
    with open(address_file, 'r') as addresses:
        with open(out_file, 'a') as o:
            for address in addresses:
                address = address.rstrip('\n')
                fetched = fetch_from_address(address)
                if fetched:
                    o.write(fetched + '\n')