# Welcome
from pip import main
from sympy import false
import csv


print("Welcome to Tournaments R Us")
print("============================")

# Ask for number of participants; initialize participant dictionary
end_condition = 1
while end_condition == 1:
    num_part = input("Enter the number of participants: ")
    try:
        num_part = int(num_part)
        if num_part > 1:
            break
        elif num_part < 1:
            print('Please enter an integer greater than 1')
    except:
        print('Please enter an integer greater than 1')

print("There are " + str(num_part)+ " participant slots ready for sing-ups.")
dict_part = {}

#Initialize the participant dictionary
for i in range(1, num_part):
    dict_part[i] = None

#Master Loop start
end_condition = False
while end_condition == False:
    print('Participant Menu \n================ \n1. Sign Up \n2. Cancel Sign Up \n3. View Participants\n4. Save Changes\n5. Exit')
    main_menu_input = str(input("What is thy bidding my master?")).lower()

    # 1. Sign Up
    if main_menu_input in ['1', '1.', '1. sign up', 'sign up']:
        #Get entries first
        print('Participant Sign Up\n===================\n')
        part_name = str(input('Participant Name: '))
        slot_entry = input('Desired starting slot #[1-' + str(num_part) + "]: ")

        # Check validity of slot_entry
        while isinstance(slot_entry, int) == False  or slot_entry > num_part or slot_entry < 1:
            try:
                slot_entry = int(slot_entry)
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
        
        #Entering into the dictionary
        dict_part[slot_entry] = part_name
        record = 0
        continue

    # 2. Cancel sign up section
    elif main_menu_input in ['2', '2.', '2. ', '2. cancel sign up', 'cancel sign up']:
        #Need to cover if dict_part is empty first
        if dict_part == {}:
            print('There are no entries to cancel!')
        else:
            print('Participant Cancellation\n=======================\n')
            cancel_slot = input('Starting slot #[1-' + str(num_part) + ']: ')
            cancel_name = str(input('Participant Name: ' )).lower()

            # Validate responses:
            end_loop_condition = 1
            while end_loop_condition == 1:
                try:
                    cancel_slot = int(cancel_slot)
                    if cancel_slot not in dict_part.keys():
                        print("Error:\n" + str(cancel_slot) + " does not have an entry.\n")
                        cancel_slot = input('Starting slot #[1-' + str(num_part) + ']: ')
                        cancel_name = str(input('Participant Name: ' )).lower()
                    elif cancel_name not in dict_part.values():
                        print("Error:\n" + cancel_name + " is not in the tournament.\n")
                        cancel_slot = input('Starting slot #[1-' + str(num_part) + ']: ')
                        cancel_name = str(input('Participant Name: ' )).lower()
                    elif cancel_name != dict_part[cancel_slot]:
                        print("Error:\n" + cancel_name + " is not in that starting slot.\n")
                        cancel_slot = input('Starting slot #[1-' + str(num_part) + ']: ')
                        cancel_name = str(input('Participant Name: ' )).lower()
                    elif cancel_name == dict_part[cancel_slot]:
                        dict_part.pop(cancel_slot)
                        print("Success:\n" + cancel_name + " has been cancelled from starting slot #" + str(cancel_slot))
                        break
                except:
                    print('Error- the slot number you entered was invalid.\n')
                    cancel_slot = input('Starting slot #[1-' + str(num_part) + ']: ')
                    cancel_name = str(input('Participant Name: ' )).lower()
            record = 0
            continue

    # 3. View Participants        
    elif main_menu_input in ['3', '3.', '3. ', '3. view participants', 'view participants']:
        print('View Participants\n================')
        view_slot = input('Starting slot #[1-' + str(num_part)+ ']: ')
        end_condition = 1
        while end_condition == 1:
            try:
                view_slot = int(view_slot)
                if view_slot <= num_part-5 and view_slot >= 5:
                    print("Starting Slot: Participant\n" + str(dict_part[view_slot-5:view_slot+5]))
                    break
                elif view_slot <= num_part-5 and view_slot < 5:
                    print("Starting Slot: Participant\n" + str(dict_part[1:view_slot+5]))
                    break
                elif view_slot <= num_part and view_slot >= num_part-5:
                    print("Starting Slot: Participant\n" + str(dict_part[view_slot-5:num_part]))
                    break
                else:
                    print("That integer is out of range! Please try again!\n")
                    view_slot = input('Starting slot #[1-' + str(num_part)+ ']: ')
            except:
                print('Please enter an integer!\n')
                view_slot = input('Starting slot #[1-' + str(num_part)+ ']: ')


    # 4. Save Changes
    elif main_menu_input in ['4', '4.', '4. ', '4. save changes', 'save changes']:
        print('Save Changes\n============')
        answer_csv = str(input("Save your changes to CSV? [y|n]")).lower()
        end_condition = 1
        while end_condition == 1:
            if answer_csv in ['n', 'no']:
                print("Okay, returning to the main menu.")
                break
            elif answer_csv in ['y', 'yes']:
                csv_file_name = str(input("Which empty csv file should the data be written to? "))
                try:
                    with open(csv_file_name, 'wb') as csv_file:
                        for entry in dict_part.keys():
                            csv_file.write("%s,%s\n"%(entry, dict_part[entry]))
                except:
                    print("Please enter a valid empty csv file name.")
            else:
                print("Please answer yes or no\n")
                answer_csv = str(input("Save your changes to CSV? [y|n]")).lower()

        #remember: record = 1

    # 5. Exit
    elif main_menu_input in ['5', '5.', '5. ', '5. exit', 'exit']:
        print('abc')

    # If invalid input
    else:
        print('abc')

