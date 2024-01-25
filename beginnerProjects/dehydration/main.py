# prompt list
welcome_prompt="Welcome! What would you like to do today?\n -To make a new diagnosis press 1\n -To list previous patients and diagnosis press 2 \n -To quit press Q\n"
name_prompt= "What is the patient's name?\n"
age_prompt= "How old is the patient?\n"
diagnosis_appearance_prompt= "How is the patient's general appearance?\n -Press 1 :Normal appearance and energy \n -Press 2: Irritable or lethargic\n"
eye_test_prompt="How are the patient's eyes?\n -Press 1 :Normal appearance or very slightly sunken \n -Press 2: Eyes are very sunken \n"
skin_test_prompt="How is the elacity in the patient's skin?(perform a skin pinch)\n -Press 1 :Normal elasticity(skin returns to normal imediately)  \n -Press 2:Bad elasticity(skin is very slow returning to normal) \n"
severe_dehydration="Patient is severely dehydrated. Medical help is advised"
light_dehydration="Patient has some symptoms of light dehydration"
no_dehydration="Patient suffers no signs of dehydration"
error_22="Invalid Key Input or Prompt"

# list
diagnoses_list= [

]

# functions
def patient_list():
    for patient in diagnoses_list:
        print(patient)

def save_patient(name,age,diagnosis):
    if not (isinstance(name, str) and name.strip()) or not (isinstance(age, str) and age.strip()) or not (isinstance(diagnosis, str) and diagnosis.strip()):
        print ("Could Not Save:Invalid or Corrupt Data")
        return 
    else:
        patient_info= "Name:" + name  + "\n Age:" + age + "\n Diagnosis:" + diagnosis
        diagnoses_list.append(patient_info)
        print ("final diagnosis:",patient_info )

def skin_test(skin):
    if skin == "1":
        return light_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        print(error_22)
        return ""

def eye_test(eyes):
    if  eyes =="1":
        return no_dehydration
    elif eyes =="2":
        return severe_dehydration
    else:
        print(error_22)
        return ""

def appearance_test():
    appearance = input(diagnosis_appearance_prompt)
    if appearance =="1":
        eyes = input(eye_test_prompt)
        return eye_test(eyes)
    elif appearance =="2":
        skin = input(skin_test_prompt)
        return skin_test(skin)
    else:
        print(error_22)
        return

def start_diagnosis():
    name = input(name_prompt)
    age = input(age_prompt)
    diagnosis= appearance_test()
    save_patient(name,age,diagnosis)


def welcome():
    while(True):
        selection=input(welcome_prompt)
        if selection =="1":
            start_diagnosis()
        elif selection=="2":
            patient_list()
        elif selection=="q":
            print("See you later!")
            return
        else:
            print(error_22)

# run
welcome()


# tests
def TEST_skin_test ():
    print (skin_test("1") ==light_dehydration)
    print (skin_test("2") == severe_dehydration)
    print (skin_test("!!TESTTT!!") == "")

def TEST_eye_test():
    print (eye_test("1")== no_dehydration)
    print (eye_test("2")== severe_dehydration)
    print (eye_test("3") == "")

# TEST_eye_test()
# TEST_skin_test()