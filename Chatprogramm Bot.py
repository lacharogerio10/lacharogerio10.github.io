def answerquestion():
  meineAntwort = input("Schreibe etwas Nettes! ")

  if meineAntwort == "Du bist nett":
    print(":-)")
  elif meineAntwort == "Du bist doof":
    print(":-(")
  else:
    print(":-|")
while True:
  answerquestion()

import requests

# This function will store your text in one of the training
# buckets in your machine learning project
def storeTraining(text, label):
    key = "febb27f0-a11b-11ec-b5d7-074a398540119a773ab3-3e84-4b36-953d-e6fbb262541c"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/train"

    response = requests.post(url, json={ "data" : text, "label" : label })

    if response.ok == False:
        # if something went wrong, display the error
        print (response.json())


# CHANGE THIS to the text that you want to store
training = "The text that you want to store"

# CHANGE THIS to the training bucket to store it in
label = "Beleidigungen"

storeTraining(training, label)
