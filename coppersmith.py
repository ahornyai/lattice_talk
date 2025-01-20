from manim import *
from manim_slides import Slide

class CoppersmithScene(Slide):

    def construct(self):
        title = Text("Coppersmith's method").set_color(YELLOW)
        new_title = Text("Breaking RSA using Coppersmith's method").move_to(3*UP).set_color(YELLOW)
        
        bulletpoints = BulletedList(
            "$f(x) \\equiv a_nx^n+\\ldots+a_1x+a_0 \\ (\\mathrm{mod}\\ N)$",
            "goal: find $f(x) \\equiv 0 \\ (\\mathrm{mod}\\ N)$",
            "or even $(\\mathrm{mod}\\ p)$ where $p | N$ and $p \\approx N^{\\beta}$",
            "$x < X < N^{\\tfrac{\\beta^2}{deg(\\mathbf{f})} - \\epsilon}$",
        ).scale(0.8)

        self.play(Write(title))
        self.play(title.animate.move_to(3*UP))
        self.play(LaggedStartMap(FadeIn, bulletpoints, shift=0.5 * DOWN, lag_ratio=0.25))
        self.next_slide()

        coppersmith_basis = Matrix([
            ["N", "0", "\\dots", "0", "0"],
            ["0", "XN", "\\dots", "0", "0"],
            ["\\vdots", "", "", "\\vdots", "\\vdots"],
            ["0", "0", "\\dots", "X^{d-1}N", "0"],
            ["a_0", "a_1 X", "\\dots", "a_{d-1} X^{d-1}", "X^d"],
        ], h_buff=2.5).scale(0.8)

        self.play(FadeOut(bulletpoints))
        self.play(FadeIn(coppersmith_basis))
        self.next_slide()

        common_attacks = BulletedList(
            "Stereotyped message: $f(x) = (x + M)^e - c \\equiv 0 \\ (\\mathrm{mod}\\ N)$",
            "Affine padding: $f(x) = (ax + b)^e - c \\equiv 0 \\ (\\mathrm{mod}\\ N)$",
            "Partially known factor: $f(x) = (p_{msb} + x) \\equiv 0 \\ (\\mathrm{mod}\\ p)$",
            "Boneh-Durfee - for low $d < N^{0.292}$",
            "More attacks: https://hal.science/hal-03045663/document",
            "There are also multivariate generalizations"
        ).scale(0.8)

        self.play(FadeOut(coppersmith_basis), Transform(title, new_title))
        self.play(LaggedStartMap(FadeIn, common_attacks, shift=0.5 * DOWN, lag_ratio=0.25))