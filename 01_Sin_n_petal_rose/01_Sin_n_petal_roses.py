from manim import *
import numpy as np
config.frame_width=9
config.frame_height=16
config.pixel_width=1080
config.pixel_height=1920
# setting the parametric coordinate system
class SinNPetalRoses(Scene):
    
    def construct(self):
        Title = Tex("Graphs of ","$n$","-petal roses ")
        Title.to_edge(UP)
        self.play(Write(Title))
        Function = MathTex(r"r = a\sin(n\theta)")
        Function.to_edge(UP)
        Function.shift(DOWN*2)
        self.play(Write(Function))
        parametric_coordinate_system = PolarPlane(azimuth_units="PI radians",size=8,radius_max=4).scale(0.8)
        parametric_coordinate_system.add_coordinates()
        self.play(FadeIn(parametric_coordinate_system))
        family_of_curves = VGroup(*[parametric_coordinate_system.plot_polar_graph(lambda theta: np.sin(n*theta),color=YELLOW)for n in range(6)] )
        family_of_curves.scale(3)
        # for n = 1
        details1 = Tex("for ","$n$ ","= 1 ","(1 petal rose)")
        details1.to_edge(DOWN)
        details1.shift(UP*2)
        self.play(Write(details1))
        self.play(Create(family_of_curves[1]),run_time=1.5)
        self.play(FadeOut(family_of_curves[1],details1))
        # for n = 2
        details2 = Tex("for ","$n$ ","= 2 ","(4 petal rose)")
        details2.to_edge(DOWN)
        details2.shift(UP*2)
        self.play(Write(details2))
        self.play(Create(family_of_curves[2]),run_time=1.5)
        self.play(FadeOut(family_of_curves[2],details2))
        # for n = 3
        details3 = Tex("for ","$n$ ","= 3 ","(3 petal rose)")
        details3.to_edge(DOWN)
        details3.shift(UP*2)
        self.play(Write(details3))
        self.play(Create(family_of_curves[3]),run_time=1.5)
        self.play(FadeOut(family_of_curves[3],details3))
        # for n = 4
        details4 = Tex("for ","$n$ ","= 4 ","(8 petal rose)")
        details4.to_edge(DOWN)
        details4.shift(UP*2)
        self.play(Write(details4))
        self.play(Create(family_of_curves[4]),run_time=1.5)
        self.play(FadeOut(family_of_curves[4],details4))

class ThumbnailSinPetal(Scene):
    def construct(self):
        Title = Tex("Graphs of ","$n$","-petal roses ")
        Title.to_edge(UP)
        self.add(Title)
        Function = MathTex(r"r = a\sin(\theta)")
        Function.to_edge(UP)
        Function.shift(DOWN*2)
        self.add(Function)
        parametric_coordinate_system = PolarPlane(azimuth_units="PI radians",size=8,radius_max=4).scale(0.8)
        parametric_coordinate_system.add_coordinates()
        self.add(parametric_coordinate_system)
