
from Canvas import Canvas
from vispy import app
from surface import Surface
from surface import CircularWavesSurface

if __name__ == '__main__':
    c = Canvas(CircularWavesSurface.CircularWavesSurface(max_height=0.02), size=(700, 700))
    app.run()
