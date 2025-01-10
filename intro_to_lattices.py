from manim import *
from manim_slides import Slide

class LatticeDefinition(Slide):
    
    def construct(self):
        title = Text("What is a lattice?").set_color(YELLOW)
        basis = Tex("$\\textbf{B} = (\\mathbf{b_1}, \\mathbf{b_2}, \\ldots, \\mathbf{b_n})$ where $\\mathbf{b_i} \\in \\mathbb{R}^{n}$")
        lattice_def = Tex("$\\mathcal{L} = a_1 \\cdot \\mathbf{b_1} + a_2 \\cdot \\mathbf{b_2} + \\ldots + a_n \\cdot \\mathbf{b_n}$ where $a_i \\in \\mathbb{Z}$")

        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.to_edge(UP))
        self.play(Write(basis))
        self.next_slide()

        self.play(basis.animate.move_to(UP))
        self.play(Write(lattice_def))
        self.next_slide()

        self.play(FadeOut(title))
        self.play(basis.animate.scale(2/3).to_corner(UL), lattice_def.animate.scale(2/3).to_corner(UL).shift(2/3 * DOWN))

        # 2D definitions
        basis_2d = Tex("$\\textbf{B} = (\\mathbf{b_1}, \\mathbf{b_2})$ where $\\mathbf{b_i} \\in \\mathbb{R}^{n}$").scale(2/3).to_corner(UL)
        lattice_def_2d = Tex("$\\mathcal{L} = a_1 \\cdot \\mathbf{b_1} + a_2 \\cdot \\mathbf{b_2}$ where $a_i \\in \\mathbb{Z}$").scale(2/3).to_corner(UL).shift(2/3 * DOWN)
        
        # Rectangle surrounding the defs
        def_rect = SurroundingRectangle(Group(basis_2d, lattice_def_2d), corner_radius=0.25, buff=MED_SMALL_BUFF)
        def_rect_background = BackgroundRectangle(def_rect, fill_opacity=1, color=BLACK)
        def_rect_group = VGroup(def_rect_background, def_rect, basis_2d, lattice_def_2d)
        
        self.play(Transform(basis, basis_2d), Transform(lattice_def, lattice_def_2d))
        self.add_foreground_mobject(def_rect_group)
        
        # Draw a 2D lattice 
        plane = NumberPlane()

        b1_pos = np.array((-0.2, 0.6, 0))
        b2_pos = np.array((1, 0, 0))

        b1 = Arrow(start=ORIGIN, end=b1_pos, buff=0).set_color(RED)
        b2 = Arrow(start=ORIGIN, end=b2_pos, buff=0).set_color(GREEN)
        b1_text = Tex("$b_1$").next_to(b1.get_end(), LEFT).set_color(RED)
        b2_text = Tex("$b_2$").next_to(b2.get_end() + RIGHT/3, UP).set_color(GREEN)

        self.play(FadeIn(plane))
        self.play(GrowArrow(b1), GrowArrow(b2), Write(b1_text), Write(b2_text))
        self.next_slide()

        # show the fundamental paralellogram
        parallelogram = Polygon(
            ORIGIN, b2_pos, b1_pos + b2_pos, b1_pos,
            color=BLUE, fill_opacity=0.5
        )
        parallelogram_text = Tex("$\\mathcal{P}(\\mathbf{B})$").scale(2/3).move_to(parallelogram)

        self.play(Create(parallelogram))
        self.play(Write(parallelogram_text))
        self.next_slide()

        # visualize integer linear combinations of the basis
        # b1 + b2, b1 + 2*b2
        goal_pos = 2*b1_pos + 4*b2_pos
        goal_pos += np.array((0.3, -0.1, 0)) # small displacement
        goal_dot = Dot(goal_pos, color=PURE_RED)
        goal_label = Tex("$2\\mathbf{b_1} + 4\\mathbf{b_2}$", color=YELLOW).move_to(2*b1_pos + 4*b2_pos + UP/2)
        goal_label_2 = Tex("$14\\mathbf{b_1} - 10\\mathbf{b_2}$", color=YELLOW).move_to(2*b1_pos + 4*b2_pos + UR/2)

        lll_arrows = self.create_arrow_chain([b1_pos, 2*b1_pos, 2*b1_pos+b2_pos, 2*b1_pos+2*b2_pos, 2*b1_pos+3*b2_pos, 2*b1_pos+4*b2_pos], [RED] + [GREEN]*4)

        self.play(FadeOut(parallelogram), Unwrite(parallelogram_text))
        self.play(Create(goal_dot))
        self.add_foreground_mobject(goal_dot)
        self.next_slide()

        # it's easy to reach a point with "good" bases
        self.play(LaggedStartMap(FadeIn, lll_arrows, lag_ratio=0.5))
        self.play(Write(goal_label))
        self.next_slide()

        # visualize all the points on the lattice
        dots = []

        for i in range(-20, 20):
            for j in range(-20, 20):
                dots.append(Dot(i*b1_pos + j*b2_pos))    
        
        # hide texts
        self.play(Unwrite(b1_text), Unwrite(b2_text), Unwrite(goal_label))
        self.play(LaggedStartMap(FadeIn, dots, shift=0.5 * DOWN, lag_ratio=0.01))
        self.next_slide()

        # fade out the old vectors
        # show that different bases might lead to the same lattice
        b3_pos = 3*b1_pos + b2_pos
        b4_pos = 4*b1_pos + b2_pos
        
        b3 = Arrow(start=ORIGIN, end=b3_pos, buff=0).set_color(RED)
        b4 = Arrow(start=ORIGIN, end=b4_pos, buff=0).set_color(GREEN)

        self.play(FadeOut(b1), FadeOut(b2), *map(FadeOut, lll_arrows))
        self.play(GrowArrow(b3), GrowArrow(b4))
        self.next_slide()

        # goal = 14*b3 - 10*b4
        chain_positions = []
        chain_colors = []

        # zigzag
        for i in range(5):
            chain_positions.append((i+1)*b3_pos - i*b4_pos)
            chain_positions.append((i+1)*b3_pos - (i+1)*b4_pos)
            chain_colors += [GREEN, RED]
        
        # straight up
        for i in range(5, 7):
            chain_positions.append((i+1)*b3_pos - 5*b4_pos)
            chain_colors.append(RED)
        
        # zigzag
        for i in range(5, 10):
            chain_positions.append((i+3)*b3_pos - i*b4_pos)
            chain_positions.append((i+3)*b3_pos - (i+1)*b4_pos)
            chain_colors += [GREEN, RED]
        
        # straight up
        for i in range(10, 12):
            chain_positions.append((i+3)*b3_pos - 10*b4_pos)
            chain_colors.append(RED)

        long_chain = self.create_arrow_chain(chain_positions, chain_colors)
        
        self.play(LaggedStartMap(FadeIn, long_chain, lag_ratio=0.5))
        self.next_slide()

        # remove lattice points
        self.play(FadeOut(b4), LaggedStartMap(FadeOut, dots, shift=0.5 * DOWN, lag_ratio=0.01))
        self.play(Write(goal_label_2))

    
    def create_arrow_chain(self, positions, colors):
        arrows = []
        prev_point = positions[0]

        for pos, color in zip(positions[1:], colors):
            arrows.append(Arrow(start=prev_point, end=pos, buff=0).set_color(color))
            prev_point = pos
        
        return arrows