#
import os, json
#------------------------------------Settings-----------------------------------------------------------------
folderName      = 'Input'  # WITHOUT / or \ #It should be in the same path of the script, Thanks.
JsonFileName    = 'session_data'   # WITHOUT EXTENTION(.json)
#-------------------------------------------------------------------------------------------------------------




# Functions
def getJsonCollectionFromTextFile(foldername,filename):
    with open(f"{foldername}/{filename}", "r", encoding="utf-8") as f:
        text = f.read()

        # Splitting every line in a list of sentences 
        # Exemple : ['Chedy  ', 'INTRO TEXT What happens when we defer', '', 'Unknown Speaker  ', 'It was around financial security.',]
        list_of_sentences = text.split("\n")

        # Cleaning.... / Removing Every "" (which represents an empty line)
        while("" in list_of_sentences):
            list_of_sentences.remove("")

        # Cleaning.... / Removing Every "Transcribed by https://otter.ai"
        while("Transcribed by https://otter.ai" in list_of_sentences):
            list_of_sentences.remove("Transcribed by https://otter.ai")
        
        # Cleaning.... / Making Sure that Chedy and Unknow Speaker are exactly "Chedy" and "Unknow Speaker", in some cases we might find "Chedy   " with weird spaces
        for i in range(len(list_of_sentences)):
            this_line = list_of_sentences[i]
            if this_line[:5] == "Chedy":
                list_of_sentences[i] = "Chedy"                 # Forcing the change of value
            if this_line[:15] == "Unknown Speaker":
                list_of_sentences[i] = "Unknown Speaker"       # Forcing the change of value

        # Main Program.... / Classifing the sentences in two diff Prompts
        jsonData        = []

        current_Speaker = None              # First we don't know who's the speaker so it's none

        while (len(list_of_sentences) > 0): # We will go through the list if it's not empty (Setting this condition will be usefull later on because we will remove each line who have been consulted by the program)
            lineIndex = 0
            l = list_of_sentences[lineIndex]
            #If it's Chedy we will create a new promt, if it's the AI Responder we will add data to the latest availble prompt
            if l in ["Chedy", "Unknown Speaker"]: # If the line is Chedy of unknown speak we will just save that in memory and go next line by breaking of the for loop
                current_Speaker = l
                if l == "Chedy": #make a new Prompt
                    jsonData.append({"prompt": "Unknown Speaker: ", "completion": "Chedy: "})
            else:
                if current_Speaker == "Chedy":   # If the line is a chat message then we save it to the corresponding current speaker's List of data
                    # Add this line to the latest prompt data in the "completion" field
                    if len(jsonData)> 0:
                        jsonData[len(jsonData)-1]["completion"] += l
                elif current_Speaker == "Unknown Speaker":
                    # Add this line to the latest prompt data in the "prompt" field
                    if len(jsonData)> 0:
                        jsonData[len(jsonData)-1]["prompt"] += l

            lineIndex +=1# Appending Index to go next
            list_of_sentences.remove(l) #Removing the line also to go next and make the while loop stop in case of completion 
        return jsonData

def getAllTextFilesFromFolder(foldername):
    txt_files_to_return = []
    all_files = os.listdir(f"{foldername}/")
    for file in all_files:
        if file[-4:] == '.txt':
            txt_files_to_return.append(file)
    return txt_files_to_return

# Main
if __name__ == "__main__":
    files           = getAllTextFilesFromFolder(folderName)
    print(f'Found {len(files)} Text files in {folderName} folder.')
    biggestJsonData = []
    for file in files :
        biggestJsonData += getJsonCollectionFromTextFile(folderName,file)

    with open(f"Output/{JsonFileName}.jsonl", "w", encoding="utf-8") as outfile:
        for element in biggestJsonData:
            json.dump(element, outfile, ensure_ascii=False)
            outfile.write('\n')
    print(f"Everything went fine, {JsonFileName}.jsonl created.")