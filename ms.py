# Predict Covid-19 Status Program

#Input Age Of Patients
print("WELCOME TO COVID-19 PREDICTION SOFTWARE")
age=int(input("Please Enter Your Age "))
print("Please Enter y(Yes) or n(No) for Following Symptoms :")

#Serious Symptoms
Chest_pain=input("Do you have any kind of chest pain or pressure ? ")
breathing_problem=input("Do you have any problem in breathing ? ")
loss_speech=input("Do you have problem in speaking and movement ? ")

#Less Common Symptoms
headache=input("Do you have any kind of headache ? ")
taste_loss=input("Are you unable to taste or smell things ? ")
Rash_skin=input("Do you have any rash on skin , or discoloration of finger or toes ? " )
Aches_pain=input("Do you have any kind of aches and pains ? ")
sore_throat=input("Do you have sore throat ? ")

#Give result
if(age) and ((Chest_pain=='y') or (breathing_problem=='y') or (loss_speech=='y')):
	print('Kindly Go To Your Doctor , You can have Covid-19 according to your symptoms')
elif(age>60) and ((headache=='y') or (taste_loss=='y') or (Rash_skin=='y') or (Aches_pain=='y') or (sore_throat=='y')):
	print('There are less chances but you should Go to Doctor once according to your symptoms')
elif(age<60) and ((headache=='y') or (taste_loss=='y') or (Rash_skin=='y') or (Aches_pain=='y') or (sore_throat=='y')):
	print('It will be good if you Go for 14 days Home Quarantine')
else:
	print('You are completely healthy !!! ')

print('STAY HOME STAY SAFE')


