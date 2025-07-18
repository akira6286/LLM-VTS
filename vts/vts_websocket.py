import config.json

# 🌐 WebSocket 設定
VTS_URI = "ws://localhost:8001"

# 🗝️ API Token（你從 VTS 授權視窗取得的長串密鑰）
#API_TOKEN = "你的API Token"
API_TOKEN = "1ba1f727964867318bf04635a099f6d73364dea9dfea432eff6575495fb095d8"

# 🔐 認證流程
async def authenticate(websocket):
    auth_payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": "1.0",
        "messageType": "AuthenticationRequest",
        "requestID": "auth-request",
        "data": {
            "pluginName": "Rin_VTS control",
            "pluginDeveloper": "木村遙&Copilot",
            "authenticationToken": API_TOKEN
        }
    }

    await websocket.send(json.dumps(auth_payload))
    response = await websocket.recv()
    data = json.loads(response)

    if not data["data"]["authenticated"]:
        print("❌ 認證失敗：請確認 API Token 是否正確")
        return False

    print("✅ 認證成功：凜奈已辨識你的身份")
    return True

# 🎭 表情觸發函式
async def _trigger_expression(expression_id):
    try:
        async with websockets.connect(VTS_URI) as websocket:
            # 認證流程
            if not await authenticate(websocket):
                return

            # 傳送表情指令
            expression_payload = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "messageType": "HotkeyTriggerRequest",
                "requestID": "expr-trigger",
                "data": {
                    "hotkeyID": expression_id
                }
            }

            await websocket.send(json.dumps(expression_payload))
            response = await websocket.recv()
            print("🎭 VTS 回應：", response)

    except Exception as e:
        print("❗錯誤發生：", e)

# 🧩 對外調用接口
def trigger_expression(expression_id: str):
    asyncio.run(_trigger_expression(expression_id))
