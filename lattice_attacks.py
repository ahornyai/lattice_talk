from manim import *
from manim_slides import Slide

class SmallLinearSystem(Slide):

    def construct(self):
        eq_sym = Tex("$a_1 \\mathbf{v_1} + a_2 \\mathbf{v_2} + \\ldots + a_n \\mathbf{v_n} = \\mathbf{c}$").set_color(YELLOW)
        eq_3 = Tex("$a_1 \\mathbf{v_1} + a_2 \\mathbf{v_2} + \\mathbf{v_3} = \\mathbf{c}$").set_color(YELLOW).move_to(2*UP)
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
        self.next_slide()

        irisctf_title = Text("IrisCTF2025 - knutsacque").set_color(YELLOW)

        self.play(FadeOut(success_img_1))
        self.play(FadeOut(B_sym, eq_3_subst))
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

class IrisCTFSolution(Slide):

    def construct(self):
        irisctf_title = Text("IrisCTF2025 - knutsacque").move_to(3*UP).set_color(YELLOW)
        s_expr = Tex("$s = (s_0 + s_1 \\cdot i + s_2 \\cdot j + s_3 \\cdot k)$").scale(0.6)
        eq_1 = Tex("$m_1 a_{1,1} + m_2 a_{1,2} + \\ldots + m_n a_{1,n} = s_0$").scale(0.75).move_to(1.5*UP)
        eq_2 = Tex("$m_1 a_{2,1} + m_2 a_{2,2} + \\ldots + m_n a_{2,n} = s_1$").scale(0.75).next_to(eq_1, DOWN)
        eq_3 = Tex("$m_1 a_{3,1} + m_2 a_{3,2} + \\ldots + m_n a_{3,n} = s_2$").scale(0.75).next_to(eq_2, DOWN)
        eq_4 = Tex("$m_1 a_{4,1} + m_2 a_{4,2} + \\ldots + m_n a_{4,n} = s_3$").scale(0.75).next_to(eq_3, DOWN)

        self.add(irisctf_title)

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
        self.next_slide()