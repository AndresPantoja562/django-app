import requests
import os

def get_coments_data (api_key) :
    print ("Getting coments data")
    api_url= f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        #show data
        #coment name
        print ("Coment name:", data [ "name"])
        #Apsolute magnitude print("Apsolute magnitude: ",
        print ("apsolute magnitude: ", data ["absolute_magnitude_h"])
        #Estimated diameter Max (km)
        print ("Estimated diameter max (km): ", data["estimated_diameter"] ["kilometers"] ["estimated_diameter_max"])
        #Estimated diameter min (km)
        print("Estimated diameter min (km): ", data["estimated_diameter"] ["kilometers"] ["estimated_diameter_min"])
        #Estimated diameter Max (ft)
        print("Estimated diameter max (ft): ", data["estimated_diameter"]["feet"] ["estimated_diameter_max"])
        #Estimated diameter min (ft)
        print("Estimated diameter min (ft): ", data["estimated_diameter"]["feet"] ["estimated_diameter_min"])
        #obital data:
        #last observation date
        print ("Last observation date: ", data["orbital_data"] ["last_observation_date"])
    except requests.exceptions.RequestException as e:
        print (f"API ERROR{e}")

api_key_nasa = "eEqVBWUM3eotzuCJ1jTkKpWsx0wZfjz45yhVvKfG"
get_coments_data(api_key_nasa)