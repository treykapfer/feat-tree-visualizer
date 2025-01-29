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
    'Honed Discipline', 'Eagle Eye', 'Monster Hunter', 'Nightstalker', 
    'Scoundrel', 'Serial Killer', 'Unnatural Reflexes', 'Weapon Initiate'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Inquisitor': ['Monster Hunter'],
    'Sharpshooter': ['Weapon Initiate', 'Eagle Eye'],
    'Silent Predator': ['Weapon Initiate', 'Scoundrel', 'Serial Killer', 'Nightstalker'],
    'Vigilant': ['Unnatural Reflexes', 'Eagle Eye'],
    'Lethal Focus': ['Honed Discipline', 'Eagle Eye']
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Death Dealer': ['Inquisitor', 'Silent Predator'],
    'True Shot': ['Sharpshooter'],
    'Weapons Adept': ['Weapon Initiate'],
    'Nightward Hunter': ['Vigilant', 'Lethal Focus', 'Monster Hunter']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Executioner': ['Death Dealer', 'True Shot', 'Weapons Adept', 'Nightward Hunter']
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'Underworld Reaper': ['Executioner']
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'reaper_tree')
dot.render(output_path, view=True)