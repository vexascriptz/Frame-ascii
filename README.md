# frame/ studio IV

A browser-based image and video to ASCII editor. No server, uploads, accounts, build step or external libraries.

## Workflow

1. Import an image or video, drop a file, paste an image, or try the built-in sample.
2. Choose one of nine visual looks or customize the character mapping and color.
3. Use **Adjust** for levels, tone, dithering and geometry. The source histogram and Auto levels help improve low-contrast footage.
4. Use **Motion** to choose a video frame rate, conversion mode and trim interval. Set in/out from the playhead.
5. Compare ASCII, original or split preview. Export using the format selector.

The editor displays input dimensions, character grid dimensions, and the measured time spent converting and painting the current frame. Save/load look stores one settings preset in your browser's local storage, not your media.

## Studio IV

- Live source-based look thumbnails, graphite workspace, zoom up to 400%, and a responsive canvas.
- Undo/redo for appearance settings, portable JSON look files, and local preset storage.
- Adaptive playback preview and full-resolution export, center crop, and eight-dot Braille rendering with adjustable threshold.
- PNG scaling (1–3×) with optional transparent background; download the last export again.
- Browser-supported MP4/WebM export via MediaRecorder. Recording runs in real time, does not include audio, and may drop frames on slower devices. Format availability is detected in the browser.

## Rendering

- RGB, grayscale, monochrome and duotone.
- Nine looks, seven character ramps (including custom ASCII), calibrated glyph density and directional contours.
- Resolution up to 300 columns, brightness, contrast, gamma, saturation, black and white points, edge enhancement, character aspect, mirroring, custom background and text colors, ordered and error-diffusion dithering, and palette reduction.
- Glyph calibration measures the browser monospace font once per character set; exact appearance varies by browser and terminal font.
- Split comparison and fullscreen (where supported).
- Accurate timestamp seeking or faster 2× playback sampling; fast mode can skip/repeat source frames.

Keyboard: O opens import, C cycles the preview mode, Space plays/pauses video when focus is not on an input or button.

## Exports

| Format | Image | Video |
| --- | --- | --- |
| Python | Colored terminal art | Self-contained animation |
| HTML | Standalone artwork | Standalone animation |
| JSON | Character and RGB data | Character and RGB frame sequence |
| PNG | Raster artwork | Current frame |
| SVG | Editable vector text | Current frame |
| TXT | Plain ASCII | Current frame |
| ANSI | Terminal color text | Current frame |
| Clipboard | Plain ASCII | Current frame |
| MP4 / WebM | — | Real-time recording, browser dependent |

Python 3.8+ with a modern ANSI/true-color terminal is recommended. No pip dependencies. Video Python supports `--loop`, `--speed 2`, and `--no-color`. Python/ANSI use the terminal's background; PNG, SVG and HTML preserve the selected background. Video exports do not contain audio. SVG uses live text and may vary according to installed fonts.

## Deployment

The complete app is in `index.html`. GitHub Pages: Settings → Pages → Deploy from a branch → main → /(root). Local: `python -m http.server 8000`.

## Limitations and verification

Browser media codec support applies. MP4/H.264, WebM, PNG, JPEG and WebP are common choices. Animated images are treated as stills. Animation exports have an estimated 80 MiB uncompressed limit and 12,000-frame cap; trim longer sources or reduce resolution/FPS.

V4 JavaScript syntax and static DOM references checked. Twenty-three automated mock-DOM checks passed for tone mapping, color, histograms, diffusion, contours, calibration, SVG escaping, exports, Braille bit mapping, crop, draft preview and undo/redo. A repeatable Chromium smoke test is included in `tests/smoke.py`. Run `pip install playwright`, `playwright install chromium`, then `python tests/smoke.py` from a local clone. The live browser test has not been executed in this update; visual quality, video recording and device-specific compatibility remain unverified.
