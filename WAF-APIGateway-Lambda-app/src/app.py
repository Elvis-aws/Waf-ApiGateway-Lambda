import json


def waf_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Your country is valid to call this service",
        }),
    }
