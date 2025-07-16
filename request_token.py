import asyncio
import websockets
import json
import uuid

async def request_token():
    uri = "ws://localhost:8001"

    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",  # ✅ 指定 API 版本
        "messageType": "AuthenticationTokenRequest",
        "requestID": str(uuid.uuid4()),  # ✅ 加入唯一識別
        "data": {
            "pluginName": "Rin_VTS control",
            "pluginDeveloper": "木村遙&Copilot"
        }
    }

    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(payload))
        response = await websocket.recv()
        print("🗝️ VTS 回應：", response)

asyncio.run(request_token())
