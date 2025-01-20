#!/bin/bash
scene_files=("coppersmith.py" "lattice_attacks.py" "misc_scenes.py" "utils.py" "ecdsa.py" "intro_to_lattices.py" "learning_with_errors.py" "lll_visualization.py" "knapsack.py" "truncated_lcg.py")

for file in "${scene_files[@]}"; do
    manim "$file" -a
done