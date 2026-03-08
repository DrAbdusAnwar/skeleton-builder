import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix arms to be properly mirrored
# Left Arm
l_arm_vb = "40 10 35 90"
l_arm_path = "M60 10 C70 10 75 20 65 30 L50 60 L50 100 L40 100 L40 60 L55 30 C45 20 50 10 60 10 Z"

# Right Arm
r_arm_vb = "25 10 35 90"
r_arm_path = "M40 10 C30 10 25 20 35 30 L50 60 L50 100 L60 100 L60 60 L45 30 C55 20 50 10 40 10 Z"

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

replace_svg("left-arm", l_arm_vb, l_arm_path)
replace_svg("right-arm", r_arm_vb, r_arm_path)

with open('index.html', 'w') as f:
    f.write(html)
