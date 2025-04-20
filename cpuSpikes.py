from datetime import datetime
from typing import List, Tuple
def detect_cpu_spikes(data:List[Tuple[datetime,float]]):
    spikes=[]
    for i in range(len(data)-2):
        if data[i][1]>90 and data[i+1][1]>90 and data[i+2][1]>90:
            spikes.append(i)
    return spikes


data=[
    (datetime(2025,4,14,14,0),85.0),
    (datetime(2025,4,14,14,1),92.0),
    (datetime(2025,4,14,14,2),93.0),
    (datetime(2025,4,14,14,3),91.0),
    (datetime(2025,4,14,14,4),88.0)
]
print(detect_cpu_spikes(data))