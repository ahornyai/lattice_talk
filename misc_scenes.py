from manim import *
from manim_slides import Slide

class TitleScene(Slide):
    def construct(self):
        # title slide
        title = Text("Lattice-based cryptanalysis", color=YELLOW).scale(1.5)
        author = Text("Alex Hornyai")
        author.next_to(title, DOWN)

        self.play(Write(title))
        self.wait(0.25)
        self.play(Write(author))
        self.wait()

        self.next_slide()

        # whoami slide
        whoami = Text("whoami", color=YELLOW).move_to(3*UP)

        self.play(
            FadeOut(author), 
            Transform(title, whoami)
        )
        self.wait(0.25)
        
        list = BulletedList("CTF player", "IT security and cryptography fan", "Main categories: Cryptography, web, binary exploitation", "high school student")
        list.align_to(whoami)
        self.play(
            LaggedStartMap(FadeIn, list, shift=0.5 * DOWN, lag_ratio=0.25)
        )

class OverviewScene(Slide):

    def construct(self):
        overview = Text("Chapters", color=YELLOW).move_to(3*UP)
        overview_list = BulletedList("Introduction to lattices", "The Lenstra-Lenstra-Lovász (LLL) algorithm", "Common lattice problems/attacks", "Building encryptions relying on lattice problems")
        rect = SurroundingRectangle(overview_list[0])

        self.play(
            Write(overview),
            LaggedStartMap(FadeIn, overview_list, shift=0.5 * DOWN, lag_ratio=0.25)
        )

        self.play(DrawBorderThenFill(rect))

class EndingScene(Slide):

    def construct(self):
        thanks = Text("Thanks for your attention").move_to(2*UP).set_color(YELLOW)
        github_logo = ImageMobject("assets/github.png").scale(0.5).move_to(4*LEFT + 2.5*DOWN)
        linkedin_logo = ImageMobject("assets/linkedin.png").scale(0.4).move_to(5*RIGHT + 2.5*DOWN)
        github = Text("ahornyai").scale(0.5).next_to(github_logo, LEFT)
        linkedin = Text("Hornyai Alex").scale(0.5).next_to(linkedin_logo, LEFT)

        self.play(Write(thanks), FadeIn(github_logo, shift=DOWN), FadeIn(linkedin_logo, shift=DOWN), Write(github), Write(linkedin))