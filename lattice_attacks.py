from manim import *
from manim_slides import Slide

from utils import create_arrow_chain

class SmallLinearSystem(Slide):

    def construct(self):
        eq_sym = Tex("$a_1 \\mathbf{v_1} + a_2 \\mathbf{v_2} + \\ldots + a_n \\mathbf{v_n} = \\mathbf{c}$").set_color(YELLOW)
        eq_3 = Tex("$a_1 \\mathbf{v_1} + a_2 \\mathbf{v_2} + a_3 \\mathbf{v_3} = \\mathbf{c}$").set_color(YELLOW).move_to(2*UP)
        eq_3_to_zero = Tex("$\\mathbf{c} - a_1 \\mathbf{v_1} - a_2 \\mathbf{v_2} - a_3 \\mathbf{v_3} = 0$").set_color(YELLOW).move_to(2*UP)

        tips = BulletedList(
            "All $a_i$ small",
            "$\\Rightarrow$ linear system with a small solution",
            "$\\mathbf{n}$ unknowns, less than $\\mathbf{n}$ equations",
            "$\\Rightarrow$ infinite solutions"
        ).scale(0.75)

        self.play(Write(eq_sym))
        self.next_slide()

        self.play(eq_sym.animate.move_to(2*UP))
        self.play(LaggedStartMap(FadeIn, tips, shift=0.5 * DOWN, lag_ratio=0.25))
        self.next_slide()

        self.play(FadeOut(tips))
        self.play(Transform(eq_sym, eq_3))
        self.next_slide()

        self.play(TransformMatchingTex(eq_sym, eq_3_to_zero))
        self.next_slide()

        B_sym = Matrix(np.transpose([["\\mathbf{c}", "-\\mathbf{v_1}", "-\\mathbf{v_2}", "-\\mathbf{v_3}"]]))

        self.play(FadeIn(B_sym))
        self.next_slide()

        eq_3_subst = Tex("$71661849286 - a_1 \\cdot 688113347 - a_2 \\cdot 722344289 - a_3 \\cdot 856896121 = 0$").scale(0.75).set_color(YELLOW).move_to(2*UP)
        B_subst = Matrix(np.transpose([["71661849286", "-688113347", "-722344289", "-856896121"]]))
        fail_img_1 = ImageMobject("assets/svp_fail_1.png").scale(1.5)
        success_img_1 = ImageMobject("assets/svp_success.png").scale(1.5)
        
        self.play(TransformMatchingTex(eq_3_to_zero, eq_3_subst))
        self.play(Transform(B_sym, B_subst))
        self.next_slide()

        self.play(FadeIn(fail_img_1, scale=0.5, lag_ratio=0.1))
        self.next_slide()

        B_subst_new = Matrix(np.hstack((np.transpose([["71661849286", "-688113347", "-722344289", "-856896121"]]), np.eye(4, dtype=np.int64))))

        self.play(FadeOut(fail_img_1))
        self.play(Transform(B_sym, B_subst_new))
        self.next_slide()

        self.play(FadeIn(success_img_1, scale=0.5, lag_ratio=0.1))

