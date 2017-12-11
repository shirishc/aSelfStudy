from twilio import rest

# Your account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3d640557104e57e5fee482f1a45a719b"
auth_token = "d4cc119d2b3c1750b50959a0e0cbbebe"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
			body = "My name is Lakhan",
			to = "+818021113754", 
			from_ = "+1-415-523-8607")

print (message.sid)
