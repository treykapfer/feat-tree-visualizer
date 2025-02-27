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
    'Devout Servant', 'God\'s Chosen', 'Masochist', 'Monster Hunter', 'Vanguard', 'Weapon Initiate', 'Arcanist'
]
for feat in tier_0_feats:
    dot.node(feat, feat)

# Tier 1 Feats
tier_1_feats = {
    'Hallowed Keeper': ['Devout Servant'],
    'Inquisitor': ['Monster Hunter'],
    'Martyr': ['Vanguard', 'Masochist'],
    'Seer of Realms Beyond': ['Arcanist'],
    'Ward Weaver': ['Devout Servant', 'Arcanist']
}
for feat, requirements in tier_1_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 2 Feats
tier_2_feats = {
    'Wielder of the Holy Light': ['Hallowed Keeper', 'God\'s Chosen'],
    'Weapons Adept': ['Weapon Initiate'],
    'Ancient Protector': ['Ward Weaver', 'God\'s Chosen', 'Hallowed Keeper']
}
for feat, requirements in tier_2_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 3 Feats
tier_3_feats = {
    'Bane of Monsters': ['Weapons Adept', 'Inquisitor', 'Wielder of the Holy Light'],
    'Realmwalker': ['Ancient Protector', 'Seer of Realms Beyond']
}
for feat, requirements in tier_3_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Tier 4 Feats
tier_4_feats = {
    'Holy Guardian': ['Bane of Monsters', 'Martyr', 'Wielder of the Holy Light'],
    'Pact of the Watcher': ['Wielder of the Holy Light', 'Realmwalker']
}
for feat, requirements in tier_4_feats.items():
    dot.node(feat, feat)
    for req in requirements:
        dot.edge(req, feat)

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'guardian_tree')
dot.render(output_path, view=True)