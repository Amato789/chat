from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Kafka Chat',
        docs_url='/api/docs',
        description='FastAPI + Kafka + Websockets + DDD example',
    )
