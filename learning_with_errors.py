from manim import *
from manim_slides import Slide

class IntroToLWE(Slide):

    def construct(self):
        title = Text("Learning With Errors", color=YELLOW)
        A_matrix = Matrix([
            ["a_{1,1}", "a_{1,2}", "\\dots", "a_{1, n}"],
            ["a_{2,1}", "a_{2,2}", "\\dots", "\\vdots"],
            ["\\vdots", "\\vdots", "\\ddots", "\\vdots"],
            ["a_{n,1}", "\\dots", "\\dots", "a_{n, n}"]
        ]).scale(0.8).move_to(3*LEFT)
        s_vector = Matrix(np.transpose([["s_1","s_2","\\vdots","s_n"]])).scale(0.8).next_to(A_matrix)
        plus_label = Text("+").next_to(s_vector)
        e_vector = Matrix(np.transpose([["e_1","e_2","\\vdots","e_n"]])).scale(0.8).next_to(plus_label)
        eq_label = Tex("$\\equiv$").next_to(e_vector)
        b_vector = Matrix(np.transpose([["b_1","b_2","\\vdots","b_n"]])).scale(0.8).next_to(eq_label)
        mod_label = Tex("$\\ (\\mathrm{mod} \\ q)$").next_to(b_vector)

        matrix_group = VGroup(A_matrix, s_vector, plus_label, e_vector, eq_label, b_vector, mod_label)
        public_private_info = Tex("$(\\mathbf{A}, b)$ are public, $(s, e)$ is private").move_to(3*DOWN)

        self.play(Write(title))
        self.play(title.animate.move_to(3*UP))
        self.play(FadeIn(matrix_group))
        self.play(Write(public_private_info))
        self.next_slide()

        eq_1 = Tex("$a_{1,1} s_1 + a_{1,2} s_2 + \\dots + a_{1, n} + e_1 \\equiv b_1 \\ (\\mathrm{mod} \\ q)$").move_to(UP)
        eq_2 = Tex("$a_{2,2} s_1 + a_{2,2} s_2 + \\dots + a_{2, n} + e_2 \\equiv b_2 \\ (\\mathrm{mod} \\ q)$").next_to(eq_1, DOWN)
        dots = Tex("\\vdots").next_to(eq_2, DOWN)
        eq_3 = Tex("$a_{n,1} s_1 + a_{n,2} s_2 + \\dots + a_{n, n} + e_n \\equiv b_n \\ (\\mathrm{mod} \\ q)$").next_to(dots, DOWN)

        eq_group = VGroup(eq_1, eq_2, dots, eq_3)

        self.play(Transform(matrix_group, eq_group))

class LWEProblems(Slide):

    def construct(self):
        title = Text("Learning With Errors", color=YELLOW).move_to(3*UP)
        lwe_problems = BulletedList(
            "Search-LWE: find s vector",
            "Decision-LWE: distinguish b from \"random\"",
            "these are equivalent when $q$ is a prime bounded by some polynomial in $n$",
            "We can embed messages",
            "$b \\equiv \\mathbf{A} s + e + \\tfrac{q}{p} \\cdot m \\ (\\mathrm{mod} \\ q)$",
            "$b \\equiv \\mathbf{A} s + p \\cdot e + m \\ (\\mathrm{mod} \\ q)$"
        ).scale(0.75).next_to(title, 2*DOWN)

        self.add(title)
        self.play(LaggedStartMap(FadeIn, lwe_problems, shift=0.5 * DOWN, lag_ratio=0.25))