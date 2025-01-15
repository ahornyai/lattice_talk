from manim import Arrow

def create_arrow_chain(positions, colors):
    arrows = []
    prev_point = positions[0]

    for pos, color in zip(positions[1:], colors):
        arrows.append(Arrow(start=prev_point, end=pos, buff=0).set_color(color))
        prev_point = pos
    
    return arrows