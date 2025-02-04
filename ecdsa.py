from manim import *
from manim_slides import Slide

class ECDSAScene(Slide):

    def construct(self):
        title = Text("Elliptic Curve Digital Signature Algorithm").set_color(YELLOW)
        new_title = Text("ECDSA").move_to(3*UP).set_color(YELLOW)

        self.play(Write(title))
        self.next_slide()

        self.play(title.animate.move_to(3*UP))
        self.play(Transform(title, new_title))

        r = Tex("$r \\equiv [k*G]_x \\ (\\mathrm{mod}\\ q)$").move_to(0.5*UP)
        s = Tex("$s \\equiv k^{-1} * (h + r*d) \\ (\\mathrm{mod}\\ q)$").move_to(0.2*DOWN) # 0.7 y difference

        self.play(Write(r), Write(s))
        self.next_slide()

        self.play(r.animate.move_to(2*UP), s.animate.move_to(1.3*UP))

        q = Text("q - generator point's order, must be prime").scale(0.5)
        k = Text("k - nonce").scale(0.5).move_to(3*LEFT + 0.5*DOWN)
        point_G = Text("G - generator point on a curve").scale(0.5).move_to(2*RIGHT + 0.5*DOWN)
        h = Text("h - hash digest").scale(0.5).move_to(1.5*RIGHT + 1*DOWN)
        d = Text("d - private key").scale(0.5).move_to(3*LEFT + 1*DOWN)

        self.play(Write(q), Write(k), Write(point_G), Write(h), Write(d))
        self.next_slide()

        k_rect = SurroundingRectangle(k, buff=0.07)
        g_rect = SurroundingRectangle(point_G, buff=0.07)
        h_rect = SurroundingRectangle(h, buff=0.07)

        self.play(Write(Text("Attack surface?").set_color(YELLOW).move_to(2*DOWN)))
        self.play(Write(k_rect), Write(g_rect), Write(h_rect))
        self.next_slide()

        self.play(FadeOut(g_rect, h_rect))

class PracticalVulnExampleScene(Slide):

    def construct(self):
        putty_cve_headline = ImageMobject("assets/putty_cve.png").scale(1.25)
        minerva = ImageMobject("assets/minerva.png").scale(0.8)
        predictable_nonce_img = ImageMobject("assets/ecdsa_predictable_nonce.png").scale(1.25)
        minerva_label = Text("Minerva: The curse of ECDSA nonces").next_to(minerva, DOWN)

        self.play(FadeIn(putty_cve_headline))
        self.next_slide()

        self.play(FadeOut(putty_cve_headline))
        self.play(FadeIn(minerva), Write(minerva_label))
        self.next_slide()

        self.play(FadeOut(minerva), FadeOut(minerva_label))
        self.play(FadeIn(predictable_nonce_img))
        self.next_slide()

class BiasedNonceAttackScene(Slide):

    def construct(self):
        title = Text("Biased nonce lattice attacks").set_color(YELLOW)

        self.play(Write(title))

        self.next_slide()
        self.play(title.animate.move_to(3*UP))

        what_if = Text("What if the few most significant bits of our nonces are constantly all zero?").scale(0.6).move_to(UP)
        then = Tex("$ \\implies$ our nonce k will be way smaller than our private key d").set_color(YELLOW)

        self.play(Write(what_if))
        self.play(Write(then))
        
        k_group = VGroup()

        k_1 = Tex("$k_1 \\equiv s_1^{-1} h_1 + s_1^{-1} r d \\ (\\mathrm{mod}\\ q)$").move_to(DOWN)
        k_2 = Tex("$k_2 \\equiv s_2^{-1} h_2 + s_2^{-1} r d \\ (\\mathrm{mod}\\ q)$").next_to(k_1, DOWN)

        k_group.add(k_1, k_2)

        self.play(FadeIn(k_group))

        self.next_slide()

        group = VGroup()
        k_vec = Matrix(np.transpose([["k_1", "k_2"]])).move_to(2*DOWN + 4*LEFT)
        eq = Tex("$ \\equiv $").move_to(2*DOWN + 3*LEFT)
        c_vec = Matrix(np.transpose([["s_1^{-1} h_1", "s_2^{-1} h_2"]])).move_to(2*DOWN + 1.4*LEFT)
        plus = Tex("$ + $").move_to(2*DOWN + 0.2*RIGHT)
        d_vec = Matrix(np.transpose([["s_1^{-1} r d", "s_2^{-1} r d"]])).move_to(2*DOWN + 2*RIGHT)
        mod = Tex("$ (\\mathrm{mod}\\ q)$").move_to(2*DOWN + 4.5*RIGHT)
        vec_equation = Tex("$ \\vec{k} \\equiv \\vec{h} + d \\vec{r} \\ (\\mathrm{mod}\\ q)$").move_to(3.5*DOWN)

        group.add(k_vec.get_brackets(), k_vec.get_columns()[0])
        group.add(eq, plus, mod)
        group.add(c_vec.get_brackets(), c_vec.get_columns()[0])
        group.add(d_vec.get_brackets(), d_vec.get_columns()[0])

        self.play(Transform(k_group, group))
        self.play(Write(vec_equation))

