import requests

def trigger_expression(expression_name):
    url = "http://localhost:4455"  # OBS WebSocket 連接埠
    payload = {
        "request-type": "SetSceneItemRender",
        "source": expression_name,
        "render": True,
        "message-id": "trigger-" + expression_name
    }
    requests.post(url, json=payload)
