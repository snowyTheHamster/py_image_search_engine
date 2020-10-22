# Compare image similarities using python and opencv

A script that when provided an reference image will search for similar images in a given folder.

## installation

- install python, set up virtual env, install required modules.

```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## preparation

- prepare a folder with a bunch of images you want to search
- Add a reference image in the same folder

## launch script

run the gui app to launch the script:

```
python gui.py
```

A gui will pop up where you can specify the **reference image**, the **target folder** and 
the mode of the image comparison algorithm.

The results will show in the window & saved to **results.csv** where the gui script was run.