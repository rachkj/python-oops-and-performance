servers=[
    {"id":"server-1", "cpu_usage": 85},
    {"id":"server-2","cpu_usage": 90},
    {"id":"server-3","cpu_usage": 60},
    {"id":"server-4","cpu_usage": 70},
    {"id":"server-5","cpu_usage": 80},
    {"id":"server-6","cpu_usage": 92},
    {"id":"server-7","cpu_usage": 97},
]

top_servers=sorted(servers, key=lambda x:x["cpu_usage"], reverse=True)[:5]
for server in top_servers:
    print(server["id"])