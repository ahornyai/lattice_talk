from manim import *
from manim_slides import Slide

class LLLIntroduction(Slide):
    
    def construct(self):
        title = Text("The Lenstra-Lenstra-Lovász algorithm").set_color(YELLOW)
        basis = Tex("$\\textbf{B} = (\\mathbf{b_1}, \\mathbf{b_2}, \\ldots, \\mathbf{b_n})$").set_color(GREEN)
        gs_basis = Tex("Gram-Schmidt Ortogonalized $\\textbf{Q} = (\\mathbf{q_1}, \\mathbf{q_2}, \\ldots, \\mathbf{q_n})$").set_color(RED)
        working_basis = Tex("Number of the working basis vectors $k$")

        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.to_edge(UP))
        self.play(Write(basis))
        self.next_slide()

        self.play(basis.animate.move_to(UP))
        self.play(Write(gs_basis))
        self.next_slide()

        self.play(basis.animate.move_to(2*UP), gs_basis.animate.move_to(UP))
        self.play(Write(working_basis))
        self.next_slide()

        rendered_code = Code("assets/lll_implementation_example.py", style="github-dark", insert_line_no=False).scale(0.7).next_to(title, DOWN)

        self.play(FadeOut(basis), FadeOut(gs_basis), FadeOut(working_basis))
        self.play(FadeIn(rendered_code))
        self.next_slide()

        self.play(rendered_code.animate.align_on_border(LEFT))

        size_cond_rectangle = SurroundingRectangle(rendered_code.code[12:15], buff=MED_SMALL_BUFF).set_fill(YELLOW).set_opacity(0).stretch_to_fit_width(rendered_code.background_mobject.get_width()).align_to(rendered_code.background_mobject, LEFT)
        lovasz_condition_group = SurroundingRectangle(rendered_code.code[18:19], buff=MED_SMALL_BUFF).set_fill(YELLOW).set_opacity(0).stretch_to_fit_width(rendered_code.background_mobject.get_width()).align_to(rendered_code.background_mobject, LEFT)

        # explain size condition
        mu_def = Tex("$\\mu_{i, j} = \\frac{\\mathbf{b_i} \\cdot \\mathbf{q_j}}{\\mathbf{q_j} \\cdot \\mathbf{q_j}}$").scale(0.6).next_to(rendered_code.background_mobject, UR).shift(DOWN)
        size_condition_def = Tex("I. Size condition: $|\\mu_{i, j}| \\leq 0.5$").scale(0.6).next_to(rendered_code.background_mobject, UR).shift(DOWN + DOWN*0.6)
        size_condition_def_ending = Tex("for $0 \\leq j < i \\leq n $").scale(0.6).next_to(rendered_code.background_mobject, UR).shift(DOWN + DOWN*0.6 + DOWN*0.4)

        # explain Lovasz-condition
        lovasz_condition_label = Tex("II. Lovász-condition:").scale(0.6).next_to(rendered_code.background_mobject, UR).shift(DOWN + 2*DOWN*0.6 + DOWN*0.4)
        lovasz_condition_def = Tex("$\\lVert q_k \\rVert^2 \\geq (\\delta - \\mu_{k, k-1}^2) \\cdot \\lVert q_{k-1} \\rVert^2$").scale(0.6).next_to(rendered_code.background_mobject, UR).shift(DOWN + 2*DOWN*0.6 + DOWN*0.4 + DOWN*0.5)

        self.add(size_cond_rectangle, lovasz_condition_group)
        self.play(size_cond_rectangle.animate.set_opacity(0.3))
        self.play(Write(mu_def), Write(size_condition_def), Write(size_condition_def_ending))
        self.next_slide()

        self.play(size_cond_rectangle.animate.set_opacity(0), lovasz_condition_group.animate.set_opacity(0.3))
        self.play(Write(lovasz_condition_label), Write(lovasz_condition_def))

