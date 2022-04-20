import os

class TestOpenslide:
    def test_import_openslide(self):
        if os.name == 'nt':
            with os.add_dll_directory("c:\\openslide\\openslide-win64-20171122\\bin"):
                print('import openslide on windows')
                import openslide
        else:
            print('import openslide on non-windows')
            import openslide

