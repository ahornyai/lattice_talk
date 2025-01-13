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

        self.play(irisctf_title.animate.move_to(2*UP))
        self.play(LaggedStartMap(FadeIn, irisctf_info, shift=0.5 * DOWN, lag_ratio=0.25))
        self.next_slide()

        quaternion_example = Tex("$a_1 = a + b*i + c*j + d*k$")
        quat_arrow = Arrow(start=LEFT, end=RIGHT)
        quat_repr = Matrix(np.array([["a","b","c","d"],["-b","a","-d","c"],["-c","d","a","-b"],["-d","-c","b","a"]])).next_to(quat_arrow, RIGHT)

        self.play(FadeOut(irisctf_info))
        self.play(Write(quaternion_example))
        self.play(quaternion_example.animate.move_to(4*LEFT))
        self.play(GrowArrow(quat_arrow))
        self.play(FadeIn(quat_repr))
        self.next_slide()