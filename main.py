import shutil, pathlib
src = pathlib.Path(__file__).parent / "cutest.png"
out = pathlib.Path("/output"); out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out / "entry.png")
