import os

html = """<!DOCTYPE html>
<html>
<head>
<style>
svg { width: 100px; height: 100px; border: 1px solid red; margin: 5px; }
path { fill: #ccc; stroke: #333; }
.board { position: relative; width: 400px; height: 800px; border: 1px solid black; }
.board svg { position: absolute; border: none; margin: 0; }
</style>
</head>
<body>
<div style="display: flex; flex-wrap: wrap;">
"""

bones = {
    "skull": '<path fill-rule="evenodd" d="M50 5 C30 5 15 25 15 45 C15 65 25 75 35 80 L65 80 C75 75 85 65 85 45 C85 25 70 5 50 5 Z M30 40 A8 8 0 1 0 30 56 A8 8 0 1 0 30 40 Z M70 40 A8 8 0 1 0 70 56 A8 8 0 1 0 70 40 Z M50 60 L45 70 H55 Z" />',
    "jaw": '<path d="M35 80 C40 85 60 85 65 80 L65 95 C60 100 40 100 35 95 Z" />',
    "left-clavicle": '<path d="M45 10 C30 5 15 15 5 10 C15 5 30 0 45 5 Z" />',
    "right-clavicle": '<path d="M55 10 C70 5 85 15 95 10 C85 5 70 0 55 5 Z" />',
    "ribcage": '<path d="M45 10 H55 V100 H45 Z M45 20 C20 15 15 35 45 40 V35 C20 30 25 20 45 25 Z M55 20 C80 15 85 35 55 40 V35 C80 30 75 20 55 25 Z M45 45 C20 40 15 60 45 65 V60 C20 55 25 45 45 50 Z M55 45 C80 40 85 60 55 65 V60 C80 55 75 45 55 50 Z M45 70 C20 65 15 85 45 90 V85 C20 80 25 70 45 75 Z M55 70 C80 65 85 85 55 90 V85 C80 80 75 70 55 75 Z" />',
    "pelvis": '<path fill-rule="evenodd" d="M10 10 Q50 30 90 10 Q100 40 80 55 L65 75 L50 60 L35 75 L20 55 Q0 40 10 10 Z M25 45 A5 5 0 1 0 25 55 A5 5 0 1 0 25 45 Z M75 45 A5 5 0 1 0 75 55 A5 5 0 1 0 75 45 Z" />',
    "left-arm": '<path d="M60 10 C70 10 75 20 65 30 L50 60 L50 100 L40 100 L40 60 L55 30 C45 20 50 10 60 10 Z" />',
    "right-arm": '<path d="M40 10 C30 10 25 20 35 30 L50 60 L50 100 L60 100 L60 60 L45 30 C55 20 50 10 40 10 Z" />',
    "left-thigh": '<path d="M50 10 C60 10 65 20 60 30 L50 80 L40 80 L40 30 C35 20 40 10 50 10 Z" />',
    "right-thigh": '<path d="M50 10 C40 10 35 20 40 30 L50 80 L60 80 L60 30 C65 20 60 10 50 10 Z" />',
    "left-lower-leg": '<path d="M40 80 L50 80 L50 180 L30 180 L30 170 L40 170 Z" />',
    "right-lower-leg": '<path d="M50 80 L60 80 L60 170 L70 170 L70 180 L50 180 Z" />'
}

# The coordinates for viewBox and style
positions = {
    "skull": {"top": 100, "left": 150, "viewBox": "15 5 70 75", "width": 70, "height": 75},
    "jaw": {"top": 175, "left": 150, "viewBox": "35 80 30 20", "width": 30, "height": 20},
    "left-clavicle": {"top": 200, "left": 115, "viewBox": "0 0 50 20", "width": 50, "height": 20},
    "right-clavicle": {"top": 200, "left": 165, "viewBox": "50 0 50 20", "width": 50, "height": 20},
    "ribcage": {"top": 210, "left": 150, "viewBox": "15 10 70 90", "width": 70, "height": 90},
    "left-arm": {"top": 210, "left": 115, "viewBox": "40 10 35 90", "width": 35, "height": 90},
    "right-arm": {"top": 210, "left": 220, "viewBox": "25 10 35 90", "width": 35, "height": 90},
    "pelvis": {"top": 300, "left": 140, "viewBox": "5 10 90 65", "width": 90, "height": 65},
    "left-thigh": {"top": 355, "left": 140, "viewBox": "30 10 40 70", "width": 40, "height": 70},
    "right-thigh": {"top": 355, "left": 190, "viewBox": "30 10 40 70", "width": 40, "height": 70},
    "left-lower-leg": {"top": 425, "left": 140, "viewBox": "30 80 40 100", "width": 40, "height": 100},
    "right-lower-leg": {"top": 425, "left": 190, "viewBox": "30 80 40 100", "width": 40, "height": 100},
}

for name, path in bones.items():
    html += f'<div style="text-align: center;"><div>{name}</div><svg viewBox="{positions[name]["viewBox"]}">{path}</svg></div>\n'

html += '</div>\n'
html += '<div class="board">\n'

for name, path in bones.items():
    p = positions[name]
    html += f'<svg viewBox="{p["viewBox"]}" style="top: {p["top"]}px; left: {p["left"]}px; width: {p["width"]}px; height: {p["height"]}px;">{path}</svg>\n'

html += '</div></body></html>'

with open('test_bones.html', 'w') as f:
    f.write(html)
