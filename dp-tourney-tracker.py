# Welcome
from sympy import false


print("Welcome to Tournaments R Us")
print("============================")

# Ask for number of participants; initialize participant dictionary
num_part = input("Enter the number of participants: ")
print("There are 57 participant slots ready for sing-ups.")
dict_part = {}

#Master Loop start
end_condition = False
while end_condition == False:
    print('Participant Menu \n================ \n1. Sign Up \n2. Cancel Sign Up \n3. View Participants\n4. Save Changes\n5. Exit')
    main_menu_input = str(input("What is thy bidding my master?")).lower()
    if main_menu_input in ['1', '1.', '1. sign up', 'sign up']:
        #Sign Up code
        #Get entries first
        print('Participant Sign Up\n===================\n')
        part_name = str(input('Participant Name: '))
        slot_entry = input('Desired starting slot #[1-' + str(num_part) + "]: ")
        
        # Check validity of slot_entry
        while isinstance(slot_entry, int) == False  or slot_entry > num_part or slot_entry < 1:
            try:
                slot_entry = int(slot_entry)
                print(slot_entry in dict_part.keys())
                if slot_entry in dict_part.keys():
                    slot_entry = input("Error:\nSlot #" + str(slot_entry) + " is filled. Please try again.\n\nDesired starting slot#[1-" + str(num_part) + "]: ")
                    continue
                elif slot_entry < num_part + 1 and slot_entry > 0:
                    dict_part[slot_entry] = part_name
                    print("Success:\n" + part_name + " is signed up in starting slot #" + str(slot_entry))
                    break
                else:
                    slot_entry = input("Please enter the participant's desired starting slot as an integer between 1 and " + str(num_part) + '.')
            except:
                slot_entry = input("Please enter the participant's desired starting slot as an integer between 1 and " + str(num_part) + '.')
        
        #Test to make sure slot_entry is not already filled
        
