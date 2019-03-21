import json
import logging
import sys
import pika

RABBIT_URL = f'amqp://localhost:5672'
EXCHANGE = 'ingest.bundle.exchange'
QUEUE = 'ingest.bundle.assay.create'
FILE_PATH = 'tm-failed-messages-20190321.json'

# TODO Parameterise rabbit details and filename

if __name__ == '__main__':
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=format, stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger(__name__)

    if not RABBIT_URL:
        raise Exception("No rabbit")

    connection = pika.BlockingConnection(pika.URLParameters(RABBIT_URL))
    channel = connection.channel()

    logger.info(f'connecting to {RABBIT_URL}')

    with open(FILE_PATH, encoding='utf-8') as data_file:
        messages = json.loads(data_file.read())

    ctr = 0
    for message in messages:
        logger.warning(f'Sending message: {json.dumps(message)}')
        channel.basic_publish(exchange='', routing_key=QUEUE, body=json.dumps(message))
        ctr = ctr + 1

    logger.warning(f'Total no of sent messages: {ctr}')
    connection.close()
