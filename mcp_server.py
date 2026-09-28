import sys
import json
from client import ReflexionEpisodicEvaluator

reflex = ReflexionEpisodicEvaluator()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "reflexion_memory",
                        "description": "Record episode trajectory with critique or query accumulated reflective guidance",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "action": {"type": "string", "enum": ["record", "get_advice"]},
                                "trajectory": {"type": "array", "items": {"type": "string"}},
                                "critique": {"type": "string"},
                                "score": {"type": "number"}
                            },
                            "required": ["action"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "reflexion_memory":
            act = args["action"]
            if act == "record":
                traj = args.get("trajectory", [])
                crit = args.get("critique", "")
                sc = args.get("score", 0.0)
                reflex.record_episode(traj, crit, sc)
                return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"status": "RECORDED", "total_episodes": len(reflex.memory)})}]}}
            elif act == "get_advice":
                adv = reflex.get_context_advice()
                return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"advice": adv})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
