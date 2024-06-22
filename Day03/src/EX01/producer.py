import json
import logging
import redis
from time import sleep
from datetime import datetime
from random import randint
from sys import stdout

CHANNEL_NAME = 'monetary_transactions'

# Создание логгера
datetime_format = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logging.basicConfig(datefmt=datetime_format,
                    stream=stdout,
                    level=logging.INFO,
                    format='[%(asctime)s][%(funcName)-14s][%(levelname)s] %(message)s')


def main():
    # Создание объекта Redis
    redis_client = redis.Redis(decode_responses=True)
    logger.info('Started\n\n')
    while True:
        logger.info('Start creating message')
        created_message = create_message(*generate_data())
        logger.info(f'Created json message{created_message}')
        redis_client.publish(CHANNEL_NAME, created_message)
        logger.info('Publish message\n')

        sleep(1)
    logger.info('Finished')


def generate_data() -> tuple[int, int, int]:
    logger.info('Start generating data')
    account_from = randint(1000000000, 9999999999)
    logger.info(f'The account from which the money is to be sent: {account_from}')
    while (account_to := randint(1000000000, 9999999999)) == account_from:
        account_to = randint(1000000000, 9999999999)
    logger.info(f'The account where the money is to be sent: {account_to}')
    amount = randint(-10000, 10000)
    logger.info(f'transfer amount: {amount}')
    logger.info('Stop generating data')
    return account_from, account_to, amount


def create_message(account_from, account_to, amount):
    message = {
        "metadata": {
            "from": account_from,
            "to": account_to
        },
        "amount": amount
    }

    json_msg = json.dumps(message)
    return json_msg


def tests():
    # test creating message
    answer_1 = '{"metadata": {"from": 6239586773, "to": 7615690735}, "amount": 1000}'
    answer_2 = '{"metadata": {"from": 6239586773, "to": 7615690735}, "amount": -1000}'
    assert create_message(6239586773, 7615690735, 1000) == answer_1
    assert create_message(6239586773, 7615690735, -1000) == answer_2


if __name__ == '__main__':
    tests()
    main()
