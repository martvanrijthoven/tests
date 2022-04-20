import os

class TestOpenslide:
    def test_import_openslide(self):
        if os.name == 'nt':
            _dll_path = os.getenv('OPENSLIDE_PATH')
            if _dll_path is not None:
                if hasattr(os, 'add_dll_directory'):
                    # Python >= 3.8
                    with os.add_dll_directory(_dll_path):
                        print('import openslide on windows')
                        import openslide
                else:
                    raise ValueError('Python>=3.8 required')
        else:
            print('import openslide on non-windows')
            import openslide

