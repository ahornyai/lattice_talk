from manim import *
from manim_slides import Slide

class KnapsackDefinition(Slide):

    def construct(self):
        title = Text("Knapsack / subset sum").move_to(3*UP).set_color(YELLOW)
        given_label = Tex("Given:").move_to(UP + 3*LEFT).set_color(YELLOW)
        given_set = Tex("$\\mathbf{A}$ = \\{$a_1, a_2, \\ldots, a_n$\\}").next_to(given_label)
        given_value = Tex("$s = \\sum{e_i a_i}$ where $e_i \\in \\{0, 1\\}$").next_to(given_label).shift(0.7 * DOWN)

        self.play(Write(title))
        self.play(Write(given_label), Write(given_set), Write(given_value))
        self.next_slide()

        example_eq = Tex("$832499 \\cdot e_1 + 823033 \\cdot e_2 + 765137 \\cdot e_3 + 1025891 \\cdot e_4 = 2623527$").scale(0.8).next_to(given_value, 2*DOWN).shift(LEFT).set_color(YELLOW)
        example_eq_sol = Tex("$832499 \\cdot 1 + 823033 \\cdot 0 + 765137 \\cdot 1 + 1025891 \\cdot 1 = 2623527$").scale(0.8).move_to(example_eq).set_color(YELLOW)

        self.play(Write(example_eq))
        self.next_slide()

        self.play(TransformMatchingTex(example_eq, example_eq_sol))
        self.next_slide()

        mod_example_eq = Tex("$832499 \\cdot e_1 + 823033 \\cdot e_2 + 765137 \\cdot e_3 + 1025891 \\cdot e_4 \\equiv 571733 \\ (\\mathrm{mod}\\ 1025897)$").scale(0.8).move_to(example_eq).set_color(YELLOW)
        mod_example_eq_sol = Tex("$832499 \\cdot 1 + 823033 \\cdot 0 + 765137 \\cdot 1 + 1025891 \\cdot 1 \\equiv 571733 \\ (\\mathrm{mod}\\ 1025897)$").scale(0.8).move_to(example_eq).set_color(YELLOW)

        self.play(FadeOut(example_eq_sol))
        self.play(Write(mod_example_eq))
        self.next_slide()

        self.play(TransformMatchingTex(mod_example_eq, mod_example_eq_sol))
        self.next_slide()

        merkle_hellmann = Tex("Merkle-Hellman cryptosystem").move_to(2*DOWN)
        merkle_hellmann_broken = Tex("$\\Rightarrow$ broken by lattices (in low density setting)").next_to(merkle_hellmann, DOWN)

        self.play(FadeOut(mod_example_eq_sol))
        self.play(Write(merkle_hellmann), Write(merkle_hellmann_broken))
        self.next_slide()

        density = Tex("$d = \\frac{n}{\\log_2 \\max(a_i)}$").move_to(example_eq).set_color(YELLOW)
        
        self.play(Write(density))

class KnapsackLattice(Slide):

    def construct(self):
        title = Text("Subset sum - CJLOSS algorithm").move_to(3*UP).set_color(YELLOW)
        lattice = Matrix([
            ["1", "", "", "", "N a_1"],
            ["", "1", "", "", "N a_2"],
            ["", "", "\\ddots", "", "\\vdots"],
            ["", "", "", "1", "N a_n"],
            ["\\tfrac{1}{2}", "\\tfrac{1}{2}", "\\dots", "\\tfrac{1}{2}", "N s"],
        ]).scale(0.75)
        N_val = Tex("$N = \\Bigl \\lceil \\sqrt{\\tfrac{n+1}{4}} \\ \\Bigr \\rceil$").next_to(lattice, 2*DOWN).set_color(YELLOW)
        shortest_vec = Tex("$(e_1 - \\tfrac{1}{2}, \\dots, e_n - \\tfrac{1}{2}, -1)$").next_to(N_val, DOWN)

        self.play(Write(title))
        self.play(FadeIn(lattice))
        self.next_slide()

        self.play(Write(N_val))
        self.next_slide()

        self.play(Write(shortest_vec))
        self.next_slide()

        d_ineq = Tex("$d < 0.9408 \\dots$").next_to(lattice, 2*DOWN).set_color(YELLOW)

        self.play(FadeOut(N_val))
        self.play(Write(d_ineq))

