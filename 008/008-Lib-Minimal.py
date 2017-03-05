import random, json
from time import gmtime, strftime
def bar(stat, maximum, label): # prints a stat bar
    templateForLabel = list("            :")
    for key, letter in enumerate(label): templateForLabel[key] = letter # Zero pad label
    templateForBar = "["
    for i in range(1, maximum+1): templateForBar += " " #Generate a [    ] of specified maximum length
    templateForBar += "]"
    templateForBar = list(templateForBar)
    for key in range(stat): templateForBar[key + 1] = "~" # Add correct amount of ~ to [~~~~    ]
    return ''.join(templateForLabel) + " " + ''.join(templateForBar) # Finalise the bar
random.seed(strftime("%Y-%m-%d %H:%M:%S", gmtime())) # Random seed should be random if not secure
possibilities = {"rpgClass": ["Elf", "Dwarf", "Human", "Zombie", "Spirit"], "gender": ['Agender', 'Androgyne', 'Androgynous', 'Bigender', 'Cis', 'Cisgender', 'Cis Female', 'Cis Male', 'Cis Man', 'Cis Woman', 'Cisgender Female', 'Cisgender Male', 'Cisgender Man', 'Cisgender Woman', 'Female to Male', 'FTM', 'Gender Fluid', 'Gender Nonconforming', 'Gender Questioning', 'Gender Variant', 'Genderqueer', 'Intersex', 'Male to Female', 'MTF', 'Neither', 'Neutrois', 'Non-binary', 'Other', 'Pangender', 'Trans', 'Trans*', 'Trans Female', 'Trans* Female', 'Trans Male', 'Trans* Male', 'Trans Man', 'Trans* Man', 'Trans Person', 'Trans* Person', 'Trans Woman', 'Trans* Woman', 'Transfeminine', 'Transgender', 'Transgender Female', 'Transgender Male', 'Transgender Man', 'Transgender Person', 'Transgender Woman', 'Transmasculine', 'Transsexual', 'Transsexual Female', 'Transsexual Male', 'Transsexual Man', 'Transsexual Person', 'Transsexual Woman', 'Two-Spirit', 'Male', 'Female'], "strength": {"Elf": list(range(3,8)), "Dwarf": list(range(6,10)), "Human": list(range(0,5)), "Zombie": list(range(7,10)), "Spirit": list(range(0,2))}, "magic": {"Elf": list(range(5,8)), "Dwarf": list(range(3,5)), "Human": list(range(0,2)), "Zombie": list(range(9,10)), "Spirit": list(range(5,10))},"dexterity": {"Elf": list(range(5,8)), "Dwarf": list(range(3,5)), "Human": list(range(0,2)), "Zombie": list(range(9,10)), "Spirit": list(range(5,10))}, "possibleExtras": [["diorreah", -5], ["super eyesight", 5], ["super speed", 6], ["psycic powers", 10], ["a headache", -3], ["dyspraxia", -4]]}
class Character: # Create a character class
    def __init__(self): #Initialise, letting user/programmer set name
        self.rpgClass, self.gender, self.strength, self.magic, self.dexterity, self.extra, self.name = (random.choice(possibilities["rpgClass"]), random.choice(possibilities["gender"]), random.choice(possibilities["strength"][self.rpgClass]), random.choice(possibilities["magic"][self.rpgClass]), random.choice(possibilities["dexterity"][self.rpgClass]), random.choice(possibilities["possibleExtras"]), random.choice(["Voltar", "Vultrax", "Frizban", "Rasputin", "Rostor", "Simonexto", "Guurglex"]) + random.choice(["bald", "ban", "buck", "tor", "van", "gax", "trandor", "thuri", "ben", "baldar", "may", "lam", "mor", "dard", "burg", "whit"]) + "-" + random.choice(["Ard", "Alf", "Fiz", "Risa", "Warran", "Kel", "Wren", "Kan", "Can", "Gy", "Dero", "Ak", "Dall", "Dell", "Mil", "Ward"]))
        if self.calculateOverallPoints() <= 4: self.level = "Junior" 
        elif self.calculateOverallPoints() <= 12: self.level = "Level 1"          # Choose level of player
        elif self.calculateOverallPoints() <= 20: self.level = "Level 2"
        elif self.calculateOverallPoints() <= 30: self.level = "Level 3"
        else: self.level = "Level 4"
    def outputJson(self):
        # Model: {"name":"gender": "Male", "class": "Elf", "stats": {"magic": 6 etc}, "extra": ["super eyesight", 5], "overallPoints": 20}
        return {"name": self.name, "gender": self.gender, "class": self.rpgClass, "level": self.level, "stats": {"magic": self.magic, "strength": self.strength, "dexterity": self.dexterity}, "extra": self.extra, "overallPoints": self.strength + self.magic + self.dexterity + self.extra[1]}
    def save(self, fileName):
        with open(fileName, "w") as f: f.write(json.dumps(self.outputJson()))  # Save output of json dump to user file
    def load(self, fileName):
        with open(fileName, "r") as f: jsonRead = f.read()
        jsonObj = json.loads(jsonRead)
        self.rpgClass, self.gender, self.strength, self.magic, self.dexterity, self.extra, self.name = (jsonObj['class'],jsonObj['gender'],jsonObj['stats']['strength'],jsonObj['stats']['magic'],jsonObj['stats']['dexterity'],jsonObj['extra'],jsonObj['name'])
        if self.calculateOverallPoints() <= 4: self.level = "Junior" 
        elif self.calculateOverallPoints() <= 12: self.level = "Level 1"          # Choose level of player
        elif self.calculateOverallPoints() <= 20: self.level = "Level 2"
        elif self.calculateOverallPoints() <= 30: self.level = "Level 3"
        else: self.level = "Level 4"
    def prettyPrint(self):
        return "\n~~~ RPG Character Generator V1 ~~~\n\nYour character is called {}, and has {}.\nThey identify as a(n) {} {} {}.\nTheir overall power is {}.\nTheir stats are:\n{}\n{}\n{}""".format(self.name, self.extra[0], self.gender, self.level, self.rpgClass, self.strength + self.magic + self.dexterity + self.extra[1], bar(self.magic, 10, "Magic"), bar(self.dexterity, 10, "Dexterity"), bar(self.strength, 10, "Strength")) # Fill template with values
