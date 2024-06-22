import argparse
import redis
import json

CHANNEL_NAME = 'monetary_transactions'

# Создаём парсер
parser = argparse.ArgumentParser()
parser.add_argument("-e", help="is a parameter receiving a list of bad guy account numbers", required=True)
args = parser.parse_args()

# Подключение к Редис
redis_client = redis.Redis(decode_responses=True)
pubsub = redis_client.pubsub()
pubsub.subscribe(CHANNEL_NAME)
message = pubsub.get_message()


def check_message(data: str, bad_guy_account_numbers: list[int]) -> json:
    data = json.loads(data)
    if data['amount'] > 0 and data['metadata']['to'] in bad_guy_account_numbers:
        data['metadata']['to'], data['metadata']['from'] = data['metadata']['from'], data['metadata']['to']
    return data


def main():
    while True:
        if (message := pubsub.get_message()) and message['type'] == 'message':
            print(check_message(message['data'], list(map(int, args.e.split(',')))))


def tests():
    bad_guy_account_numbers = [2222222222, 4444444444]
    example_1 = '{"metadata": {"from": 1111111111,"to": 2222222222},"amount": 10000}'
    answer_1 = {"metadata": {"from": 2222222222, "to": 1111111111}, "amount": 10000}
    example_2 = '{"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000}'
    answer_2 = {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000}
    example_3 = '{"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}'
    answer_3 = {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}

    assert check_message(example_1, bad_guy_account_numbers) == answer_1
    assert check_message(example_2, bad_guy_account_numbers) == answer_2
    assert check_message(example_3, bad_guy_account_numbers) == answer_3


if __name__ == '__main__':
    tests()
    main()
