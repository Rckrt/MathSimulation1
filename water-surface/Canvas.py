
from vispy import app
from vispy import gloo

import shaders
from Surface import Surface

class Canvas(app.Canvas):

    def __init__(self, size=(600, 600)):
        self.width = size[0]
        self.height = size[1]

        self.time = 0

        app.Canvas.__init__(self, size=(self.width, self.height), title='Water surface simulator')

        gloo.set_state(clear_color=(0, 0, 0, 1), depth_test=False, blend=False)

        self.surface = Surface()

        self.program = gloo.Program(shaders.vert_shader, shaders.frag_shader)
        self.program['a_position'] = self.surface.position()
        self.program['a_height'] = self.surface.height()

        self.timer = app.Timer('auto', connect=self.on_timer, start=True)
        self.activate_zoom()
        self.show()

    def activate_zoom(self):
        self.width, self.height = self.size
        gloo.set_viewport(0, 0, *self.physical_size)

    def on_draw(self, event):
        gloo.clear()

        self.program['a_height'] = self.surface.height(self.time)

        self.program.draw('points')

    def on_timer(self, event):
        self.time += 0.01
        self.update()

    def on_resize(self, event):
        self.activate_zoom()
