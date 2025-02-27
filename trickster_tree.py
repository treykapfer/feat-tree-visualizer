from graphviz import Digraph
import os

# Create the "exports" folder if it doesn't exist
exports_folder = 'exports'
if not os.path.exists(exports_folder):
    os.makedirs(exports_folder)

# Create a directed graph
dot = Digraph(comment='Feat Progression', format='png')
dot.attr(rankdir='LR')  # Left-to-right layout

# Tier 0 (Base Feats)
tier_0_feats = [
    'Arcanist', 'Unnatural Reflexes', 'Swift', 'Weapon Initiate', 
    'Seasoned Performer', 'Scoundrel', 'Athlete', 'Energy Fiend', 'Well Studied (Artisan)'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Fleetfooted Flurry': ['Weapon Initiate', 'Swift', 'Athlete'],
    'Traceur': ['Swift', 'Athlete'],
    'Sly Villain': ['Scoundrel'],
    'Deadly Duelist': ['Weapon Initiate'],
    'Illusionist': ['Arcanist'],
    'Dammerskript Initiate': ['Arcanist'],
    'Showstopper': ['Seasoned Performer', 'Well Studied (Artisan)'],
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Escape Artist': ['Showstopper', 'Sly Villain', 'Traceur'],
    'Speed Demon': ['Swift', 'Energy Fiend'],
    'Trickshot Maestro': ['Unnatural Reflexes','Traceur','Deadly Duelist','Fleetfooted Flurry'],
    'Invisible Trickster': ['Illusionist', 'Dammerskript Initiate']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Devious Artistry': ['Escape Artist'],
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'The Great Deciever': ['Devious Artistry', 'Trickshot Maestro', 'Invisible Trickster'],
    'Sprite': ['Devious Artistry', 'Speed Demon']
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'trickster_tree')
dot.render(output_path, view=True)