

import json
import urllib.request
import random
import webbrowser
import facebook

SEARCH_ENGINE_ID = "016782293291136921152:iomvwhhbvjk"
GOOGLE_API_KEY = "AIzaSyBwIKySY3CwbVYDTieFVCPauZ4ufnk6WyE"

cities = [
	"pdx",
	"kc",
	"columbus",
	"new york",
	"sf",
	"austin"
]

imageSearchTerms = [
	"fidget+spinner",
    "bee",
    "haramBEE",
    "bee+game",
    "here+come+dat+bee",
    "malort+chicago",
    "killer+queen+game",
    "#mood",
    "REKT"
    "Shrekt",
    "simpsons",
    "futurama",
	"snail",
    "ding+dang+snack",
    "topo+chico",
    "dank+bee",
    "beedrill",
    "salt",
    "Rico-the-dragon",
    "Rico-the-dragon",
    "heard+of+elf+on+the+shelf",
    "sonic",
	"rick+and+morty",
    "dumb+bee+game"
]

imageSearchModifiers = [
    "meme",
    "lit",
    "pokemon",
    "logan+arcade",
    "squad",
    "anime",
    "donald trump",
    "vaporwave",
    "Gucci",
    "af",
    "dank"
    "",
]

basePhrases = [
	"tfw",
	"stingers out",
	"dingers out",
	"my team will be there",
    "literally me",
    "it me",
    "sets tonight?",
    "mood",
    "anyone at logan?",
    "lit *flame*",
    "RIP",
    "let’s gooooooo!",
    "new team name",
    "get wrecked",
    "scene’s dead",
    "scene’s lit",
    "you know where i’m at",
    "who's with me?",
    "Honestly",
	"Malort is the worst",
	"Anyone looking for a team?",
    "boi",
	"anyone going to <city> this weekend?"
]

phraseModifiers = [
    "@Dre Quan",
    "@Josh Debones",
    "@Nikita Mikaros",
    "Fam",
    "Ding",
    "Dang",
    "Dong",
    "heck",
    "LOL",
	"lmao",
	"lmfao",
	"sup",
	"#mood",
	"rip"
    "boi",
    "🔥",
	"<3",
    "😱"
]



searchTerm = random.choice(imageSearchTerms);
searchTerm += "+"
searchTerm += random.choice(imageSearchModifiers)

print("Searching for " + searchTerm)

imageURL = ""


try:
    url = "https://www.googleapis.com/customsearch/v1?q="+searchTerm+"&cx=016782293291136921152%3Aiomvwhhbvjk&imgSize=large&num=10&searchType=image&fields=items%2Flink&key=" + GOOGLE_API_KEY
    req = urllib.request.urlopen(url)
    
    responseAsJson = json.load(req)
    imageURLs = []
    for item in responseAsJson["items"]:
        imageURLs.append(item["link"]);
    
    imageURL = random.choice(imageURLs);

    
    webbrowser.open(imageURL)
except:
    print("failed to perform image search")


message = random.choice(basePhrases)
message = message.replace('<city>', random.choice(cities))

#facebook.GraphAPI.get_access

#facebookGraph = facebook.GraphAPI(access_token="", version="2.10")
#version = facebook.GraphAPI.get_version();
#print("facebook graph api version: " + version)

print(imageURL);

if random.uniform(0, 100) < 50:
    modifier = random.choice(phraseModifiers)
    message += " " + modifier


print(message);
