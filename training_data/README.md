Getting Training Data
=====================

The files in here are used to retrieve suitable training data images from google image search and put them into the training data folder.  The images are not archived, both because they're huge, but also because we don't own the copyright on them so we can't distribute them.  If you choose to replicate this then please be aware of the limitations in the use of such downloaded
images.

Download package
----------------

The image retrieval makes use of the python [Google Images Download](https://google-images-download.readthedocs.io/en/latest/index.html) package.  However at the time of writing there is a [bug](https://github.com/hardikvasa/google-images-download/issues/354) in the package which means it doesn't download anything.  I was therefore using [this fork](https://github.com/Joeclinton1/google-images-download) which contained a fix and was working again. Hopefully the fix will be rolled into the main line again so you can use the version of the package in pypi and install it with ```pip install google-images-download``` but check if it doesn't work for you.

