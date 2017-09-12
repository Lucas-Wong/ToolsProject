#! /usr/bin/env python
# _*_coding:utf-8_*_
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7646921d135c6de8753fa8b91f141272"
# Your Auth Token from twilio.com/console
auth_token = "d41978ec25633b3129072bae9e37b206"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8613920160560",
    from_="+16193206920",
    body="Hello from Python!")

print(message.sid)
