# vts/vts_ws_client.py

import asyncio
import json
import websockets
from config import VTS_HOST, VTS_PORT, API_TOKEN

class VTSWebSocketClient:
    def __init__(self, uri: str, token: str):
        self.uri = uri
        self.token = token
        self.ws = None
        self.authenticated = False

    async def connect(self):
        if self.ws and not self.ws.closed and self.authenticated:
            return
        self.ws = await websockets.connect(self.uri)
        await self._authenticate()

    async def _authenticate(self):
        auth = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "messageType": "AuthenticationRequest",
            "requestID": "auth-request",
            "data": {
                "pluginName": "Rinna Control",
                "pluginDeveloper": "木村遙&Copilot",
                "authenticationToken": self.token
            }
        }
        await self.ws.send(json.dumps(auth))
        resp = json.loads(await self.ws.recv())
        self.authenticated = resp["data"].get("authenticated", False)
        if not self.authenticated:
            raise RuntimeError("VTS Authentication Failed")

    async def trigger_hotkey(self, hotkey_id: str):
        if not self.ws or self.ws.closed or not self.authenticated:
            await self.connect()
        payload = {
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "messageType": "HotkeyTriggerRequest",
            "requestID": f"hotkey-{hotkey_id}",
            "data": {"hotkeyID": hotkey_id}
        }
        await self.ws.send(json.dumps(payload))
        return await self.ws.recv()

    async def close(self):
        if self.ws:
            await self.ws.close()
            self.authenticated = False

# 同步介面
_client: VTSWebSocketClient = None

def init_vts(host=VTS_HOST, port=VTS_PORT, token=API_TOKEN):
    global _client
    uri = f"ws://{host}:{port}"
    _client = VTSWebSocketClient(uri, token)
    asyncio.get_event_loop().run_until_complete(_client.connect())

def trigger_expression(hotkey_id: str):
    if _client is None:
        raise RuntimeError("請先呼叫 init_vts() 建立連線")
    asyncio.get_event_loop().run_until_complete(
        _client.trigger_hotkey(hotkey_id)
    )

def close_vts():
    if _client:
        asyncio.get_event_loop().run_until_complete(_client.close())
