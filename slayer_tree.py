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
    'Athlete', 'Brawler', 'Swift', 'Weapon Initiate',  'Hulking'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Battle-Hardened': ['Weapon Initiate', 'Brawler'],
    'Close Quarters Gunner': ['Weapon Initiate'],
    'Crusher': ['Weapon Initiate'],
    'Deadly Duelist': ['Weapon Initiate'],
    'Dual Wielder': ['Weapon Initiate'],
    'Fleetfooted Flurry': ['Weapon Initiate', 'Swift', 'Athlete'],
    'Savage Striker': ['Brawler', 'Weapon Initiate'],
    'Martial Artist': ['Brawler'],
    'Charger': ['Hulking', 'Athlete', 'Weapon Initiate', 'Brawler']
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Bladedancer': ['Deadly Duelist', 'Dual Wielder', 'Fleetfooted Flurry'],
    'Bone Breaker': ['Savage Striker', 'Crusher', 'Charger'],
    'Champion': ['Athlete', 'Battle-Hardened'],
    'Lead Slugger': ['Deadly Duelist', 'Close Quarters Gunner'],
    'Veteran Brawler': ['Brawler'],
    'Weapons Adept': ['Weapon Initiate']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Battle-Tested': ['Weapons Adept', 'Veteran Brawler', 'Champion']
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'Legendary Slayer': ['Battle-Tested', 'Bone Breaker', 'Lead Slugger', 'Bladedancer', 'Martial Artist']
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'slayer_tree')
dot.render(output_path, view=True)