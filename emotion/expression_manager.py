# expression_manager.py

expression_map = {
    "粉髮": ["頭髮, 髮色"],
    "遊戲機": ["遊戲, 電玩, 玩遊戲, 打電動, 電動"],
    "比心": ["喜歡你, 愛心"],
    "比耶": ["耶, 好耶, 太棒了"],
    "話筒": ["唱, 唱歌, 歌唱"],
    "飛吻": ["親親, 飛吻, 吻"],
    "5星星眼": ["星星眼, 眼冒金星"],
    "5流淚": ["哭哭, 哭了"],
    "5愛心眼": ["愛你"],
    "5臉紅": ["害羞, 臉紅"],
    "5臉黑":["臉黑, 鄙視"],
    "clean": ["正常"],
    "生氣": ["生氣, 生氣氣, 氣死我了"],
    "5棒棒糖": ["棒棒糖, 吃糖"],
    "5流汗": ["好喔, ..."],

}

def match_expression(text):
    for emotion, keywords in expression_map.items():  # ✅ 改成 expression_map
        if any(word in text for word in keywords):
            return emotion
    return None
