import random
from datetime import datetime, timedelta


def blood_sample_generator(blood_types):
    """
    Generates 10 blood samples a day
    :param blood_types:
    :return:
    """
    daily_blood_samples = []
    for x in range(1, 11):
        blood_sample = []
        random_blood = random.choice(blood_types)
        blood_sample.append(random_blood)
        daily_blood_samples.append(blood_sample)

    print(daily_blood_samples) # list of 10 blood samples


def get_date(): # CAN BE COMPARED BY
    # Using current time
    ini_time_for_now = datetime.now()
    todays_date = ini_time_for_now.strftime("%d_%m")
    print('Todays date: ', todays_date)
    after_21days = ini_time_for_now + timedelta(days=21)
    expiration_dates = after_21days.strftime("%d_%m")
    print('Expiration date: ', expiration_dates)

    return todays_date, expiration_dates


def serial_code_generator(start_d, end_d):
    """
    Basically labels each samples and updates the list with the date it was created and a serial number randomly generated
    :param blood_list:
    :return:
    """



    date = 22
    count = len(blood_list)
    for x in blood_list:
        x.append(date)
        count +=1
        x.append(date + count + random.randint(1,123590)) #gives the actual serial number and add it to the list

    return blood_list
    # print(blood_list) // to test


def hasher(): # NEED TO FIX
    """
    This how we generate an location_id_code that is going to be labeled on to the sample, basically becomes
    a value in that blood sample list, which will be used to keep track of that specific blood sample, which
    can be removed later on
    :param blood_types:
    :return:
    """
    global new_hash_id
    new_hash_id = ""

    blood_types  = ['opos']  # EXAMPLE, MAKE SURE TO CHANGE

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
    reverse = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']

    hash_code = []
    blood_sample_id_codes = []
    blood_hash_code = []
    for blood in blood_types:
        for letter in blood:
            blood_hash_code.append(blood)
            position = alpha.index(letter)  #0
            new_hash_id += reverse[position] # generates the hash code for me.
            #hash_code.append(new_hash_id)
            # position = blood_hash_code.index(blood)
            # print(position)
            # list = blood_hash_code[position]
            # print(list)
            # list.append(new_hash_id)
            # blood_sample_id_codes.append(list)
    print(new_hash_id) # the hash coded if for that blood type
    """
    hash_code.append(str(numbers[position]))
    new_id = ''.join(map(str, hash_code))
    print("New id: " ,new_id)
    blood_sample_id_codes.append(new_id)
    print(blood_sample_id_codes)
    """
    #return blood_sample_id_codes

    #return hash_coder

def pod_hash(blood_type_id):
    """
    THis function basically creates a hash for each bloodtype, which will be stored and labeled on each
    blood samples later on for location identifcation that only the system will be able to understand.  For example
    oneg turns into zeda, which will be labeled on each blood sample that has oneg. Which will automatically
    be used to detect the location of that blood. That Zeda is suppose to simulate some kind of encryption
    that a system would have later, that a person wouldnt be able to memorize or understand enough to keep
    track of things, but the system itself can keep track of any required data piece that passes through its system.
    :param blood_type:
    :return:
    """

    if bloodtype_id == 'oneg':
        location = "pod1"
    elif bloodtype_id =='oneg':
        location = "pod2"
    elif bloodtype_id == 'oneg':
        location = "pod3"
    elif bloodtype_id == 'oneg':
        location = "pod4"
    elif bloodtype_id == 'oneg':
        location = "pod5"
    elif bloodtype_id== 'oneg':
        location = "pod6"
    elif bloodtype_id == 'oneg':
        location = "pod7"
    elif bloodtype_id== 'oneg':
        location = "pod8"

    return location


