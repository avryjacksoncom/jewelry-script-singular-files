I had a folder with about 12,000 image files. Some of these images had alternate versions 
(like edits or variations), and others were just single, standalone files.

My task was to delete the images that only had one version—basically, get rid of any image 
that didn’t have duplicates.

To do this, I used the tags in the filenames. First, I parsed and extracted the first two tags 
from each filename to group similar images. Then I ran another check using just the first tag, 
because some duplicates still remained after the first pass.

After grouping the files, I identified which ones were truly singular (no other versions with the same tag).
I marked these files by storing their indexes in an array.

Finally, I looped through the marked list and deleted those single-version files.

In the end, I removed about 197 standalone images from the folder.
