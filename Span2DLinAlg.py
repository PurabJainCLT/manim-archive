from manim import *

# manim -pqh Span2DLinAlg.py Span2DLinAlg

class Span2DLinAlg(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-50, 50],
            y_range=[-50, 50],
            x_length=50,
            y_length=50,
            background_line_style={"stroke_opacity": 0}
        ).add_coordinates()
        self.play(Create(plane))
        vec = Vector((1,2), color=BLUE)
        vecSpan = Line(start=(-4,-8,0), end=(4,8,0), color=WHITE)
        vecSpan.z_index = 0
        vec.z_index = 1
        t_vec = MathTex(r"\begin{pmatrix} 1 \\ 2 \end{pmatrix}",font_size=30).next_to(vec.get_end(), RIGHT)
        t_vecSpan = MathTex(r"span\{\begin{pmatrix} 1 \\ 2 \end{pmatrix}\}", font_size=30).next_to(vec.get_end(), RIGHT)
        self.play(Create(vec), Write(t_vec))
        self.play(Create(vecSpan), ReplacementTransform(t_vec,t_vecSpan))
        self.wait(2)