# Useful Scripts

A collection of scripts I've created and used over time for different purposes.

## `resize_images.py`

### What's The Script Do?

Used to resize a set of images (can either be a single image or directory).

### Why Did I Make This?

An issue I face (*frequently*) as a photographer is attempting to upload old images of mine to my site, and not having them be "web-sized" (i.e. under 1 MB per image and typically `4000px` on the long edge).

In my photography workflow now, I've automated that process so that it automatically creates those, however for historic images of mine I only have the high-resolution JPGs. This serves as a means of automating the creation of web-sized copies.

### Next Steps

- [ ] Add the ability to pass the options (i.e. file-path or whether it's a single file or directory) right to the CLI instead of prompting.
- [ ] Remember previously used value (so a user didn't need to pass in values if they just wanted to re-run it on the same directory).
- [ ] Add usage guide / help option as well as some examples here in the readme.
