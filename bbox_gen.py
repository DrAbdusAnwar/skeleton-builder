from svgpathtools import parse_path, wsvg
import sys

def bbox(path_str):
    if not path_str:
        return (0, 0, 0, 0)
    p = parse_path(path_str)
    return p.bbox()

bones = {
    "skull": 'M50 5 C30 5 15 25 15 45 C15 65 25 75 35 80 L65 80 C75 75 85 65 85 45 C85 25 70 5 50 5 Z M30 40 A8 8 0 1 0 30 56 A8 8 0 1 0 30 40 Z M70 40 A8 8 0 1 0 70 56 A8 8 0 1 0 70 40 Z M50 60 L45 70 H55 Z',
    "jaw": 'M35 80 C40 85 60 85 65 80 L65 95 C60 100 40 100 35 95 Z',
    "left-clavicle": 'M45 10 C30 5 15 15 5 10 C15 5 30 0 45 5 Z',
    "right-clavicle": 'M55 10 C70 5 85 15 95 10 C85 5 70 0 55 5 Z',
    "ribcage": 'M45 10 H55 V100 H45 Z M45 20 C20 15 15 35 45 40 V35 C20 30 25 20 45 25 Z M55 20 C80 15 85 35 55 40 V35 C80 30 75 20 55 25 Z M45 45 C20 40 15 60 45 65 V60 C20 55 25 45 45 50 Z M55 45 C80 40 85 60 55 65 V60 C80 55 75 45 55 50 Z M45 70 C20 65 15 85 45 90 V85 C20 80 25 70 45 75 Z M55 70 C80 65 85 85 55 90 V85 C80 80 75 70 55 75 Z',
    "pelvis": 'M10 10 Q50 30 90 10 Q100 40 80 55 L65 75 L50 60 L35 75 L20 55 Q0 40 10 10 Z M25 45 A5 5 0 1 0 25 55 A5 5 0 1 0 25 45 Z M75 45 A5 5 0 1 0 75 55 A5 5 0 1 0 75 45 Z',
    "left-arm": 'M60 10 C70 10 75 20 65 30 L50 60 L50 100 L40 100 L40 60 L55 30 C45 20 50 10 60 10 Z',
    "right-arm": 'M40 10 C30 10 25 20 35 30 L50 60 L50 100 L60 100 L60 60 L45 30 C55 20 50 10 40 10 Z',
    "left-thigh": 'M50 10 C60 10 65 20 60 30 L50 80 L50 100 L40 100 L40 30 C35 20 40 10 50 10 Z',
    "right-thigh": 'M50 10 C40 10 35 20 40 30 L50 80 L50 100 L60 100 L60 30 C65 20 60 10 50 10 Z',
    "left-lower-leg": 'M40 100 L50 100 L50 180 L30 180 L30 170 L40 170 Z',
    "right-lower-leg": 'M50 100 L60 100 L60 170 L70 170 L70 180 L50 180 Z'
}

for name, path in bones.items():
    xmin, xmax, ymin, ymax = bbox(path)
    width = xmax - xmin
    height = ymax - ymin
    print(f'"{name}": {{"viewBox": "{xmin} {ymin} {width} {height}"}},')
