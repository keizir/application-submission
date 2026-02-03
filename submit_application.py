import json
import hmac
import hashlib
import urllib.request
from datetime import datetime, timezone

URL = "https://b12.io/apply/submission"
SIGNING_SECRET = b"hello-there-from-b12"

payload = {
    "timestamp": "2026-01-06T16:59:37.571Z",
    "name": "Eugene Lynch",
    "email": "eugeneban18@gmail.com",
    "resume_link": "https://drive.google.com/file/d/1vmjzzci2tiwVxWU_0B3TcGABthThWHPQ/view",
    "repository_link": "https://github.com/keizir/application-submission",
    "action_run_link": "https://github.com/keizir/application-submission/actions/runs/21628121625",
}

body = json.dumps(
    payload,
    separators=(",", ":"),
    sort_keys=True
).encode("utf-8")

signature = hmac.new(
    SIGNING_SECRET,
    body,
    hashlib.sha256
).hexdigest()

request = urllib.request.Request(
    URL,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={signature}",
    },
    method="POST",
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result["receipt"])
