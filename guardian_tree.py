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
dot.node('Devout Servant', 'Devout Servant')
dot.node('God\'s Chosen', 'God\'s Chosen')
dot.node('Masochist', 'Masochist')
dot.node('Monster Hunter', 'Monster Hunter')
dot.node('Vanguard', 'Vanguard')
dot.node('Weapon Initiate', 'Weapon Initiate')

# Tier 1 Feats
dot.node('Hallowed Keeper', 'Hallowed Keeper')
dot.node('Inquisitor', 'Inquisitor')
dot.node('Martyr', 'Martyr')

# Tier 2 Feats
dot.node('Wielder of the Holy Light', 'Wielder of the Holy Light')
dot.node('Weapons Adept', 'Weapons Adept')

# Tier 3 Feats
dot.node('Bane of Monsters', 'Bane of Monsters')

# Tier 4 Feats
dot.node('Holy Guardian', 'Holy Guardian')

# Add edges (prerequisites)
# Tier 0 -> Tier 1
dot.edge('Devout Servant', 'Hallowed Keeper')
dot.edge('Monster Hunter', 'Inquisitor')
dot.edge('Vanguard', 'Martyr')
dot.edge('Masochist', 'Martyr')

# Tier 1 -> Tier 2
dot.edge('Hallowed Keeper', 'Wielder of the Holy Light')
dot.edge('God\'s Chosen', 'Wielder of the Holy Light')
dot.edge('Weapon Initiate', 'Weapons Adept')

# Tier 2 -> Tier 3
dot.edge('Weapons Adept', 'Bane of Monsters')
dot.edge('Inquisitor', 'Bane of Monsters')
dot.edge('Wielder of the Holy Light', 'Bane of Monsters')

# Tier 3 -> Tier 4
dot.edge('Bane of Monsters', 'Holy Guardian')
dot.edge('Martyr', 'Holy Guardian')
dot.edge('Wielder of the Holy Light', 'Holy Guardian')

# Save and render the graph into the "exports" folder
output_path = os.path.join(exports_folder, 'guardian_tree')
dot.render(output_path, view=True)