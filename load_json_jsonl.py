def load_jsonl(path):
    infos = []
    with open(path, mode="r", encoding="utf-8") as f:
        for line in f:
            infos.append(json.loads(line))
    return infos

def load_json(path):
    with open(path, mode='r', encoding='utf-8') as f:
        json_dict = json.load(f)
        f.close()
    return json_dict
