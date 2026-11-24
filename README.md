# frame/ — image and video to ASCII

A static, local-first converter for images and videos. No backend, API keys, accounts, build step or dependencies. Media stays in your browser.

## Use

Open the site, choose or drop an image/video, or paste an image. Pick an appearance preset, adjust the controls, and compare the original with the ASCII preview. For videos, play, pause, seek, trim, and select the frame rate.

### Appearance

- Six presets: Balanced, High detail, Classic terminal, Pixel blocks, Soft color, Green binary.
- RGB, grayscale and custom single-color text.
- Adjustable resolution, brightness, contrast, gamma, saturation, edge enhancement, character aspect, ordered dithering, RGB palette and background.
- Seven character-set choices including custom printable ASCII.
- Transparent images are composited onto the selected background.

### Export

| Format | Image | Video |
| --- | --- | --- |
| Python (.py) | Colored terminal artwork | Self-contained animation |
| HTML | Standalone artwork | Standalone animation |
| PNG | Rendered artwork | Current frame |
| TXT | Plain ASCII | Current frame |
| ANSI | Colored terminal text | Current frame |
| Clipboard | Plain ASCII | Current frame |

Python requires Python 3.8+ and no external libraries. A modern true-color terminal is recommended. Video Python exports support `--loop`, `--speed 2` and `--no-color`. The Python and ANSI exports use the terminal's own background; the preview, PNG and HTML use your selected background. Animation exports do not include audio.

Accurate mode seeks to each requested timestamp. Fast mode samples during 2× playback and can repeat or skip source frames, depending on the browser and device. Preview frame rate follows the FPS control. Python video data is gzip-compressed when the browser supports CompressionStream; monochrome frames omit RGB data.

## Host on GitHub Pages

The entire application is in `index.html`. In repository Settings → Pages, select Deploy from a branch, `main`, and `/(root)`. Local testing: `python -m http.server 8000` and open http://localhost:8000.

## Limits and verification

The browser must support the source codec. MP4/H.264, WebM, PNG, JPEG and WebP are common choices. Animated images are treated as still images. The app limits large animation exports to an estimated 80 MiB of uncompressed data and 12,000 frames; lower FPS, resolution or trim duration for long videos.

Version 2 automated JavaScript checks cover parsing, RGB and grayscale conversion, monochrome packing, inversion, transparency, image geometry, text and ANSI output, image Python generation, and generated HTML script syntax. These are logic checks with a mock DOM, not a live browser or mobile end-to-end test. Actual Pages deployment and device-specific codecs/playback remain to be verified.
