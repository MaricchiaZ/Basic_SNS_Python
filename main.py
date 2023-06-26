import boto3
from botocore.exceptions import ClientError

def subscribe(topic, protocol, endpoint):
    sns_client = boto3.client('sns', verify=False, endpoint_url=(
        "http://localhost:4566"))

    try:
        subscription = sns_client.subscribe(
            TopicArn=topic, Protocol=protocol, Endpoint=endpoint,
            ReturnSubscriptionArn=True)
    except ClientError:
        print("Erro\n")
        raise
    return subscription


def list_topics():
    sns_client = boto3.client('sns', verify=False, endpoint_url=(
        "http://localhost:4566"))

    try:
        topic_iter = sns_client.list_topics()
    except ClientError:
        print("Error in list_topics\n")
        raise
    else:
        return topic_iter


def create_topic(name):  # tópico é um canal de comunicação (pode ser SMS, email...)
    sns_client = boto3.client('sns', verify=False, endpoint_url=(
        "http://localhost:4566"))

    try:
        topic = sns_client.create_topic(Name=name)

    except ClientError:
        print("Erro\n")
        raise
    else:
        return topic


if __name__ == '__main__':
    sns_client = boto3.client('sns', verify=False, endpoint_url=(
        "http://localhost:4566"))
    # topic = create_topic("teste2")
    # topics = list_topics()

    # for arn in topics['Topics']:
    #     print(arn['TopicArn'])

    response = subscribe("arn:aws:sns:us-east-1:000000000000:sub", "email", "gabrielmori16@gmail.com")
    sns_client.publish(TopicArn="arn:aws:sns:us-east-1:000000000000:sub",
        Message="message text",
        Subject="subject used in emails only")