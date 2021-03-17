import time
import hmac
import hashlib

expire_time = 30
code_len = 6
secret = b"dolphin?!"


def get_HOTP(K, C):
    hmac_res = hmac.new(K, str(C).encode(), hashlib.sha1).hexdigest()
    offset = int(hmac_res[39], 16) * 2
    code_raw = int(hmac_res[offset: offset + 8], 16)
    code_trunc = str(code_raw)[len(str(code_raw)) - code_len:]
    return code_trunc


while 1:
    u_time = int(time.time())
    ct = int(u_time / expire_time)
    expires = expire_time - (u_time % expire_time)
    hotp = get_HOTP(secret, ct)

    print(expires, hotp)
    time.sleep(1)