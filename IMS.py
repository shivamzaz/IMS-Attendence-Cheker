#!/usr/bin/python
import urllib2
import re
import subprocess 
Rollno="1314310838"#raw_input("Enter Roll No: ")
Branch="2cs"#raw_input("Enter Branch: ")
Year="4"#raw_input("Enter Subyear: ")
#http://118.102.164.133/cull2016odd_webshow.jsp?roll=1314310012&subbranch=CS1&subyear=4&att=Theory&batch=All
#u="http://118.102.164.133/cull2016odd_webshow.jsp?roll=1314310838&subbranch=2CS&subyear=4&att=Theory&batch=All"
u="http://118.102.164.133/cull2016odd_webshow.jsp?roll="+Rollno+"&subbranch="+Branch.upper()+"&subyear="+Year+"&att=Theory&batch=All"
feh = urllib2.urlopen(u).read()
f=re.findall(r'(?<!\-)\b(\d\d\d|\d\d|\d)\b', feh)
#print f
d={}
d[0]="Aptitude" 	
d[1]="Distributed Systems" 	
d[2]="Artificial Intelligence" 	
d[3]="Software Project Management" 	
d[4]="OPEN ELECTIVE -I COMPUTER VISION" 	
d[5]="Cryptography & Network Security" 	
d[6]="Distributed Systems Lab" 	
d[7]="Project Lab" 	
d[8]="Industrial Training Viva" 	
l=[]
	#l.append((f[-10],f[-9])
try:
		for i in range(17,51,4):
			if(i%2==0):
				pass
			else:
				l.append((f[i],f[i+1]))
		#print l
		k=0
		def sendmessage(message):
				subprocess.Popen(['notify-send', message])
				return
		print "                                      "
		for i in l:
			print "{} => {}/{}".format(d[k],i[0],i[1])
			k+=1
		xx="Improve Your Attendence"
		if(int(f[-6])<75):
			xx=xx+" that's only:  "+f[-6] +"%"
			sendmessage(xx);
		else:
			xx="Hey! Attendence: "+f[-6]+'%'
			sendmessage(xx)
		print("--------------------------------------")
		print("                                      ")
		print "Total Attendence is: {}%".format(f[-6])	
		print "total lectures {}/{}".format(f[-8],f[-7])
		print("                                      ")
		print("--------------------------------------")
except:
		print("--------------------------------------")
		print("                                      ")	
		print "Unable to Help !! Sorry for Inconvience :("
		print("                                      ")
		print("--------------------------------------")
'''class DeviseCreateEnters < ActiveRecord::Migration
	def change
		create_table :enters do |t|
			## Database authenticatable
			t.string :name
			t.string :email,              null: false, default: ""
			t.string :encrypted_password, null: false, default: ""

			## Recoverable
			t.string   :reset_password_token
			t.datetime :reset_password_sent_at

			## Rememberable
			t.datetime :remember_created_at

			## Trackable
			t.integer  :sign_in_count, default: 0, null: false
			t.datetime :current_sign_in_at
			t.datetime :last_sign_in_at
			t.string   :current_sign_in_ip
			t.string   :last_sign_in_ip

			## Confirmable
			# t.string   :confirmation_token
			# t.datetime :confirmed_at
			# t.datetime :confirmation_sent_at
			# t.string   :unconfirmed_email # Only if using reconfirmable

			## Lockable
			# t.integer  :failed_attempts, default: 0, null: false # Only if lock strategy is :failed_attempts
			# t.string   :unlock_token # Only if unlock strategy is :email or :both
			# t.datetime :locked_at


			t.timestamps null: false
		end

		add_index :enters, :email,                unique: true
		add_index :enters, :reset_password_token, unique: true
		# add_index :enters, :confirmation_token,   unique: true
		# add_index :enters, :unlock_token,         unique: true
	end
end
'''