class HashMasterChallenge(Slide):

    def construct(self):
        title = Text("DDC Nationals - HashMaster 9000").set_color(YELLOW)
        final_hash = Tex("$h \\equiv \\displaystyle\\sum_{i=0}^{68}$ MD5(str($i) \\ || \\ c_i$) $\\ (\\mathrm{mod}\\ 2^{128})$")
        restriction = Tex("$c_i \\in \\{L, l\\}$ for $4 \\leq i \\leq 67$").move_to(0.5 * DOWN)
        hash_func = Tex("H(i, c) = MD5(str($i) \\ || \\ c_i$)").scale(0.8).move_to(2.2*UP)

        self.play(Write(title))
        self.next_slide()
        
        self.play(title.animate.move_to(3*UP))
        self.play(Write(final_hash))
        self.next_slide()

        self.play(final_hash.animate.move_to(UP))
        self.play(Write(restriction))
        self.next_slide()

        first_eq = Tex("$H(0, L) e_0 + H(0, l) e_1 + \\dots + H(67, L) e_{134} + H(67, l) e_{135} \\equiv h'$").scale(0.7).move_to(0.5 * DOWN).set_color(YELLOW)
        second_eq_1 = Tex("$H(0, L) e_0 + H(0, l) (1 - e_0) + \\dots + H(67, L) e_{67} + H(67, l) (1 - e_{67}) \\equiv h'$").scale(0.7).move_to(0.5 * DOWN).set_color(YELLOW)
        second_eq_2 = Tex("$H(0, L) e_0 + H(0, l) - H(0, l) e_0 + \\dots + H(67, L) e_{67} + H(67, l) - H(67, l) e_{67} \\equiv h'$").scale(0.7).move_to(0.5 * DOWN).set_color(YELLOW)
        second_eq_3 = Tex("$H(0, L) e_0 - H(0, l) e_0 + \\dots + H(67, L) e_{67} - H(67, l) e_{67} + H(0, l) + \\dots + H(67, l) \\equiv h'$").scale(0.7).move_to(0.5 * DOWN).set_color(YELLOW)
        second_eq_4 = Tex("$(H(0, L) - H(0, l)) e_0 + \\dots + (H(67, L) - H(67, l)) e_{67} + H(0, l) + \\dots + H(67, l) \\equiv h'$").scale(0.7).move_to(0.5 * DOWN).set_color(YELLOW)
        second_eq_5 = Tex("$(H(0, L) - H(0, l)) e_0 + \\dots + (H(67, L) - H(67, l)) e_{67} \\equiv h' - (H(0, l) + \\dots + H(67, l))$").scale(0.7).move_to(0.5 * DOWN).set_color(YELLOW)

        self.play(Write(hash_func), Create(SurroundingRectangle(hash_func)))
        self.play(Transform(restriction, first_eq))
        self.next_slide()

        self.play(TransformMatchingTex(restriction, second_eq_1))
        self.next_slide()

        self.play(TransformMatchingTex(second_eq_1, second_eq_2))
        self.next_slide()
        
        self.play(TransformMatchingTex(second_eq_2, second_eq_3))
        self.next_slide()

        self.play(TransformMatchingTex(second_eq_3, second_eq_4))
        self.next_slide()

        self.play(TransformMatchingTex(second_eq_4, second_eq_5))
        self.next_slide()

        A = Tex("A = [H(0, L) - H(0, l), H(1, L) - H(1, l), $\\dots$, H(67, L) - H(67, l)]").scale(0.8).move_to(2*DOWN)
        s = Tex("$s = h' - (H(0, l) + \\dots + H(67, l))$").scale(0.8).next_to(A, DOWN)

        self.play(Write(A))
        self.play(Write(s))