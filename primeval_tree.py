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
    'Arcanist', 'Clairvoyant', 'Bloodmage', 
    'Beast Whisperer', 'Vampire Traditionalist', 'Cannibal',
    'Sadist', 'Serial Killer'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Dammerskript Initiate': ['Arcanist', 'Bloodmage'],
    'Grafi Initiate': ['Arcanist', 'Clairvoyant'],
    'Seer of Realms Beyond': ['Arcanist', 'Clairvoyant'],
    'Ward Weaver': ['Arcanist', 'Bloodmage', 'Clairvoyant'],
    'Dreadmonger': ['Cannibal', 'Sadist', 'Serial Killer'],
    'Shapechanger': ['Beast Whisperer', 'Vampire Traditionalist']
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Dammermancer': ['Dammerskript Initiate'],
    'Grafimancer': ['Grafi Initiate'],
    'Ancient Protector': ['Clairvoyant', 'Ward Weaver'],
    'Blood Chieftain': ['Bloodmage', 'Dreadmonger', 'Dammerskript Initiate']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Primordial Acolyte': ['Blood Chieftain', 'Ancient Protector', 'Dammermancer', 'Grafimancer'],
    'Master of the Wild Hunt': ['Ancient Protector', 'Shapechanger'],
    'Realmwalker': ['Seer of Realms Beyond', 'Blood Chieftain', 'Ancient Protector']
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'Pact of the Damned': ['Primordial Acolyte', 'Realmwalker'],
    'Primordial Power': ['Primordial Acolyte', 'Master of the Wild Hunt']
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'primeval_tree')
dot.render(output_path, view=True)