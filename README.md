# frame/ studio

A browser-based image and video to ASCII editor. No server, uploads, accounts, build step or external libraries.

## Workflow

1. Import an image or video, drop a file, paste an image, or try the built-in sample.
2. Choose one of nine visual looks or customize the character mapping and color.
3. Use **Adjust** for levels, tone, dithering and geometry. The source histogram and Auto levels help improve low-contrast footage.
4. Use **Motion** to choose a video frame rate, conversion mode and trim interval. Set in/out from the playhead.
5. Compare ASCII, original or split preview. Export using the format selector.

The editor displays input dimensions, character grid dimensions, and the measured time spent converting and painting the current frame. Save/load look stores one settings preset in your browser's local storage, not your media.

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

Python 3.8+ with a modern ANSI/true-color terminal is recommended. No pip dependencies. Video Python supports `--loop`, `--speed 2`, and `--no-color`. Python/ANSI use the terminal's background; PNG, SVG and HTML preserve the selected background. Video exports do not contain audio. SVG uses live text and may vary according to installed fonts.

## Deployment

The complete app is in `index.html`. GitHub Pages: Settings → Pages → Deploy from a branch → main → /(root). Local: `python -m http.server 8000`.

## Limitations and verification

Browser media codec support applies. MP4/H.264, WebM, PNG, JPEG and WebP are common choices. Animated images are treated as stills. Animation exports have an estimated 80 MiB uncompressed limit and 12,000-frame cap; trim longer sources or reduce resolution/FPS.

V3 JavaScript syntax and static DOM references checked. Fifteen automated mock-DOM logic checks passed for tone mapping, color, histograms, diffusion, contours, density calibration, SVG escaping, and export generation. No live browser or mobile end-to-end test or visual review was performed in this update; speed and device compatibility are not benchmarked.
