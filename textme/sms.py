from twilio.rest import Client 


account_sid = '[account_sid]' 
auth_token = '[auth_token]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
    from_='[phone_number_from]',    
    body='I cant believe this works!!!!!',    
    to='[phone_number_to]' 
) 

print(message.sid)