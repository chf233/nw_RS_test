from reedsolo import RSCodec

rsc = RSCodec(10)
e = rsc.encode(b'hello world')
print(e)
try:
    ans1 = rsc.decode(b'hello world\xed%T\xc4\xfd\xfd\x89\xf3\xa8\xaa')[0] #0 error
    print("0 error correction:", ans1)
except:
    print('Too much error')

try:
    ans2 = rsc.decode(b'heXlo worXd\xed%T\xc4\xfdX\x89\xf3\xa8\xaa')[0] #3 error
    print("3 error correction:", ans2)
except:
    print('Too much error')

try:
    ans3 = rsc.decode(b'hXXXo worXd\xed%T\xc4\xfdX\x89\xf3\xa8\xaa')[0] #5 error
    print("5 error correction:", ans3)
except:
    print('Too much error')

try:
    ans4 = rsc.decode(b'hXXXo worXd\xed%T\xc4\xfdXX\xf3\xa8\xaa')[0] #6 error
    print("6 error correction:", ans4)
except:
    print('Too much error: 6')