class IrisCTFSolution(Slide):

    def construct(self):
        irisctf_title = Text("IrisCTF2025 - knutsacque").set_color(YELLOW)

        self.play(Write(irisctf_title))
        self.next_slide()

        irisctf_info = BulletedList(
            "m = [(flag[0] + flag[1] * i + flag[2] * j + flag[3] * k), $\\ldots$]",
            "A = [$\\mathbf{a_1}, \\mathbf{a_2}, .., \\mathbf{a_n}$] where $\\mathbf{a_i} \\in \\mathbb{H}$",
            "$s = m_1 \\mathbf{a_1} + m_2 \\mathbf{a_2} + \\ldots + m_n \\mathbf{a_n}$",
            "What's m?"
        ).scale(0.75)

        self.play(irisctf_title.animate.move_to(3*UP))
        self.play(LaggedStartMap(FadeIn, irisctf_info, shift=0.5 * DOWN, lag_ratio=0.25))
        self.next_slide()

        quaternion_example = Tex("$\\mathbf{a_1} = a + b \\cdot i + c \\cdot j + d \\cdot k$").scale(0.8).shift(DOWN)
        quat_arrow = Arrow(start=LEFT, end=RIGHT).scale(0.8).shift(DOWN)
        quat_repr = Matrix(np.array([["a","b","c","d"],["-b","a","-d","c"],["-c","d","a","-b"],["-d","-c","b","a"]])).scale(0.8).next_to(quat_arrow, RIGHT)

        self.play(FadeOut(irisctf_info))
        self.play(Write(quaternion_example))
        self.play(quaternion_example.animate.move_to(4*LEFT + DOWN))
        self.play(GrowArrow(quat_arrow))
        self.play(FadeIn(quat_repr))
        self.next_slide()

        quaternion_flag = Tex("$m_1 = f_0 + f_1 \\cdot i + f_2 \\cdot j + f_3 \\cdot k$").scale(0.8).shift(UP)
        quat_arrow_2 = Arrow(start=LEFT, end=RIGHT).scale(0.8).shift(UP)
        quat_repr_2 = Matrix(np.array([["f_0","f_1","f_2","f_3"],["-f_1","f_0","-f_3","f_2"],["-f_2","f_3","f_0","-f_1"],["-f_3","-f_2","f_1","f_0"]])).scale(0.8).next_to(quat_arrow_2, RIGHT)

        self.play(quaternion_example.animate.shift(DOWN), quat_arrow.animate.shift(DOWN), quat_repr.animate.shift(DOWN))

        self.play(Write(quaternion_flag))
        self.play(quaternion_flag.animate.move_to(4*LEFT + UP))
        self.play(GrowArrow(quat_arrow_2))
        self.play(FadeIn(quat_repr_2))
        self.next_slide()

        result = ImageMobject("assets/quat_multiplication.png").shift(3*DOWN)

        self.play(FadeOut(quaternion_flag, quaternion_example, quat_arrow, quat_arrow_2))
        self.play(quat_repr.animate.move_to(2.25*RIGHT), quat_repr_2.animate.move_to(2.25*LEFT))
        self.play(FadeIn(result))
        self.next_slide()

        self.play(FadeOut(result, quat_repr, quat_repr_2))
    
        s_expr = Tex("$s = (s_0 + s_1 \\cdot i + s_2 \\cdot j + s_3 \\cdot k)$").scale(0.6)
        eq_1 = Tex("$m_1 a_{1,1} + m_2 a_{1,2} + \\ldots + m_n a_{1,n} = s_0$").scale(0.75).move_to(1.5*UP)
        eq_2 = Tex("$m_1 a_{2,1} + m_2 a_{2,2} + \\ldots + m_n a_{2,n} = s_1$").scale(0.75).next_to(eq_1, DOWN)
        eq_3 = Tex("$m_1 a_{3,1} + m_2 a_{3,2} + \\ldots + m_n a_{3,n} = s_2$").scale(0.75).next_to(eq_2, DOWN)
        eq_4 = Tex("$m_1 a_{4,1} + m_2 a_{4,2} + \\ldots + m_n a_{4,n} = s_3$").scale(0.75).next_to(eq_3, DOWN)

        self.play(Write(s_expr))
        self.play(s_expr.animate.shift(2*UP))
        self.play(Write(eq_1), Write(eq_2), Write(eq_3), Write(eq_4))
        self.next_slide()

        basis_matrix = Matrix([
            ["s_0", "s_1", "s_2", "s_3", "1", "0", "0", "\\dots", "0"],
            ["-a_{1,1}", "-a_{2,1}", "-a_{3,1}", "-a_{4,1}", "0", "1", "0", "\\dots", "0"],
            ["-a_{1,2}", "-a_{2,2}", "-a_{3,2}", "-a_{4,2}", "0", "0", "1", "\\dots", "0"],
            ["\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\ddots", "\\vdots"],
            ["-a_{1,n}", "-a_{2,n}", "-a_{3,n}", "-a_{4,n}", "0", "0", "0", "\\dots", "1"],
        ], h_buff=1.8).scale(0.75).next_to(eq_4, DOWN)

        self.play(FadeIn(basis_matrix))
        self.next_slide()

        weight_basis_matrix = Matrix([
            ["W s_0", "W s_1", "W s_2", "W s_3", "W", "0", "0", "\\dots", "0"],
            ["-W a_{1,1}", "-W a_{2,1}", "-W a_{3,1}", "-W a_{4,1}", "0", "1", "0", "\\dots", "0"],
            ["-W a_{1,2}", "-W a_{2,2}", "-W a_{3,2}", "-W a_{4,2}", "0", "0", "1", "\\dots", "0"],
            ["\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\vdots", "\\ddots", "\\vdots"],
            ["-W a_{1,n}", "-W a_{2,n}", "-W a_{3,n}", "-W a_{4,n}", "0", "0", "0", "\\dots", "1"],
        ], h_buff=1.8).scale(0.75)
        
        weight_label = Tex("$W = 2^{256}$").next_to(weight_basis_matrix, DOWN)

        self.play(FadeOut(s_expr, eq_1, eq_2, eq_3, eq_4))
        self.play(basis_matrix.animate.move_to(ORIGIN))
        self.next_slide()

        self.play(Transform(basis_matrix, weight_basis_matrix))
        self.play(Write(weight_label))