def pods_location_checker():
    """
    THis functions basically checks all the blood samples  based on their hash location id and makes
    sure that they get stored in the right pods and returns the list to the system so other
    systems can continue with their simulated automated work.
    :return: pod_database basically
    """
    sample = [["oneg","21","234","pod1"],["oneg","23","235","pod1"],["oneg","26","236","pod1"],
              ["oneg","26","236","pod2"],["oneg","26","236","pod2"],["oneg","26","236","pod2"],
              ["oneg","26","236","pod3"],["oneg","26","236","pod3"],["oneg","26","236","pod3"],
              ["oneg","26","236","pod4"],["oneg","26","236","pod4"],["oneg","26","236","pod4"],
              ["oneg","26","236","pod5"],["oneg","26","236","pod5"],["oneg","26","236","pod5"],
              ["oneg","26","236","pod6"],["oneg","26","236","pod6"],["oneg","26","236","pod6"],
              ["oneg","26","236","pod7"],["oneg","26","236","pod7"],["oneg","26","236","pod7"],
              ["oneg","26","236","pod8"],["oneg","26","236","pod8"],["oneg","26","236","pod8"]]

    # CAN BE 2D ARRAYS IF THAT WORKS MUCH BETTER - 2D LIST WORKS TOO
    list = [[], [], [], [], [], [], [], []]  # 3D list
    for x in sample:
        sample_1 = x
        if sample_1[3] == "pod1":
            list[0].append(sample_1)
        elif sample_1[3] == "pod2":
            list[1].append(sample_1)
        elif sample_1[3] == "pod3":
            list[2].append(sample_1)
        elif sample_1[3] == "pod4":
            list[3].append(sample_1)
        elif sample_1[3] == "pod5":
            list[4].append(sample_1)
        elif sample_1[3] == "pod6":
            list[5].append(sample_1)
        elif sample_1[3] == "pod7":
            list[6].append(sample_1)
        elif sample_1[3] == "pod8":
            list[7].append(sample_1)

    return list


def pod_list_report(list):  #show pod database at whenever requested
    print("Pod1:",list[0])
    print("Pod2:",list[1])
    print("Pod3:",list[2])
    print("Pod4:",list[3])
    print("Pod5:",list[4])
    print("Pod6:",list[5])
    print("Pod7:",list[6])
    print("Pod8:",list[7])


def collision_checker(): #NEED help with this one
    pass # check serial numbers to check if the serial number has the same serial number

def remove_expired_samples(list):
    """
    This is the function that is going to make sure that we never have expired bloods
    stuck in our pods at any given time. It does so by checking the current date, and checks every pods and
    their blood samples to make sure they have not expired yet, and remove the ones that have expired.
    :param list:
    :return:
    """
    date = 19
    for x in list[0]:
        list_layer2 = x
        import_date = list_layer2[1]
        print(import_date) #test
        the_date = int(import_date)
        if the_date > date: #issue getting the date out!
            list[0].remove(list_layer2)
    return list


# Assignment #2
def random_blood_need():
    """
    This function basically generates (random amount) people that need different types of blood. The function will create
    a list of need consisting of x amount of blood samples. It will keep track of the amount of blood types and
    create an amount:
    For example oneg: 6, ab-neg: 8, ab-pos: 2
    And based on these numbers, it will run a for loop to grab those list (blood samples) and pull
    them into another list, which together will create another 3D list, that will be the (blood deliveyr)
    bag or something like that, that the hosipital or medicial faciilit will take for the day
    :return:
    """

#def remove_need_for_blood():
    #pass

def main():
    """
    This main loop basically runs for 30 days straight with several loops running different
    sections daily within that main for loop to simulate the following:
    30 days of the full process
    10 bloods being delivered to the facility daily, that need to be put in the blood pods
    Daily blood checking to make sure that the pods always have none-expired bloods in their pods and removes the ones that have expired
    Will also daily generate a random amount of patients that need blood, which will require a for loop that will get a number of bloods out
    and finally generates a report at the end to show how much blood are still in the pod,
    and provide a visual report of the blood pods.
    :return:
    """
    blood_types = ["aneg", "apos", "bpos", "bneg", "abpos", "abneg", "opos", "oneg"]
    start_d, end_d = get_date()

    # blood_list = blood_sample_generator(blood_types)
    # blood_list = serial_code_generator(blood_list)
    # hasher(blood_types)
    # list = pods()
    # pod_list_report(list)
    # remove_expired_samples(list)


    # for loop to run for 21 days

    # for loop to run for a whole month
    blood_sample_generator(blood_types)

if __name__ == '__main__':
    main()