# VTS_cle.py

import vts_websocket  # 假設你有封裝 VTS WebSocket 客戶端

# 🎭 封裝表情觸發函式
def trigger_expression(expression_id, debug=False):
    try:
        vts_websocket.trigger_expression(expression_id)
        if debug:
            print(f"✅ 已觸發 VTS 表情：{expression_id}")
    except Exception as e:
        print(f"❗ VTS 表情觸發失敗：{e}")