class TryDifferentAlgorithms(Slide):

    def construct(self):
        title = Text("Try different algorithms").set_color(YELLOW).move_to(2*UP)

        bulletpoints = BulletedList(
            "LLL is fast but inaccurate for larger dimensions",
            "$\\Rightarrow$ Try BKZ with different block sizes.",
            "If $\\beta = n \\Rightarrow$ BKZ = HKZ $\\Rightarrow$ exponential time complexity",
            "https://github.com/keeganryan/flatter"
        ).scale(0.75).next_to(title, 2*DOWN)

        self.play(Write(title))
        self.play(LaggedStartMap(FadeIn, bulletpoints, shift=0.5 * DOWN, lag_ratio=0.25))
        self.next_slide()

        change_to_cvp = Text("Change view from SVP to CVP").set_color(YELLOW).move_to(3*UP)
        babai_title = Text("I. method: Babai's nearest plane algorithm").scale(0.75).next_to(change_to_cvp, DOWN)

        babai_code = Code("assets/babai_impl.py", style="github-dark", insert_line_no=False).scale(0.75)
        
        self.play(FadeOut(bulletpoints))
        self.play(Transform(title, change_to_cvp), Write(babai_title), FadeIn(babai_code))
        self.next_slide()

        babai_info = BulletedList(
            "Requires reduced basis",
            "tldr: Iteratively project each coordinate onto the nearest hyperplane.",
            "$\\Rightarrow \\frac{\\mathbf{a} \\cdot \\mathbf{g_i}}{\\mathbf{g_i} \\cdot \\mathbf{g_i}}$"
        ).scale(0.75).next_to(babai_code, DOWN)

        self.play(LaggedStartMap(FadeIn, babai_info, shift=0.5 * DOWN, lag_ratio=0.25))

