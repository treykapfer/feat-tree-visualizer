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
    'Arcanist', 'Bloodmage', 'Clairvoyant', 'Devout Servant',
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Dammerskript Initiate': ['Arcanist', 'Bloodmage'],
    'Grafi Initiate': ['Arcanist', 'Clairvoyant'],
    'Ohrskript Initiate': ['Arcanist', 'Devout Servant'],
    'Seer of Realms Beyond': ['Arcanist', 'Clairvoyant'],
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Dammermancer': ['Dammerskript Initiate'],
    'Grafimancer': ['Grafi Initiate'],
    'Ohromancer': ['Ohrskript Initiate'],
    'Archcaster': ['Dammerskript Initiate', 'Grafi Initiate', 'Ohrskript Initiate'],
    'Spellmonger': ['Dammerskript Initiate', 'Grafi Initiate', 'Ohrskript Initiate'],
    'Blood Chieftain': ['Bloodmage', 'Dammerskript Initiate'],
    'Covenant of Lamentation': ['Seer of Realms Beyond', 'Clairvoyant']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Dammerskript Mastery': ['Dammermancer', 'Archcaster'],
    'Grafi Mastery': ['Grafimancer', 'Archcaster'],
    'Ohrskript Mastery': ['Ohromancer', 'Archcaster'],
    'Realmwalker': ['Blood Chieftain', 'Spellmonger', 'Covenant of Lamentation', 'Seer of Realms Beyond'],
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'Pact of the Djinn': ['Realmwalker', 'Grafi Mastery', 'Ohrskript Mastery'],
    'Demonic Pact': ['Realmwalker', 'Dammerskript Mastery'],
    'Hexed Sovereign': [ 'Grafi Mastery', 'Ohrskript Mastery', 'Dammerskript Mastery']
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'mage_tree')
dot.render(output_path, view=True)