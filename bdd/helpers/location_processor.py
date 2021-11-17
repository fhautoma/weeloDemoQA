import json
import random


file = open("C:\\Users\\user\\Documents\\GitHub\\_weeloDemoQA\\bdd\\helpers\\states_and_cities.json", "r")


def get_state_and_city():

    data = json.load(file)
    states_list = random.choice(['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan'])
    city = random.choice(data[f"{states_list}"])

    data_dict = {
        "state": f"{states_list}",
        "city": f"{city}"
    }
    file.close()
    return data_dict
