from manim import *
from manim_slides import Slide

class LCGIntroduction(Slide):

    def construct(self):
        title = Text("Linear Congruential Generators").set_color(YELLOW)
        lcg_intro = BulletedList(
            "Used by java.util.Random",
            "$x_{n+1} \\equiv a x_n + b \\ (\\mathrm{mod}\\ c)$",
            "If $c$ is a power of 2 and $b \\neq 0$",
            "1. $c$ and $b$ are coprime,",
            "2. $a-1$ is divisible by all prime factors of $b$",
            "3. $a-1$ is divisible by 4 if $c$ is divisible by 4.",
            "$\\iff$ period equals to $c$ for all x",
            "reversible, since $x_n \\equiv a^{-1}(x_{n+1} - b) \\ (\\mathrm{mod}\\ c)$",
        dot_scale_factor=0, buff=MED_SMALL_BUFF).scale(0.8) # dots are overrated

        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.move_to(3*UP))
        self.play(LaggedStartMap(FadeIn, lcg_intro, shift=0.5 * DOWN, lag_ratio=0.25))

class RandarExploit(Slide):

    def construct(self):
        randar_title = Text("RANDAR exploit - Minecraft").move_to(3*UP).set_color(YELLOW)
        survival_img = ImageMobject("assets/minecraft_survival.png").scale(0.75).next_to(randar_title, DOWN)
        anarchy_spawn = ImageMobject("assets/2b2t_spawn.webp").scale(1.25).next_to(randar_title, DOWN)
        anarchy_base = ImageMobject("assets/2b2t_masons_base.jpg").scale(0.75).next_to(randar_title, DOWN)

        self.play(Write(randar_title))
        self.play(FadeIn(survival_img))
        self.next_slide()

        self.play(FadeOut(survival_img))
        self.play(FadeIn(anarchy_spawn))
        self.next_slide()

        self.play(FadeOut(anarchy_spawn))
        self.play(FadeIn(anarchy_base))
        self.next_slide()

        source = Text("source: https://github.com/spawnmason/randar-explanation").scale(0.3).to_corner(DL)
        woodland_code = Code("assets/WoodlandCode.java", style="github-dark", insert_line_no=False).scale(0.5).next_to(randar_title, DOWN)
        spawn_item_code = Code("assets/SpawnItem.java", style="github-dark", insert_line_no=False).scale(0.5).next_to(randar_title, DOWN)
        java_nextfloat_code = Code("assets/NextFloat.java", style="github-dark", insert_line_no=False).scale(0.5).next_to(spawn_item_code, DOWN)
        first_highlight = SurroundingRectangle(woodland_code.code[8], buff=0).set_fill(YELLOW).set_opacity(0).stretch_to_fit_width(woodland_code.background_mobject.get_width()).align_to(woodland_code.background_mobject, LEFT)
        second_highlight = SurroundingRectangle(woodland_code.code[29], buff=0).set_fill(YELLOW).set_opacity(0).stretch_to_fit_width(woodland_code.background_mobject.get_width()).align_to(woodland_code.background_mobject, LEFT)
        
        self.play(FadeOut(anarchy_base))
        self.play(FadeIn(woodland_code), Write(source))
        self.next_slide()

        self.add(first_highlight, second_highlight)
        self.play(first_highlight.animate.set_opacity(0.3), second_highlight.animate.set_opacity(0.3))
        self.next_slide()

        self.play(FadeOut(first_highlight, second_highlight, woodland_code))
        self.play(FadeIn(spawn_item_code), FadeIn(java_nextfloat_code))

class TruncatedRNGLattice(Slide):

    def construct(self):
        title = Text("Breaking truncated LCGs").move_to(3*UP).set_color(YELLOW)
        we_have = Tex("We have: $\\lfloor \\tfrac{x_1}{2^{24}} \\rfloor$, $\\lfloor \\tfrac{x_2}{2^{24}} \\rfloor$, $\\lfloor \\tfrac{x_3}{2^{24}} \\rfloor$").scale(0.9).next_to(title, DOWN)

        x_2 = Tex("$x_2 = a x_1 + b \\ (\\mathrm{mod}\\ c)$").next_to(we_have, 2*DOWN)
        x_3_1 = Tex("$x_3 = a x_2 + b \\ (\\mathrm{mod}\\ c)$").next_to(x_2, DOWN)
        x_3_2 = Tex("$x_3 = a (a x_1 + b) + b \\ (\\mathrm{mod}\\ c)$").next_to(x_2, DOWN)
        x_3_3 = Tex("$x_3 = a^2 x_1 + ab + b \\ (\\mathrm{mod}\\ c)$").next_to(x_2, DOWN)

        self.play(Write(title))
        self.play(FadeIn(we_have))
        self.play(Write(x_2), Write(x_3_1))
        self.next_slide()

        self.play(TransformMatchingTex(x_3_1, x_3_2))
        self.next_slide()

        self.play(TransformMatchingTex(x_3_2, x_3_3))
        self.next_slide()

        lattice = Matrix([
            ["1", "a", "a^2"],
            ["0", "c", "0"],
            ["0", "0", "c"],
        ]).scale(0.9).next_to(x_3_1, 2*DOWN)
        close_lattice_point = Tex("$(\\lfloor \\tfrac{x_1}{2^{24}} \\rfloor + 2^{23}, \\lfloor \\tfrac{x_2}{2^{24}} \\rfloor + 2^{23} - b, \\lfloor \\tfrac{x_3}{2^{24}} \\rfloor + 2^{23} - ab - b)$").scale(0.9).next_to(lattice, 2*DOWN)

        self.play(FadeIn(lattice))
        self.play(Write(close_lattice_point))