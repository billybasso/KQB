

import json
import urllib.request
import random
import webbrowser
import facebook

SEARCH_ENGINE_ID = "016782293291136921152:iomvwhhbvjk"
GOOGLE_API_KEY = "AIzaSyBwIKySY3CwbVYDTieFVCPauZ4ufnk6WyE"

teamColors = [
    "gold",
    "blue",
]

teamPositions = [
    "abs",
    "checks",
    "skull",
    "stripes",
    "queen",
]

cabParts = [
    "stick",
    "button"
]

cabPartConditions = [
    "screwy",
    "loose",
    "shit",
    "sticky",
    "bad",
]

times = [
	"15",
	"20",
	"an hour",
	"a couple hours",
	"3 hours"
]

setTimes = [
	"thursday",
	"tonight",
	"tomorrow",
	"monday",
	"tuesday",
	"next week",
	"right now",
]

cities = [
	"pdx",
	"kc",
	"columbus",
	"new york",
	"sf",
	"austin",
    "mpls",
]

imageSearchTerms = [
	"fidget+spinner",
    "bee",
    "haramBEE",
    "bee+game",
    "here+come+dat+bee",
    "malort+chicago",
    "killer+queen+game",
    "mood",
    "REKT",
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
    "donald+trump",
    "vaporwave",
    "Gucci",
    "af",
    "dank"
    "",
]

basePhrases = [
	"headed to the arcade",
	"headed over in <time>",
	"headed to <city> in <time>",
    "<team_color> <team_position> <cab_part> is <cab_part_condition>",
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
	"bae",
	"sets <set_time>?",
    "omw",
	"anyone going to <city> this weekend?",
    "<team_colors> stick is "
]

phraseModifiers = [
    "@Dre Quan",
    "@Josh Debones",
    "@Nikita Mikaros",
    "honestly",
    "fam",
    "ding",
    "dang",
    "dong",
    "heck",
    "LOL",
	"lmao",
	"lmfao",
    "haha",
	"sup",
	"#mood",
    "omg",
	"rip",
    "pls",
    "boi",
    "tbh",
    "🔥",
	"<3",
    "😱",
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


    "<team_color> <team_position> <cab_part> is <cab_part_condition>",

message = random.choice(basePhrases)
message = message.replace('<city>', random.choice(cities))
message = message.replace('<time>', random.choice(times))
message = message.replace('<set_time>', random.choice(setTimes))
message = message.replace('<cab_part>', random.choice(cabParts))
message = message.replace('<team_color>', random.choice(teamColors))
message = message.replace('<team_position>', random.choice(teamPositions))
message = message.replace('<cab_part_condition>', random.choice(cabPartConditions))

#facebook.GraphAPI.get_access

#facebookGraph = facebook.GraphAPI(access_token="", version="2.10")
#version = facebook.GraphAPI.get_version();
#print("facebook graph api version: " + version)

print(imageURL);

while random.uniform(0, 100) < 40:
    modifier = random.choice(phraseModifiers)
    message += " " + modifier


print(message);
