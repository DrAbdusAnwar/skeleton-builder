from svgpathtools import parse_path
left_arm = parse_path('M60 10 C70 10 75 20 65 30 L50 60 L50 100 L40 100 L40 60 L55 30 C45 20 50 10 60 10 Z')
print("Left Arm:", left_arm.bbox())

right_arm = parse_path('M20 10 C10 10 5 20 15 30 L30 60 L30 100 L40 100 L40 60 L25 30 C35 20 30 10 20 10 Z')
print("Right Arm:", right_arm.bbox())

ribcage = parse_path('M45 10 H55 V100 H45 Z M45 20 C20 15 15 35 45 40 V35 C20 30 25 20 45 25 Z M55 20 C80 15 85 35 55 40 V35 C80 30 75 20 55 25 Z M45 45 C20 40 15 60 45 65 V60 C20 55 25 45 45 50 Z M55 45 C80 40 85 60 55 65 V60 C80 55 75 45 55 50 Z M45 70 C20 65 15 85 45 90 V85 C20 80 25 70 45 75 Z M55 70 C80 65 85 85 55 90 V85 C80 80 75 70 55 75 Z')
print("Ribcage:", ribcage.bbox())
