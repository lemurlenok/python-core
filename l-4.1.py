#3
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},
    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},
    ]
]

res = []
indices = [0] * len(data)

while any(index < len(sublist) for index, sublist in zip(indices, data)):
    for i, sublist in enumerate(data):
        if indices[i] < len(sublist):
            item_id = sublist[indices[i]]["id"]
            if item_id not in res:
                res.append(item_id)
            indices[i] += 1

print(res)