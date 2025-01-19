from manim import *
from manim_slides import Slide

class CoppersmithIntro(Slide):

    def construct(self):
        title = Text("Coppersmith's method").set_color(YELLOW)
        bulletpoints = BulletedList(
            "$f(x) \\equiv a_nx^n+\\ldots+a_1x+a_0 \\ (\\mathrm{mod}\\ N)$",
            "goal: find $f(x) \\equiv 0 \\ (\\mathrm{mod}\\ N)$",
            "$x < X < N^{\\tfrac{\\beta^2}{deg(\\mathbf{f})} - \\epsilon}$"
        ).scale(0.8)

        self.play(Write(title))
        self.play(title.animate.move_to(3*UP))
        self.play(LaggedStartMap(FadeIn, bulletpoints, shift=0.5 * DOWN, lag_ratio=0.25))

        # TODO