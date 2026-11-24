# frame/ — video to ASCII

A static, local-first video-to-ASCII converter. No backend, API key, account, build step or dependency installation. The website uses JavaScript because GitHub Pages hosts static files; its Python export is a self-contained program with embedded animation data.

## GitHub Pages

1. Create a GitHub repository (for example, `frame-ascii`).
2. Upload `index.html`, `style.css`, `app.js` and `.nojekyll` to the repository root. You can alternatively use the standalone HTML file by itself, renamed to `index.html`.
3. Open **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, and select `main` and `/(root)`. Save.
4. GitHub will show your published URL when the deployment completes.

Local development: run `python -m http.server 8000` in the project directory and open `http://localhost:8000`.

## Conversion

- Select or drag in a video, then play, pause, seek or toggle its original audio.
- Choose RGB, grayscale, or monochrome, character density, contrast, resolution and export frame rate.
- Use the start/end fields to export only a section, particularly for longer videos.
- Export a standalone Python animation, a standalone HTML animation, or a plain text frame (no color in plain text).

## Python playback

The generated Python file embeds the ASCII frames and RGB data. No original video or pip dependencies are required. Open a modern ANSI/true-color terminal such as Windows Terminal, macOS Terminal/iTerm2, or a Linux terminal. Run:

```sh
python video-ascii.py
python video-ascii.py --loop
python video-ascii.py --speed 2
python video-ascii.py --no-color
```

Use Ctrl+C to stop. The player fits the animation to the terminal dimensions. Python 3.8+ is recommended.

## Limits

The browser must support the video container and codec. MP4 (H.264) and WebM are generally good choices. Unsupported codecs must be transcoded before importing. Exports contain sampled visual frames, not audio. Full-length videos at high resolution can generate very large files; the site limits estimated uncompressed export size to 100 MiB and frame count to 18,000. Export settings apply to generated animations, while live preview follows the video. Performance depends on device and browser.

## Verification

Browser smoke test using a one-second synthetic WebM: import, playback, Python/HTML/TXT downloads and HTML playback. Generated Python passed compilation and executed in a pseudo-terminal with ANSI RGB output. The browser sandbox blocked direct file and localhost navigation, so the test loaded the same page markup and script directly. Actual GitHub Pages deployment and mobile browser compatibility have not been tested.
