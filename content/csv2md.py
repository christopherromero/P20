import pandas as pd
from io import StringIO

# Function to convert the entire CSV string to a markdown table
def csv_to_markdown(csv_string):
    # Convert the CSV string to a DataFrame
    csv_data = StringIO(csv_string)
    df = pd.read_csv(csv_data)
    
    # Convert the DataFrame to a Markdown table
    markdown_table = df.to_markdown(index=False)
    return markdown_table       

# Example CSV string input
csv_string = """Name,Location Met,Description,Info
Dotty,Apalachia equivalent of Augard,"Female Goliath, a bit shorter than Imn","Childhood friend, introduces Imn to local fighting pit"
Aurlok Trueguard,Apalachia equivalent of Augard,Older Male Goliath,"Currently a Blacksmith and formerly a Warden, Imn's fighter trainer"
Earthspeaker Soot,Inrith,Older late 70s Earth Genasi,"Earth Speaker for the Inrith tribe, it is in important position in Indengious society."
Gideon,Deep South Augard,Human Male,"Very intense individual, trainer for Vale"
Rirrk,Caelkirk,"Male Aarakocra, 20's","Intern for Titanpelt Industries, one of many staff at Caelkirk. Probably not getting enough sleep."
Dougart Williamson,Caelkirk,"Male Half Elf, 40's, High and tight military haircut","Military Liason for this event, is not enjoying himself at all"
Constance Ruppert,Caelkirk,"Female High Elf, 30s","Staff member from Titanpelt, seems overtly friendly, gives off Dolores Umbridge vibes and asethic"
Tilrac Troudaar,Caelkirk,Male Dragonborn,Barbarian Proctor
Thelma Whistlespring,Caelkirk,Female Halfling,Rogue Proctor
Razh,Caelkirk,Male Loxodon,Barbarian participant
Kilid,Caelkirk,Male Half Orc,Barbarian participant
Wilbur Billowdust,Caelkirk,Male Gnome,Artificer participant
Raven,Caelkirk,Male Kenku,Rogue participant
Edgar,Caelkirk,"Male Goliath, more wirey/slim build, Bow user",Fighter participant
Marcus Heraldbringer,Caelkirk,"Human Male, Giving off Lord Farquaad vibes","Paladin participant, not very smart, very ego centric"
Yoslen Sparklefen,Caelkirk,Female Gnome Artificer Proctor,
Tommy,Caelkirk,Male Half-Orc Fighter participant,
Yameia,Caelkirk,"Female Variant Tiefling, Effie Trinket vibes",
Garxes,Caelkirk,"Male Tiefling Lawyer for Titanpelt, very serious",
Dukka,Caelkirk,"Titanpelt Intern, Aarakocra",
Frederick Yew,Caelkirk,"Wood Elf, Fighter proctor, military man",
Gavin,Eshhelion,"Human Male, 30s Titanpelt security guard at the main gate",
Butch T Cougar,Eshhelion,"Male Tabaxi, Titanpelt staff member in R&D, Head of Magical Rings, married to Husband+Coworker Harry",
Harry,Eshhelion,"Ardling that looks like a Husky, Titanpelt staff member in R&D, Head of Magical Cloaks, married to husband+coworker Butch",
Oenru Agilepelt,Eshhelion,"Minotaur male, head of secret service detail",
Utzu,Eshhelion,"female Yuan-ti, head of Titanpelt security/personal security officer",
Bilben Finediggles,Eshhelion,Looks like a Gnome version of Teddy Rosevelt. President of Augard.,
Lila Titanpelt,Eshhelion,"CEO/President of Titanpelt. A Elven woman who looks like she is in her early 40s, tall (6 feet) and slender build. While she is the most powerful person in Augard and probably never had to get her hands “dirty” that she has actually contributed and you can tell that her hands are of those that still to this day work, while not as often in the laboratory. She has dark brown hair, that is silky/shiny that goes down about shoulder length. Typically seen in a suit of some variety. When she enters a room, a silence seems to come over it, her blue eyes pierce through the soul of anyone who dares step out of line in her presence.
",
Magnus Titanpelt,Eshhelion,"RIP/Dead, Lils's father, original founder of Titanpelt. You see a statue of him in the Titanpelt executive building lobby.",
Litany,HOME HQ,"(Owlin Librarian Male (He/Him) Looks like he is in his 50s, thin academic type in magnificent robes. You can tell that some of his feathers are white with aging. Roughly 4 and half feet tall. Can be a bit persnickity at times, is the keeper of the library and tomes, takes himself very serious.
",
Godfrey ,HOME HQ,"(Drawf, head of the home, generalist, Male (He/Him) Looks like he is in his 60’s, still stout and always impeccably dressed. Long bread that is braided, and hair that is tied up in a man bun. Roughly 3 and half feet tall. Always has a warm smile and is looking to help whenever possible. Always available to answer questions and provide assistance.",
Miah,HOME HQ,"(Half Orc chef, Female (She/Her) Always in her chefs outfit, her apron is covered in flour or whatever she is cooking up but otherwise her clothes have no stains. 6 feet tall and very muscular. Can have a very crass sense of humor.",
Dreyus,HOME HQ,"(Tiefling Quartermaster, Non Binary (They/Them) They are roughly 5 feet 10 inches tall, muscular from working a very manual job. Dark red skin, with cuts across their body. Wears leathers and an apron. Hair cut high and tight, military esque. Thier right horns tip is broken off. Is very indifferent, is not trying to be rude but may come off as such. Seems to have been in the military in the past but takes his work seriously.",
Milton,HOME HQ,"Human Arcanist/Ingredient cultivator (He/Him) Thin academic type in well worn robes that while clean, have various stains from previous magical experiments and cultivation. 5 foot 8 inches tall and looks like he is in his late 40s. Undercut haircut. Very friendly and will talk your ear off about anything Arcana/Magic related.
",
"""

# Convert the CSV string to a Markdown table
markdown_table = csv_to_markdown(csv_string)

# Save the Markdown table to a file or print it
with open("markdown_table.md", "w") as file:
    file.write(markdown_table)

print(markdown_table)