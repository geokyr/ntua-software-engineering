import argparse
import requests

my_parser = argparse.ArgumentParser(description='returns the amount of money op2_ID owes \
    to op1_ID in a specific period with ids and period provided in the params of the url')
my_parser.add_argument('--op1', metavar='operator_id', type=str, 
                        help='select the station operator')
my_parser.add_argument('--op2', metavar='operator_id', type=str, 
                        help='select the tag operator')
my_parser.add_argument('--datefrom', metavar='YYYYMMDD', type=str, 
                        help='select the starting date')
my_parser.add_argument('--dateto', metavar='YYYYMMDD', type=str, 
                        help='select the ending date')
my_parser.add_argument('--format', metavar='{json|csv}', type=str, 
                        help='select the format type of the output (json or csv)')
args = my_parser.parse_args()

url = 'http://127.0.0.1:9103/PassesCost/' + args.op1 + '/' + args.op2 + '/' + args.datefrom + '/' + args.dateto + '?format=' + args.format
r = requests.get(url)

try:    
    if args.format == 'json':
        print(r.json())
    elif args.format == 'csv': 
        print(r.text)
except Exception as e:
    print(e)