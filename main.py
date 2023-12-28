import sys
import package.app as app
import package.globalargs as gl

if __name__ == "__main__":
    if "debug" in sys.argv:
        gl.debug = True
    app.create_ui()
