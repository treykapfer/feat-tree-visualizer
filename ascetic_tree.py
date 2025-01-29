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
    'Brawler', 'Clairvoyant', 'Eagle Eye', 'Honed Discipline', 'Iron Will',
    'Masochist', 'Psychic Awakening', 'Undead Vigor'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Lethal Focus': ['Honed Discipline', 'Eagle Eye'],
    'Psionic Adept': ['Psychic Awakening'],
    'Stoic State': ['Iron Will'],
    'Martial Artist': ['Brawler'],
    'Acolyte of Pain': ['Masochist', 'Honed Discipline', 'Iron Will'],
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Iron Fist': ['Martial Artist', 'Honed Discipline', 'Iron Will'],
    'Covenant of Lamentation': ['Acolyte of Pain','Clairvoyant','Psychic Awakening'],
    'Mind Mage': ['Psionic Adept'],
    'Third Eye Opened': ['Psychic Awakening', 'Lethal Focus'],
    'Inner Sanctum': ['Psychic Awakening', 'Stoic State'],
    'Aura of Unlife': ['Undead Vigor'],
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Scion of the Rack': ['Covenant of Lamentation', 'Iron Fist'],
    'Psychic Mastery': ['Mind Mage']
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 (Ultimate Feats)
tier_4_feats = {
    'The Final Mantra': ['Scion of the Rack', 'Aura of Unlife', 'Acolyte of Pain', 'Lethal Focus'],
    'Astral Awakening': ['Psychic Mastery', 'Third Eye Opened', 'Inner Sanctum'],
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'ascetic_tree')
dot.render(output_path, view=True)