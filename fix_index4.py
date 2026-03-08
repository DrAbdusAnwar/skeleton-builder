import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix lower legs to be properly mirrored
# Left Lower Leg
l_leg_vb = "30 100 20 80"
l_leg_path = "M40 100 L50 100 L50 180 L30 180 L30 170 L40 170 Z"
# Right Lower Leg
r_leg_vb = "50 100 20 80"
r_leg_path = "M50 100 L60 100 L60 170 L70 170 L70 180 L50 180 Z"

def replace_svg(bone_id, new_vb, new_path):
    global html
    # Replace in draggable-bone
    re_str = rf'(<div class="draggable-bone" id="bone-{bone_id}">.*?<svg viewBox=").*?(" class="bone-svg">.*?<path.*?d=").*?(".*?/>.*?</svg>.*?</div>)'
    match = re.search(re_str, html, re.DOTALL)
    if match:
        html = html.replace(match.group(0), match.group(1) + new_vb + match.group(2) + new_path + match.group(3))
    else:
        print("Not found", bone_id)

    # Replace in bone-outline
    re_str = rf'(<div class="bone-outline" id="outline-{bone_id}">.*?<svg viewBox=").*?(" class="bone-svg faint-outline">.*?<path.*?d=").*?(".*?/>.*?</svg>.*?</div>)'
    match = re.search(re_str, html, re.DOTALL)
    if match:
        html = html.replace(match.group(0), match.group(1) + new_vb + match.group(2) + new_path + match.group(3))
    else:
        print("Not found outline", bone_id)

replace_svg("left-lower-leg", l_leg_vb, l_leg_path)
replace_svg("right-lower-leg", r_leg_vb, r_leg_path)

with open('index.html', 'w') as f:
    f.write(html)