class LLLVisualization(Slide):
        
    def construct(self):
        # Draw a 2D lattice 
        plane = NumberPlane(background_line_style={
            "stroke_opacity": 0
        })

        b0_pos = 3*np.array((-0.2, 0.6, 0)) + np.array((1, 0, 0))
        b1_pos = 4*np.array((-0.2, 0.6, 0)) + np.array((1, 0, 0))
        
        b0 = Arrow(start=ORIGIN, end=b0_pos, buff=0).set_color(GREEN)
        b1 = Arrow(start=ORIGIN, end=b1_pos, buff=0).set_color(YELLOW)

        b0_label = Tex("$b_0 = $").scale(0.8).to_edge(UL).set_color(GREEN)
        b0_matrix = Matrix(np.transpose([[round(b0_pos[0], 2), round(b0_pos[1], 2)]])).scale(0.8).next_to(b0_label, RIGHT).set_color(GREEN)

        b1_label = Tex("$b_1 = $").scale(0.8).next_to(b0_matrix, RIGHT).shift(0.2*RIGHT).set_color(YELLOW)
        b1_matrix = Matrix(np.transpose([[round(b1_pos[0], 2), round(b1_pos[1], 2)]])).scale(0.8).next_to(b1_label, RIGHT).set_color(YELLOW)

        self.play(FadeIn(plane))
        self.play(GrowArrow(b0), GrowArrow(b1), Write(b0_label), Write(b0_matrix), Write(b1_label), Write(b1_matrix))
        self.next_slide()

        gs = [
            [
                np.array((2/5, 9/5, 0)), # b0
                np.array((-27/85, 6/85, 0)) # b1
            ],
            [
                np.array((-1/5, 3/5, 0)), # b0
                np.array((9/10, 3/10, 0)) # b1
            ]
        ]

        q0 = Arrow(start=ORIGIN, end=gs[0][0], buff=0).set_color(RED)
        q1 = Arrow(start=ORIGIN, end=gs[0][1], buff=0).set_color(RED)

        q0_label = Tex("$q_0 = $").scale(0.8).to_edge(UL).shift(2*DOWN).set_color(RED)
        q0_matrix = Matrix(np.transpose([[round(gs[0][0][0], 2), round(gs[0][0][1], 2)]])).scale(0.8).next_to(q0_label, RIGHT).set_color(RED)

        q1_label = Tex("$q_1 = $").scale(0.8).next_to(q0_matrix, RIGHT).shift(0.2*RIGHT).set_color(RED)
        q1_matrix = Matrix(np.transpose([[round(gs[0][1][0], 2), round(gs[0][1][1], 2)]])).scale(0.8).next_to(q1_label, RIGHT).set_color(RED)

        self.play(GrowArrow(q0), GrowArrow(q1), Write(q0_label), Write(q0_matrix), Write(q1_label), Write(q1_matrix))
        self.next_slide()

        k_label = Tex("$k = 1$").scale(0.8).to_edge(UL).shift(3*DOWN)

        self.play(Write(k_label))
        self.next_slide()

        mus = [22/17, 5/17, 5/2, -1/2]

        mu_vec = Arrow(start=ORIGIN, end=q0.get_end() * mus[0], buff=0).set_color(PURPLE)
        mu_brace = BraceBetweenPoints(ORIGIN, mu_vec.get_end())
        mu_label = mu_brace.get_text("$\\mu_{1,0} \\cdot \\mathbf{q_0} = " + str(round(mus[0], 2)) + " \\cdot \\mathbf{q_0}$")
        
        projection_vec = Arrow(start=b1.get_end(), end=mu_vec.get_end(), buff=0)
        self.play(GrowArrow(mu_vec), FadeIn(mu_brace), Write(mu_label), GrowArrow(projection_vec))
        self.next_slide()

        # update b1, since \\mu_{1,0} > 0.5, also update \\mu{1,0} and Gram-Schmidt ortogonalization (that doesn't change now)
        b1_pos = np.array((-1/5, 3/5, 0))
        b1_matrix_new = Matrix(np.transpose([[round(b1_pos[0], 2), round(b1_pos[1], 2)]])).scale(0.8).next_to(b1_label, RIGHT).set_color(YELLOW)

        current_mu = mus[1]

        mu_brace_updater = lambda b: b.become(BraceBetweenPoints(ORIGIN, mu_vec.get_end()))
        mu_label_updater = lambda b: b.become(mu_brace.get_text("$\\mu_{1,0} \\cdot \\mathbf{q_0} = " + str(round(current_mu, 2)) + " \\cdot \\mathbf{q_0}$"))

        # add updaters
        mu_brace.add_updater(mu_brace_updater)
        mu_label.add_updater(mu_label_updater)

        self.play(Transform(b1_matrix, b1_matrix_new), 
                  b1.animate.put_start_and_end_on(ORIGIN, b1_pos), 
                  mu_vec.animate.put_start_and_end_on(ORIGIN, q0.get_end() * mus[1]),
                  projection_vec.animate.put_start_and_end_on(b1_pos, q0.get_end() * mus[1]))
        self.next_slide()

        # check Lovász-condition delta=0.99
        lovasz_def = Tex("$\\lVert q_k \\rVert^2 \\geq (\\delta - \\mu_{k, k-1}^2) \\cdot \\lVert q_{k-1} \\rVert^2$").to_edge(UR)
        lovasz_subst = Tex(f"${round(9/85, 2)} \\geq (0.99 - {round(mus[1]**2, 2)}) \\cdot {round(17/5, 2)}$").move_to(lovasz_def)
        lovasz_simple = Tex(f"${round(9/85, 2)} \\geq 3.07$").set_color(RED).move_to(lovasz_subst)

        self.play(Write(lovasz_def))
        self.next_slide()

        self.play(TransformMatchingTex(lovasz_def, lovasz_subst))
        self.next_slide()

        self.play(TransformMatchingTex(lovasz_subst, lovasz_simple))
        self.next_slide()

        # hide GS and projection for clarity
        mu_brace.clear_updaters()
        mu_label.clear_updaters()

        self.play(FadeOut(q0, q1, mu_brace, mu_label, mu_vec, projection_vec, lovasz_simple))
        self.next_slide()

        # failed Lovász-condition => swap
        tmp = b1_pos
        b1_pos = b0_pos
        b0_pos = tmp

        b0_matrix_new = Matrix(np.transpose([[round(b0_pos[0], 2), round(b0_pos[1], 2)]])).scale(0.8).next_to(b0_label, RIGHT).set_color(GREEN)
        b1_matrix_new = Matrix(np.transpose([[round(b1_pos[0], 2), round(b1_pos[1], 2)]])).scale(0.8).next_to(b1_label, RIGHT).set_color(YELLOW)

        q0_matrix_new = Matrix(np.transpose([[round(gs[1][0][0], 2), round(gs[1][0][1], 2)]])).scale(0.8).next_to(q0_label, RIGHT).set_color(RED)
        q1_matrix_new = Matrix(np.transpose([[round(gs[1][1][0], 2), round(gs[1][1][1], 2)]])).scale(0.8).next_to(q1_label, RIGHT).set_color(RED)

        current_mu = mus[2]

        # update labels and positions
        self.play(Transform(b0_matrix, b0_matrix_new),
                  Transform(b1_matrix, b1_matrix_new),
                  b0.animate.put_start_and_end_on(ORIGIN, b0_pos),
                  b1.animate.put_start_and_end_on(ORIGIN, b1_pos))
        self.next_slide()

        # update GS and proj vec.
        # restore updaters
        mu_brace.add_updater(mu_brace_updater)
        mu_label.add_updater(mu_label_updater)

        self.play(FadeIn(q0, q1, mu_vec, mu_brace, mu_label, projection_vec))
        self.next_slide()
        
        self.play(Transform(q0_matrix, q0_matrix_new),
                  Transform(q1_matrix, q1_matrix_new),
                  q0.animate.put_start_and_end_on(ORIGIN, gs[1][0]),
                  q1.animate.put_start_and_end_on(ORIGIN, gs[1][1]),
                  mu_vec.animate.put_start_and_end_on(ORIGIN, gs[1][0] * current_mu),
                  projection_vec.animate.put_start_and_end_on(b1_pos, gs[1][0] * current_mu))
        self.next_slide()

        # update b1, since \\mu_{1_0} > 0.5
        b1_pos = np.array((1, 0, 0))
        b1_matrix_new = Matrix(np.transpose([[round(b1_pos[0], 2), round(b1_pos[1], 2)]])).scale(0.8).next_to(b1_label, RIGHT).set_color(YELLOW)

        current_mu = mus[3]

        self.play(Transform(b1_matrix, b1_matrix_new), 
                  b1.animate.put_start_and_end_on(ORIGIN, b1_pos), 
                  mu_vec.animate.put_start_and_end_on(ORIGIN, q0.get_end() * current_mu),
                  projection_vec.animate.put_start_and_end_on(b1_pos, q0.get_end() * current_mu))
        
        # Calculate Lovász-condition for the last time
        lovasz_subst_2 = Tex(f"${round(9/10, 2)} \\geq (0.99 - {round(current_mu**2, 2)}) \\cdot {round(2/5, 2)}$").move_to(lovasz_def)
        lovasz_simple_2 = Tex(f"${round(9/10, 2)} \\geq 0.3$").set_color(PURE_GREEN).move_to(lovasz_subst)

        self.play(Write(lovasz_def))
        self.next_slide()

        self.play(TransformMatchingTex(lovasz_def, lovasz_subst_2))
        self.next_slide()

        self.play(TransformMatchingTex(lovasz_subst_2, lovasz_simple_2))
        self.next_slide()

        new_k_label = Tex("$k = 2$").scale(0.8).to_edge(UL).shift(3*DOWN).set_color(PURE_GREEN)
        success = Tex("$k \\geq n \\Rightarrow$ LLL reduction is done").scale(0.8).next_to(lovasz_simple_2, DOWN).set_color(PURE_GREEN)
        sage_img = ImageMobject("assets/sage_2d_lll.png").scale(1.5)

        self.play(Transform(k_label, new_k_label), Write(success))
        self.next_slide()
        
        # Only show the reduced vectors
        # clear updaters
        mu_brace.clear_updaters()
        mu_label.clear_updaters()

        self.play(FadeOut(q0, q1, mu_brace, mu_label, mu_vec, projection_vec, lovasz_simple_2))
        self.next_slide()

        # show lattice points
        self.play(FadeOut(q0_label, q0_matrix, q1_label, q1_matrix, b1_label, b1_matrix, b0_label, b0_matrix, k_label, success))
        dots = []
        lll_reduced = [
            np.array((-0.2, 0.6, 0)),
            np.array((1, 0, 0))
        ]

        for i in range(-20, 20):
            for j in range(-20, 20):
                dots.append(Dot(i*lll_reduced[0] + j*lll_reduced[1]))    
        
        self.play(LaggedStartMap(FadeIn, dots, shift=0.5 * DOWN, lag_ratio=0.01))
        self.next_slide()

        self.play(FadeIn(sage_img, scale=0.5))