class BabaiVisualization(Slide):

    def construct(self):
        plane = NumberPlane(background_line_style={
            "stroke_opacity": 0
        })

        b0_pos = np.array((-0.2, 0.6, 0))
        b1_pos = np.array((1, 0, 0))

        b0 = Arrow(start=ORIGIN, end=b0_pos, buff=0).set_color(GREEN)
        b1 = Arrow(start=ORIGIN, end=b1_pos, buff=0).set_color(YELLOW)

        self.play(FadeIn(plane))
        self.play(GrowArrow(b0), GrowArrow(b1))
        self.next_slide()

        perfect_goal_pos = 5*b0_pos + 3*b1_pos
        goal_pos = perfect_goal_pos + np.array((0.3, -0.1, 0)) # small displacement
        goal_dot = Dot(goal_pos, color=PURE_RED)
        
        self.play(Create(goal_dot))
        self.next_slide()

        # GS ortogonalized vectors
        g0_pos = np.array((-1/5, 3/5, 0))
        g1_pos = np.array((9/10, 3/10, 0))

        g0 = Arrow(start=ORIGIN, end=g0_pos, buff=0).set_color(RED)
        g1 = Arrow(start=ORIGIN, end=g1_pos, buff=0).set_color(RED)

        self.play(GrowArrow(g0), GrowArrow(g1))
        self.next_slide()

        target_vec = Arrow(start=ORIGIN, end=goal_pos, buff=0).set_color(PINK)
        
        self.play(GrowArrow(target_vec))
        self.next_slide()

        mus = [3.26666666666667, 4.7]

        # step 1: project to g1
        mu_vec = Arrow(start=ORIGIN, end=g1.get_end() * mus[0], buff=0).set_color(PURPLE)
        mu_brace = BraceBetweenPoints(ORIGIN, mu_vec.get_end())
        mu_label = mu_brace.get_text("$c \\cdot \\mathbf{g_1} = " + str(round(mus[0], 2)) + " \\cdot \\mathbf{g_1}$")
        mu_rounded_label = mu_brace.get_text("$\\lceil c \\rfloor = 3$")
        
        projection_vec = Arrow(start=target_vec.get_end(), end=mu_vec.get_end(), buff=0)

        self.play(GrowArrow(mu_vec), FadeIn(mu_brace), Write(mu_label), GrowArrow(projection_vec))
        self.next_slide()

        self.play(Transform(mu_label, mu_rounded_label))
        self.next_slide()

        diff_vec = Arrow(start=ORIGIN, end=-3*b1_pos, buff=0).set_color(PURE_RED)
        diff_brace = BraceBetweenPoints(ORIGIN, diff_vec.get_end(), direction=DOWN)
        diff_label = diff_brace.get_text("$-3 \\mathbf{b_1}$")
        diff_pos = -3 * b1_pos

        diff_brace_updater = lambda b: b.become(BraceBetweenPoints(diff_vec.get_start(), diff_vec.get_end(), direction=DOWN))
        diff_label_updater = lambda b: b.become(diff_brace.get_text("$-3 \\mathbf{b_1}$"))

        self.play(FadeOut(mu_vec, mu_brace, mu_label, projection_vec))
        self.play(GrowArrow(diff_vec), FadeIn(diff_brace), Write(diff_label))
        self.next_slide()

        diff_brace.add_updater(diff_brace_updater)
        diff_label.add_updater(diff_label_updater)

        self.play(diff_vec.animate.put_start_and_end_on(target_vec.get_end(), target_vec.get_end() + diff_pos))
        self.next_slide()

        self.play(target_vec.animate.put_start_and_end_on(ORIGIN, target_vec.get_end() + diff_pos))
        self.next_slide()

        diff_brace.clear_updaters()
        diff_label.clear_updaters()

        self.play(FadeOut(diff_vec, diff_brace, diff_label))
        self.next_slide()

        # step 2 project to g0 - small code repetition, it is what it is
        mu_vec = Arrow(start=ORIGIN, end=g0.get_end() * mus[1], buff=0).set_color(PURPLE)
        mu_brace = BraceBetweenPoints(ORIGIN, mu_vec.get_end())
        mu_label = mu_brace.get_text("$c \\cdot \\mathbf{g_0} = " + str(round(mus[1], 2)) + " \\cdot \\mathbf{g_0}$")
        mu_rounded_label = mu_brace.get_text("$\\lceil c \\rfloor = 5$")
        
        projection_vec = Arrow(start=target_vec.get_end(), end=mu_vec.get_end(), buff=0)

        self.play(GrowArrow(mu_vec), FadeIn(mu_brace), Write(mu_label), GrowArrow(projection_vec))
        self.next_slide()

        self.play(Transform(mu_label, mu_rounded_label))
        self.next_slide()

        diff_vec = Arrow(start=ORIGIN, end=-5*b0_pos, buff=0).set_color(PURE_RED)
        diff_brace = BraceBetweenPoints(ORIGIN, diff_vec.get_end())
        diff_label = diff_brace.get_text("$-5 \\mathbf{b_0}$")
        diff_pos = -5*b0_pos

        diff_brace_updater = lambda b: b.become(BraceBetweenPoints(diff_vec.get_start(), diff_vec.get_end(), direction=DOWN))
        diff_label_updater = lambda b: b.become(diff_brace.get_text("$-5 \\mathbf{b_0}$"))

        self.play(FadeOut(mu_vec, mu_brace, mu_label, projection_vec))
        self.play(GrowArrow(diff_vec), FadeIn(diff_brace), Write(diff_label))
        self.next_slide()

        diff_brace.add_updater(diff_brace_updater)
        diff_label.add_updater(diff_label_updater)

        self.play(diff_vec.animate.put_start_and_end_on(target_vec.get_end(), target_vec.get_end() + diff_pos))
        self.next_slide()

        small_vec = Arrow(start=ORIGIN, end=target_vec.get_end() + diff_pos, buff=0)

        diff_brace.clear_updaters()
        diff_label.clear_updaters()

        self.play(FadeOut(target_vec, diff_vec, diff_brace, diff_label, g0, g1), GrowArrow(small_vec))
        self.next_slide()

        self.play(small_vec.animate.put_start_and_end_on(start=perfect_goal_pos, end=goal_pos))
        self.next_slide()

        original_target_vec = Arrow(start=ORIGIN, end=perfect_goal_pos, buff=0).set_color(ORANGE) 

        self.play(FadeIn(original_target_vec))
        self.next_slide()

        dots = []

        for i in range(-20, 20):
            for j in range(-20, 20):
                dots.append(Dot(i*b0_pos + j*b1_pos))    
        
        self.play(LaggedStartMap(FadeIn, dots, shift=0.5 * DOWN, lag_ratio=0.01))
        self.next_slide()

        # what's the exact linear combination? -> system of equations
        # M^-1 * v = x

        basis_matrix = Matrix(np.transpose([b0_pos[:2], b1_pos[:2]])).scale(0.8).to_corner(UL).set_color(YELLOW)
        unknown_label = Tex("$\\mathbf{x}$").scale(0.8).next_to(basis_matrix).set_color(YELLOW)
        equal_sign = Tex("=").scale(0.8).next_to(unknown_label).set_color(YELLOW)
        goal_matrix = Matrix(np.transpose([perfect_goal_pos[:2]])).scale(0.8).next_to(equal_sign).set_color(YELLOW)

        self.play(LaggedStartMap(FadeOut, dots, shift=0.5 * DOWN, lag_ratio=0.01))
        self.play(FadeIn(basis_matrix, unknown_label, goal_matrix, equal_sign))
        self.next_slide()

        inverse_sign = Tex("-1").scale(0.7).move_to(basis_matrix.get_corner(UR) + 0.1 * UP + 0.2 * RIGHT).set_color(YELLOW)

        self.play(FadeIn(inverse_sign), 
                  goal_matrix.animate.next_to(basis_matrix, 1.5* RIGHT), 
                  equal_sign.animate.shift(RIGHT), 
                  unknown_label.animate.move_to(basis_matrix.get_center() + 3.5*RIGHT))
        self.next_slide()

        result_matrix = Matrix(np.transpose([["5", "3"]])).scale(0.8).move_to(basis_matrix.get_center() + 3.75*RIGHT).set_color(YELLOW)

        self.play(Transform(unknown_label, result_matrix))
        self.next_slide()
    
        chain_positions = []
        chain_colors = []

        for i in range(3):
            chain_positions.append(i * b1_pos)
            chain_colors.append(YELLOW)

        for i in range(6):
            chain_positions.append(i * b0_pos + 3 * b1_pos)
            chain_colors.append(GREEN)
        
        arrow_chain = create_arrow_chain(chain_positions, chain_colors)

        self.play(FadeOut(b0))
        self.play(LaggedStartMap(FadeIn, arrow_chain, lag_ratio=0.5))
        self.next_slide()

        self.play(FadeOut(basis_matrix, unknown_label, equal_sign, goal_matrix, inverse_sign, original_target_vec, small_vec, result_matrix))
        self.play(LaggedStartMap(FadeIn, dots, shift=0.5 * DOWN, lag_ratio=0.01))

class KannanEmbedding(Slide):

    def construct(self):
        title = Text("Change view from SVP to CVP").set_color(YELLOW).move_to(3*UP)
        subtitle = Text("II. method: Kannan's embedding technique").scale(0.75).next_to(title, DOWN)

        kannan_matrix = Matrix(np.array([["\\mathbf{B}", "0"], ["\\mathbf{t}", "W"]])).scale(0.8).set_color(YELLOW)
        kannan_info = BulletedList(
            "Embed a CVP instance into an SVP lattice.",
            "New short vector will be $(\\mathbf{t} - \\mathbf{B} x, W)$",
            "W is the weight"
        ).scale(0.75).next_to(kannan_matrix, DOWN)

        self.play(Write(title), Write(subtitle))
        self.play(FadeIn(kannan_matrix))
        self.play(LaggedStartMap(FadeIn, kannan_info, shift=0.5 * DOWN, lag_ratio=0.25))