class LLLMatrixScene(Slide):

    def construct(self):
        title = Tex("$\\vec{k}$ is short $\\implies$ SVP").move_to(3*UP).set_color(YELLOW)
        basis = Matrix(np.transpose([
            ["s_1^{-1} h_1", "s_2^{-1} h_2"],
            ["s_1^{-1} r_1", "s_1^{-1} r_2"],
            ["q", "0"],
            ["0", "q"],
        ]), h_buff=1.5).set_color(YELLOW)
        h_prime = Tex("$h' \\equiv s^{-1} * h \\ (\\mathrm{mod}\\ q)$").scale(0.75).move_to(2*UP)
        r_prime = Tex("$r' \\equiv s^{-1} * r \\ (\\mathrm{mod}\\ q)$").scale(0.75).next_to(h_prime, DOWN)

        self.play(Write(title), Write(h_prime), Write(r_prime), FadeIn(basis.get_brackets()))
        self.play(LaggedStartMap(FadeIn, basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.25))

        arr = Arrow(start=DOWN, end=2*DOWN).scale(1.5)

        self.play(GrowArrow(arr))

        reduced_basis = Matrix(np.transpose([
            ["k_1", "k_2"],
            ["?", "?"],
            ["?", "?"],
            ["?", "?"]
        ])).set_color(YELLOW).next_to(arr, DOWN)

        self.play(FadeIn(reduced_basis.get_brackets()), LaggedStartMap(FadeIn, reduced_basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.25))

        self.next_slide()

        self.play(
            FadeOut(basis.get_brackets(), shift=DOWN), 
            LaggedStartMap(FadeOut, basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.1),
            FadeOut(reduced_basis.get_brackets(), shift=DOWN), 
            LaggedStartMap(FadeOut, reduced_basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.1),
            FadeOut(h_prime, shift=DOWN), FadeOut(r_prime, shift=DOWN),
            FadeOut(arr)
        )

        msb_attack = ImageMobject("assets/msb_attack_code.png").scale(1.15).next_to(title, DOWN)
        github_img = ImageMobject("assets/github_ecc_cryptanalysis.png").scale(0.8)
        github_url = Text("https://github.com/ahornyai/ecc_cryptanalysis").scale(0.7).next_to(github_img, DOWN)
        
        self.play(FadeIn(msb_attack, shift=DOWN))
        self.next_slide()

        self.play(FadeOut(msb_attack, title))
        self.play(FadeIn(github_img, shift=DOWN), Write(github_url))

class BonusAttackScene(Slide):

    def construct(self):
        title = Text("Bonus attacks").move_to(3*UP).set_color(YELLOW)
        attacks = BulletedList(
            "Private key can be recovered with any amount of nonce leakage (in some cases even less than one bit is enough)",
            "LadderLeak: Breaking ECDSA with Less than One Bit of Nonce Leakage - https://www.youtube.com/watch?v=Nk1uqe8Z7k4",
            "Polynonce attack: nonces generated by LCG-s can be broken",
            "https://research.kudelskisecurity.com/2023/03/06/polynonce-a-tale-of-a-novel-ecdsa-attack-and-bitcoin-tears/",
            "More info on lattice attacks: https://github.com/josephsurin/lattice-based-cryptanalysis/"
        ).scale(0.7)

        self.play(Write(title), LaggedStartMap(FadeIn, attacks, shift=0.5 * DOWN, lag_ratio=0.1))
