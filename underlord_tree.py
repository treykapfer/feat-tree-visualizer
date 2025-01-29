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
    'Arcanist', 'Seasoned Performer', 'Fury of Fang & Claw', 
    'Psychic Awakening', 'Socialite'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Spider': ['Socialite'],
    'Dammerskript Initiate': ['Arcanist'],
    'Grafi Initiate': ['Arcanist'],
    'Ohrskript Initiate': ['Arcanist'],
    'Aspiring Alpha': ['Socialite'],
    'Psionic Adept': ['Psychic Awakening'],
    'Showstopper': ['Seasoned Performer']
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Thrall Keeper': ['Psionic Adept'],
    'Mind Mage': ['Psionic Adept'],
    'Spellmonger': ['Dammerskript Initiate', 'Grafi Initiate', 'Ohrskript Initiate'],
    'Wielder of the Inner Flame': ['Fury of Fang & Claw']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Rising Underlord': ['Spider', 'Spellmonger', 'Showstopper', 'Thrall Keeper', 'Aspiring Alpha', 'Wielder of the Inner Flame'],
    'Psychic Mastery': ['Mind Mage']
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'Reviled Underlord': ['Rising Underlord'],
    'Vampire Bloodlord': ['Rising Underlord', 'Psychic Mastery'],
    'Ascended Alpha': ['Rising Underlord'],
    'Coven Mother': ['Rising Underlord'],
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'underlord_tree')
dot.render(output_path, view=True)