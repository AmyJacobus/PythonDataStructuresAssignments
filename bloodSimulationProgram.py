import random
from datetime import datetime, timedelta


def blood_sample_generator(blood_types):
    """
    Generates 10 blood samples a day
    :param blood_types:
    :return:
    """
    daily_blood_sample = []

    # blood type
    random_blood = random.choice(blood_types)
    daily_blood_sample.append(random_blood)
    #print(daily_blood_sample)

    # get_date(): # CAN BE COMPARED BY
    # Using current time
    ini_time_for_now = datetime.now()
    todays_date = ini_time_for_now.strftime("%d_%m")
    daily_blood_sample.append(todays_date)
    #print('Todays date: ', todays_date)
    after_21days = ini_time_for_now + timedelta(days=21)
    expiration_dates = after_21days.strftime("%d_%m")
    daily_blood_sample.append(expiration_dates)
    #print('Expiration date: ', expiration_dates)

    # serial_code_generator(start_d, end_d):

    serial_number = random.randint(1, 99999999999)
    daily_blood_sample.append(serial_number)

    #print(daily_blood_sample)
    return daily_blood_sample


def hasher(blood_sample):  # NEED TO FIX
    """
    This how we generate an location_id_code that is going to be labeled on to the sample, basically becomes
    a value in that blood sample list, which will be used to keep track of that specific blood sample, which
    can be removed later on
    :param blood_types:
    :return:
    """
    global new_hash_id
    new_hash_id = ""

    blood = blood_sample[0]
    #print('blood?', blood)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
    reverse = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']

    # hash_code = []
    # blood_sample_id_codes = []
    # blood_hash_code = []
    for letter in blood:
        position = alpha.index(letter)  #0
        #print('test', position)
        new_hash_id += reverse[position] # generates the hash code for me.
        #hash_code.append(new_hash_id)
        # position = blood_hash_code.index(blood)
        # print(position)
        # list = blood_hash_code[position]
        # print(list)
        # list.append(new_hash_id)
        # blood_sample_id_codes.append(list)
    #print(new_hash_id)  # the hash coded if for that blood type
    # blood_sample.append(new_hash_id)
    #print(blood_sample)
    return blood_sample

def pods_location_checker(list, blood_types, blood_sample):
    """
    THis functions basically checks all the blood samples  based on their hash location id and makes
    sure that they get stored in the right pods and returns the list to the system so other
    systems can continue with their simulated automated work.
    :return: pod_database basically
    """

    #Original sample to test
    sample = [["oneg","21","234","pod1"],["oneg","23","235","pod1"],["oneg","26","236","pod1"],
              ["oneg","26","236","pod2"],["oneg","26","236","pod2"],["oneg","26","236","pod2"],
              ["oneg","26","236","pod3"],["oneg","26","236","pod3"],["oneg","26","236","pod3"],
              ["oneg","26","236","pod4"],["oneg","26","236","pod4"],["oneg","26","236","pod4"],
              ["oneg","26","236","pod5"],["oneg","26","236","pod5"],["oneg","26","236","pod5"],
              ["oneg","26","236","pod6"],["oneg","26","236","pod6"],["oneg","26","236","pod6"],
              ["oneg","26","236","pod7"],["oneg","26","236","pod7"],["oneg","26","236","pod7"],
              ["oneg","26","236","pod8"],["oneg","26","236","pod8"],["oneg","26","236","pod8"]]

    blood_code_hashed_list = []
    x = 0
    for i in blood_types:
        hash_code = hasher(blood_types[x])
        blood_code_hashed_list.append(hash_code)
        x += 1


    lista = list
    # for x in sample:
    #     sample_1 = x
    if blood_sample[0] == blood_code_hashed_list[0]:
        lista[0].append(blood_sample)
    elif blood_sample[0] == blood_code_hashed_list[1]:
        lista[1].append(blood_sample)
    elif blood_sample[0] == blood_code_hashed_list[2]:
        lista[2].append(blood_sample)
    elif blood_sample[0] == blood_code_hashed_list[3]:
        lista[3].append(blood_sample)
    elif blood_sample[0] == blood_code_hashed_list[4]:
        lista[4].append(blood_sample)
    elif blood_sample[0] == blood_code_hashed_list[5]:
        lista[5].append(blood_sample)
    elif blood_sample[0] == blood_code_hashed_list[6]:
        lista[6].append(blood_sample)
    elif blood_sample[0] == blood_code_hashed_list[7]:
        lista[7].append(blood_sample)

    return lista


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

