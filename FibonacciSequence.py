from manim import *
import numpy as np

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

class FibonacciSequence(Scene):
    def construct(self):
        fibText = Text("The Fibonacci Sequence", font_size=30)
        self.play(Write(fibText))
        self.wait(0.75)
        self.play(fibText.animate.to_edge(UP, buff=0.3).scale(0.75))
        self.wait(0.75)

        positions = {}
        positions[0] = (0, 0)
        positions[1] = (1, 0)
        bbox = [0, 0, 2, 1]

        directions = [
            (0, 1), (-1, 0), (0, -1), (1, 0), (0, 1), (-1, 0)
        ]

        for idx, (dx, dy) in enumerate(directions):
            i = idx + 2
            sz = fib(i)
            if dx == 1:
                positions[i] = (bbox[2], bbox[1])
                bbox[2] += sz
            elif dx == -1:
                positions[i] = (bbox[0] - sz, bbox[1])
                bbox[0] -= sz
            elif dy == 1:
                positions[i] = (bbox[0], bbox[3])
                bbox[3] += sz
            elif dy == -1:
                positions[i] = (bbox[0], bbox[1] - sz)
                bbox[1] -= sz

        NUM = 8
        total_w = bbox[2] - bbox[0]
        total_h = bbox[3] - bbox[1]

        available_h = 6.5
        available_w = 12.0
        S = min(available_w / total_w, available_h / total_h)

        cx = (bbox[0] + bbox[2]) / 2
        cy = (bbox[1] + bbox[3]) / 2
        offset_y = -0.6

        fibGroups = []
        for i in range(NUM):
            sz = fib(i)
            bx, by = positions[i]
            center_x = (bx + sz / 2 - cx) * S
            center_y = (by + sz / 2 - cy) * S + offset_y
            side = sz * S

            rect = Rectangle(
                width=side, height=side,
                fill_opacity=0.5, stroke_opacity=1, color=YELLOW
            )
            label = Text(str(sz), font_size=max(12, int(side * 20)))
            label.move_to(rect.get_center())
            group = VGroup(rect, label)
            group.move_to(np.array([center_x, center_y, 0]))
            fibGroups.append(group)

        for group in fibGroups:
            self.play(FadeIn(group), run_time=0.4)

        direction = [1, -1, -1, 1]
        corner = [[UL, -UL], [UR, -UR]]

        arcs = []
        for i in range(NUM):
            rect = fibGroups[i][0]
            c = corner[i % 2]
            d = direction[i % 4]
            arc = ArcBetweenPoints(
                rect.get_corner(c[0]),
                rect.get_corner(c[1]),
                angle=PI / 2 * d,
                color=WHITE,
                stroke_width=2,
            )
            if direction[i % 4] != 1:
                arc = arc.reverse_direction()
            arcs.append(arc)

        self.play(*[Create(arc) for arc in arcs], run_time=2)
        self.wait(1)