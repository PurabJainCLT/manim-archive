import numpy as np
from manim import *

# manim -pql Span3DLinAlg.py Span3DLinAlg

class Span3DLinAlg(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes()
        label_x = axes.get_x_axis_label("x")
        label_y = axes.get_y_axis_label("y")
        label_z = axes.get_z_axis_label("z")
        plane = VGroup(axes, label_x, label_y, label_z)
        self.add(plane)

        v1 = np.array([1/5, 2/5, 3/5])
        v2 = np.array([4/5, 5/5, 6/5])
        vec1 = Arrow3D(start=ORIGIN,end=v1,color=BLUE)
        vec2 = Arrow3D(start=ORIGIN,end=v2,color=BLUE)
        v1_n = v1 / np.linalg.norm(v1)
        v2_proj = np.dot(v2, v1_n) * v1_n
        v2_orth = v2 - v2_proj
        v2_n = v2_orth / np.linalg.norm(v2_orth)
        vec_span = Polygon(v1_n * -3 + v2_n * -3,
                           v1_n *  3 + v2_n * -3,
                           v1_n *  3 + v2_n *  3,
                           v1_n * -3 + v2_n *  3,
                           color=BLUE,
                           fill_opacity=0.4
                           )

        t_vec = MathTex(r"W = \Bigg\{\begin{pmatrix} 1 \\ 2 \\ 3\end{pmatrix},\begin{pmatrix} 4 \\ 5 \\ 6\end{pmatrix}\Bigg\}",font_size=30).to_corner(UR)
        t_vec_span = MathTex(r"\text span(W) = \text span(\Bigg\{\begin{pmatrix} 1 \\ 2 \\ 3\end{pmatrix},\begin{pmatrix} 1 \\ 2 \\ 3\end{pmatrix}\Bigg\})",font_size=30).to_corner(UR)
        self.add_fixed_in_frame_mobjects(t_vec)
        self.play(Create(vec1),Create(vec2),Write(t_vec))
        self.wait(3)
        self.play(Create(vec_span),ReplacementTransform(t_vec,t_vec_span))
        self.add_fixed_in_frame_mobjects(t_vec_span)
        self.wait(0.5)
        self.begin_ambient_camera_rotation(rate=0.8)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.wait(2)

