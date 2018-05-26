from pathlib import Path

from PIL import Image

from pelican import signals
from pelican.readers import MarkdownReader

NIM_MAX_HEIGHT = 350
NIM_MIN_PREFIX = 'min_'
NIM_EXT = ['jpg', 'png']


def create_miniature(pelican):
    """
    Finds all files ending with NIM_EXT, and create a minified version with NIM_MAX_HEIGHT prefixed with NIM_MIN_PREFIX
    """
    output_path = Path(pelican.settings['OUTPUT_PATH']) / 'images'
    for ext in NIM_EXT:
        for image in output_path.glob(f'*/*.{ext}'):
            min_name = image.parent / f'{NIM_MIN_PREFIX}{image.name}'
            if image.stem.startswith(NIM_MIN_PREFIX) or min_name.exists():
                continue
            im = Image.open(image)
            im = im.resize((round(NIM_MAX_HEIGHT * im.size[0] / im.size[1]), NIM_MAX_HEIGHT), Image.LANCZOS)
            im.save(min_name)


def register():
    signals.finalized.connect(create_miniature)
