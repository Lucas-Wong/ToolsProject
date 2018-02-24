# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-02-24 
"""
import uuid

# make a UUID based on the host ID and current time
print("uuid1".center(50, "*"))
print(uuid.uuid1())

# make a UUID using an MD5 hash of a namespace UUID and a name
print("uuid3".center(50, "*"))
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'ariix.com'))

# make a random UUID
print("uuid4".center(50, "*"))
print(uuid.uuid4())

# make a UUID using a SHA-1 hash of a namespace UUID and a name
print("uuid5".center(50, "*"))
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'ariix.com'))

if __name__ == '__main__':
    pass