mkdir -p c:\\openslide
cd c:\\openslide
curl -LO "https://github.com/openslide/openslide-winbuild/releases/download/v20171122/openslide-win64-20171122.zip"
7z x openslide-win64-20171122.zip
setx OPENSLIDE_PATH "c:\\openslide\\openslide-win64-20171122\\bin"