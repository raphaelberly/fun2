
import argparse
import logging

from zoho.lib import ZohoWrapper

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


if __name__ == '__main__':

    object_list = ['invoices', 'expenses', 'creditnotes', 'creditnotes/refunds']

    # Create argument parser
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--object', required=True, type=str, choices=object_list, help='Object to be queried from API')
    parser.add_argument('--spreadsheet_id', required=True, type=str, help='ID of the Google spreadsheet to use')
    parser.add_argument('--config_folder', default='config', type=str, help='Path to the config folder')
    parser.add_argument('--secret_json', default='client_secret.json', type=str, help='Path to client_secret.json file')

    # Parse arguments
    args = parser.parse_args()

    LOGGER.info('Starting ETL process.')
    zoho = ZohoWrapper(args.config_folder, args.secret_json)
    response = zoho.extract(args.object)
    zoho.transform(args.object, response)
    zoho.load(args.spreadsheet_id)
    LOGGER.info('Done.')
