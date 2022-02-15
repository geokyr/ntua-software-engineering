import argparse
import requests

my_parser = argparse.ArgumentParser(description='checks if there is connection with database')
my_parser.add_argument('--format', metavar='{json|csv}', type=str, 
                        help='select the format type of the output (json or csv)')
args = my_parser.parse_args()

r = requests.get('http://127.0.0.1:9103/admin/healthcheck')

try:    
    if args.format == 'json':
        print(r.json())
    elif args.format == 'csv': 
        print(r.text)
except Exception as e:
    print(e)