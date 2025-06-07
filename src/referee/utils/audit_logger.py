import json, time
from .signer import sign

def log_event(event_type: str, data: dict):
    entry = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'eventType': event_type,
        'actorId': 'referee',
        'payload': data
    }
    entry['signature'] = sign(entry)
    with open('storage/audit/audit_v1.jsonl','a') as f:
        f.write(json.dumps(entry) + "\n")