def remove_expired_samples(list): #use a while to loop and check the first in and last out method -quee
    """
    This is the function that is going to make sure that we never have expired bloods
    stuck in our pods at any given time. It does so by checking the current date, and checks every pods and
    their blood samples to make sure they have not expired yet, and remove the ones that have expired.
    :param list:
    :return:
    """
    pass
    ini_time_for_now = datetime.now()
    todays_date = ini_time_for_now.strftime("%d_%m")

    list = list
    date = todays_date
    removed = 0
    print("Current date: ", date)
    for x in list: # get each pod
        pod = x
        print("Pod is:", pod)
        print(pod[0][2])
        if pod[0][2] == date or pod[0][2] > date:
            sample = pod[0]
            pod.remove(sample)
            removed = 1
    print(f"A total of {removed} pods have been removed on {todays_date}")
    return list


# Assignment #2
def random_blood_need_request(blood_types):  # take from the beginning
    """
    This function basically generates (random amount) people that need different types of blood. The function will create
    a list of need consisting of x amount of blood samples. It will keep track of the amount of blood types and
    create an amount:
    For example oneg: 6, ab-neg: 8, ab-pos: 2
    And based on these numbers, it will run a for loop to grab those list (blood samples) and pull
    them into another list, which together will create another 3D list, that will be the (blood deliveyr)
    bag or something like that, that the medical lab will take for the day
    :return:
    """

    people_that_need_blood = random.randint(1, 10)
    for i in people_that_need_blood:
        generate_blood_request = random.choice(blood_types)
        blood_request = []
        blood_request.append(generate_blood_request)

    aneg = 0
    apos = 0
    bpos = 0
    bneg = 0
    abpos = 0
    abneg = 0
    opos = 0
    oneg = 0

    if  blood_request == 'aneg':
        aneg += 1
    elif blood_request == 'apos':
        apos += 1
    elif blood_request =='bpos':
        bpos  += 1
    elif blood_request == 'bneg':
        bneg += 1
    elif blood_request == 'abpos':
        abpos += 1
    elif blood_request == 'abneg':
        abneg += 1
    elif blood_request == 'opos':
        opos += 1
    elif blood_request == 'oneg':
        oneg += 1


def generate_10_pods_daily(list):

    day = 1
    while day != 11:
        blood_types = ["aneg", "apos", "bpos", "bneg", "abpos", "abneg", "opos", "oneg"]
        blood_sample = blood_sample_generator(blood_types)
        blood_sample_complete = hasher(blood_sample)
        list = pods_location_checker(list, blood_types, blood_sample_complete)
        day += 1
    #pod_list_report(list)
    return list


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
    list = [[], [], [], [], [], [], [], []]

    day = 1
    while day != 31: #runs simulation for 31 days
        lista = generate_10_pods_daily(list) # populate pods with 10 everyday
        report = pod_list_report(list)
        list = remove_expired_samples(list)
        print(f"Day #{day} pod report")
        report1 = pod_list_report(list)
        day += 1




    #simulate 10 pods a day


    # blood_list = blood_sample_generator(blood_types)
    # blood_list = serial_code_generator(blood_list)
    # hasher(blood_types)
    # list = pods()
    # pod_list_report(list)
    # remove_expired_samples(list)


    # for loop to run for 21 days



if __name__ == '__main__':
    main()