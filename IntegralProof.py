from manim import *
import numpy as np


# run in terminal "manim -pqh IntegralProof.py IntegralProof"
#       -p is to preview, qh is quality high

class IntegralProof(Scene):
    def construct(self):
        ax = Axes(x_range=[-1,5],
                  y_range=[-1,5]) # axes setup
        def func(x): # function setup
            return -((x-0.9)**3) + ((0.6*x)**2) + 3
        graph = ax.plot(lambda x: func(x), color=WHITE)
        self.play(Create(ax))
        self.play(Create(graph))
        def nRects(n):
            return ax.get_riemann_rectangles(graph = graph,
                                          x_range=[0,2.68],
                                          dx=(2.68/n),
                                          stroke_width=0.25,
                                          fill_opacity=0.75,
                                          color=BLUE)
        rects1 = nRects(6)
        rects2 = nRects(20)
        rects3 = nRects(100)
        area = ax.get_area(graph,x_range=(0,2.68),color=BLUE,opacity=0.75)
        n_text = MathTex("\\lim_{n\\to6} \\sum_{i=1}^n f(x_i)\\Delta x").to_corner(UR)
        n1_text = MathTex("\\lim_{n\\to20} \\sum_{i=1}^n f(x_i)\\Delta x").to_corner(UR)
        n2_text = MathTex("\\lim_{n\\to100} \\sum_{i=1}^n f(x_i)\\Delta x").to_corner(UR)
        n3_text = MathTex("\\lim_{n\\to\\infty} \\sum_{i=1}^n f(x_i)\\Delta x = \\int_{a}^{b} f(x) \\, dx").to_corner(UR)

        self.play(Create(rects1), Write(n_text))
        self.wait(0.5)
        self.play(ReplacementTransform(rects1, rects2), ReplacementTransform(n_text, n1_text))
        self.wait(0.5)
        self.play(ReplacementTransform(rects2, rects3), ReplacementTransform(n1_text, n2_text))
        self.wait(0.5)
        self.play(ReplacementTransform(rects3, area), ReplacementTransform(n2_text, n3_text))
        self.wait(2)