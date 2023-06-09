# Importing spaCy and loading en_core_web_md as it uses word vectors for word comparison and is there for a better comparison
import spacy
nlp = spacy.load('en_core_web_md')

# Creating a dictionary to save comarision scores of each film too.
film_dict = {"": 0 }

# Creating a function which will tokenise the description of the Hulk film and compare it to another string 'film'.
# The similarity rating and content of string 'film' are saved to a dictionary. 
def comparison(film):
    description = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")
    for token in description:
        rating = nlp(film).similarity(description)
        film_dict.update({str(film) : rating})

# The file with film descriptions is opened and iterated over.
# The function is run for every line in the file.
with open('movies.txt', 'r') as file:
    Lines = file.readlines()
    for line in Lines:
        film = line
        comparison(film)

# The max rating from the dictionary is found and it's key printed along with text indicating that this is the recommendation.
recommendation = max(film_dict, key=lambda x:film_dict[x])
print("Did you enjoy watching Planet Hulk? If so we recommend watching " + recommendation)

   



    



