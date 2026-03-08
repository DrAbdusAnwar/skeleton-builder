import re

with open('index.html', 'r') as f:
    html = f.read()

def replace_svg(bone_id, new_vb, new_path):
    global html
    # Replace in draggable-bone
    re_str = rf'(<div class="draggable-bone" id="bone-{bone_id}">.*?<svg viewBox=").*?(" class="bone-svg">.*?<path.*?d=").*?(".*?/>.*?</svg>.*?</div>)'
    match = re.search(re_str, html, re.DOTALL)
    if match:
        html = html.replace(match.group(0), match.group(1) + new_vb + match.group(2) + new_path + match.group(3))

    # Replace in bone-outline
    re_str = rf'(<div class="bone-outline" id="outline-{bone_id}">.*?<svg viewBox=").*?(" class="bone-svg faint-outline">.*?<path.*?d=").*?(".*?/>.*?</svg>.*?</div>)'
    match = re.search(re_str, html, re.DOTALL)
    if match:
        html = html.replace(match.group(0), match.group(1) + new_vb + match.group(2) + new_path + match.group(3))


r_arm_vb = "29.5 10 30.5 90"
replace_svg("right-arm", r_arm_vb, "M40 10 C30 10 25 20 35 30 L50 60 L50 100 L60 100 L60 60 L45 30 C55 20 50 10 40 10 Z")

l_thigh_vb = "38 10 24 90"
replace_svg("left-thigh", l_thigh_vb, "M50 10 C60 10 65 20 60 30 L50 80 L50 100 L40 100 L40 30 C35 20 40 10 50 10 Z")

r_thigh_vb = "38 10 24 90"
replace_svg("right-thigh", r_thigh_vb, "M50 10 C40 10 35 20 40 30 L50 80 L50 100 L60 100 L60 30 C65 20 60 10 50 10 Z")

with open('index.html', 'w') as f:
    f.write(html)
