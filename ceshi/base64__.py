import base64, hashlib

# hashlib.sha1(vj.encode()).digest()
aa='{"start":"0","end":"10","appId":"","sourceId":"8414f103052842d6ab59f57d93ca4b61","illegUnit":"","LeaderApproTime_start":"","LeaderApproTime_end":"","sort":"LeaderApproTime desc"}'
key = base64.b64encode(aa.encode())
print(key)
