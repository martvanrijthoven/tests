import os

class TestOpenslide:
    def test_import_openslide(self):
        if os.name == 'nt':
            _dll_path = os.getenv('OPENSLIDE_PATH')
            print(_dll_path)
            # Python >= 3.8
            with os.add_dll_directory(_dll_path):
                print('import openslide on windows')
                import openslide

        else:
            print('import openslide on non-windows')
            import openslide

