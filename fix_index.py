import re

with open('index.html', 'r') as f:
    html = f.read()

# Swap Left and Right Arm paths and viewBoxes
left_arm_re = r'(<div class="draggable-bone" id="bone-left-arm">.*?<svg viewBox=")(.*?)(" class="bone-svg">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'
right_arm_re = r'(<div class="draggable-bone" id="bone-right-arm">.*?<svg viewBox=")(.*?)(" class="bone-svg">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'

left_arm_match = re.search(left_arm_re, html, re.DOTALL)
right_arm_match = re.search(right_arm_re, html, re.DOTALL)

left_arm_vb, left_arm_path = left_arm_match.group(2), left_arm_match.group(4)
right_arm_vb, right_arm_path = right_arm_match.group(2), right_arm_match.group(4)

html = html.replace(left_arm_match.group(0), left_arm_match.group(1) + right_arm_vb + left_arm_match.group(3) + right_arm_path + left_arm_match.group(5))
html = html.replace(right_arm_match.group(0), right_arm_match.group(1) + left_arm_vb + right_arm_match.group(3) + left_arm_path + right_arm_match.group(5))

# Also swap for outline
o_left_arm_re = r'(<div class="bone-outline" id="outline-left-arm">.*?<svg viewBox=")(.*?)(" class="bone-svg faint-outline">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'
o_right_arm_re = r'(<div class="bone-outline" id="outline-right-arm">.*?<svg viewBox=")(.*?)(" class="bone-svg faint-outline">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'

o_left_arm_match = re.search(o_left_arm_re, html, re.DOTALL)
o_right_arm_match = re.search(o_right_arm_re, html, re.DOTALL)

html = html.replace(o_left_arm_match.group(0), o_left_arm_match.group(1) + right_arm_vb + o_left_arm_match.group(3) + right_arm_path + o_left_arm_match.group(5))
html = html.replace(o_right_arm_match.group(0), o_right_arm_match.group(1) + left_arm_vb + o_right_arm_match.group(3) + left_arm_path + o_right_arm_match.group(5))

# Swap Left and Right Thigh paths and viewBoxes
left_thigh_re = r'(<div class="draggable-bone" id="bone-left-thigh">.*?<svg viewBox=")(.*?)(" class="bone-svg">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'
right_thigh_re = r'(<div class="draggable-bone" id="bone-right-thigh">.*?<svg viewBox=")(.*?)(" class="bone-svg">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'

left_thigh_match = re.search(left_thigh_re, html, re.DOTALL)
right_thigh_match = re.search(right_thigh_re, html, re.DOTALL)

left_thigh_vb, left_thigh_path = left_thigh_match.group(2), left_thigh_match.group(4)
right_thigh_vb, right_thigh_path = right_thigh_match.group(2), right_thigh_match.group(4)

html = html.replace(left_thigh_match.group(0), left_thigh_match.group(1) + right_thigh_vb + left_thigh_match.group(3) + right_thigh_path + left_thigh_match.group(5))
html = html.replace(right_thigh_match.group(0), right_thigh_match.group(1) + left_thigh_vb + right_thigh_match.group(3) + left_thigh_path + right_thigh_match.group(5))

# Also swap for outline
o_left_thigh_re = r'(<div class="bone-outline" id="outline-left-thigh">.*?<svg viewBox=")(.*?)(" class="bone-svg faint-outline">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'
o_right_thigh_re = r'(<div class="bone-outline" id="outline-right-thigh">.*?<svg viewBox=")(.*?)(" class="bone-svg faint-outline">.*?<path d=")(.*?)(" />.*?</svg>.*?</div>)'

o_left_thigh_match = re.search(o_left_thigh_re, html, re.DOTALL)
o_right_thigh_match = re.search(o_right_thigh_re, html, re.DOTALL)

html = html.replace(o_left_thigh_match.group(0), o_left_thigh_match.group(1) + right_thigh_vb + o_left_thigh_match.group(3) + right_thigh_path + o_left_thigh_match.group(5))
html = html.replace(o_right_thigh_match.group(0), o_right_thigh_match.group(1) + left_thigh_vb + o_right_thigh_match.group(3) + left_thigh_path + o_right_thigh_match.group(5))

with open('index.html', 'w') as f:
    f.write(html)
