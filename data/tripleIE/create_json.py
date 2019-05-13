import json
import random
import string

data = []

with open('normalize.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_st = line.strip().split('\t')
        str = line_st[0] + '\t' + line_st[1]
        data.append({
            "paragraphs": [{
                "context": line_st[0] + '\t' + line_st[1],
                "qas": [{
                    "question": line_st[0],
                    "id": ''.join(random.sample(string.ascii_letters + string.digits, 32)),
                    "answers": [{
                        "answer_start": len(line_st[0]) + 1,
                        "text": line_st[1]
                    }]
                }],
            }]
        })

with open("train-v1.1.json", "w", encoding='utf-8') as f:
    json.dump({'data': data, 'version': '1.1'}, f, ensure_ascii=False)
