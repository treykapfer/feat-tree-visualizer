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
    'Athlete', 'Bloodlust', 'Brawler', 'Cannibal',  'Fury of Fang & Claw',
    'Hulking', 'Predatory Instict', 'Sadist', 'Serial Killer', 'Weapon Initiate'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Berserker': ['Bloodlust', 'Predatory Instict'],
    'Charger': ['Hulking', 'Athlete', 'Weapon Initiate', 'Brawler'],
    'Crusher': ['Weapon Initiate'],
    'Dreadmonger': ['Cannibal', 'Sadist', 'Serial Killer'],
    'Savage Striker': ['Weapon Initiate', 'Brawler']
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Wielder of the Inner Flame': ['Fury of Fang & Claw'],
    'Bone Breaker': ['Savage Striker', 'Crusher', 'Charger'],
    'Feral Terror': ['Berserker']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Juggernaut': ['Hulking', 'Wielder of the Inner Flame','Bone Breaker'],
    'Gorefiend': ['Feral Terror', 'Dreadmonger', 'Wielder of the Inner Flame','Bone Breaker']
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'Carnal Savage': ['Gorefiend'],
    'The Great Behemoth': ['Juggernaut']
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'beast_tree')
dot.render(output_path, view=True)