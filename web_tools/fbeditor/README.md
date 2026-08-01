# Offline HTML5 Editor

[Source](https://github.com/mariuscomper/fbeditor)

A powerful, feature-rich offline HTML editor that runs entirely in your browser. No server required, no installation needed - just open and start editing.

## Features

### Core Editing

- **Dual-pane interface**: Side-by-side HTML source and live preview
- **Live preview**: See your changes in real-time as you type
- **Always editable preview**: Edit directly in the preview pane using contentEditable
- **Auto-sync**: Changes in preview automatically sync back to source code

### File Management

- **New/Open/Save**: Standard file operations for HTML documents
- **Auto-save indicator**: Visual feedback when document has unsaved changes
- **Extract body content**: When opening full HTML documents, automatically extracts just the body content

### Text Processing & Cleaning

- **Clean HTML**: Comprehensive cleaning that:
  - Removes "opens in new tab" text and similar noise
  - Strips Reuters-style ticker codes (e.g., AAPL.O)
  - Removes external link icons and glyphs
  - Eliminates newsletter CTAs and divider lines
  - Decodes HTML entities
  - Normalizes whitespace and formatting
  - Converts plain text to proper paragraphs

- **Format HTML**: Applies consistent formatting with proper newlines between elements
- **Convert Entities**: Decodes HTML entities to their character equivalents
- **Format Line Breaks**: Converts single line breaks to double, creating proper paragraph structure

### Text Transformation

- **Case Conversion** (works on selected text):
  - Sentence case
  - lowercase
  - UPPERCASE
  - Title Case

- **CAPITALIZE Acronyms**: Automatically capitalizes common acronyms (NATO, FBI, HTML, etc.)
- **Undo Caps**: Reverts the last acronym capitalization
- **Wrap Quotes**: Wraps selected text or entire content with fancy quotation marks (❝ ❞)

### Find & Replace

- **Find Next**: Search through your document with match highlighting
- **Replace**: Replace individual occurrences one at a time
- **Replace All**: Replace all matches at once
- **Case-sensitive search**: Optional case sensitivity
- **Regular expressions**: Support for advanced regex patterns
- **Live match counter**: Shows "Match X of Y" as you search

### Smart Paste

- **URL Detection**: Automatically detects URLs when pasted
  - Adds URL to the share field
  - Inserts a clickable link into the document
  - Works anywhere in the editor
- **Text Formatting**: Automatically formats pasted text into paragraphs

### Social Sharing

- **Share on Facebook**: Quickly share URLs to Facebook
- **Archive URLs**: Open clean, archived versions via archive.ph (removes tracking parameters)

### Customization

- **Adjustable font size**: Increase/decrease source code font size
- **Toggle preview**: Hide preview pane for full-width source editing
- **Statistics**: Real-time character, word, and line counts

## Keyboard Shortcuts

| Shortcut       | Action                     |
| -------------- | -------------------------- |
| `Ctrl+S`       | Save document              |
| `Ctrl+N`       | New document               |
| `Ctrl+F`       | Open Find & Replace        |
| `Ctrl+Shift+C` | Clean HTML                 |
| `Ctrl+Shift+Q` | Wrap selection with quotes |
| `Escape`       | Close Find & Replace modal |

## Usage

### Getting Started

1. Open `updated-html-editor GOOD.html` in any modern web browser
2. Start typing in the preview pane or paste content
3. The HTML source updates automatically in the left pane

### Typical Workflow

1. **Paste content** from an article or webpage
2. **Click "Clean HTML"** to remove noise and formatting issues
3. **Use "CAPITALIZE Acronyms"** to fix common acronyms
4. **Format and edit** as needed
5. **Save** your cleaned HTML

### Working with URLs

- Paste a URL anywhere to automatically populate the share field
- Use **Share on FB** to quickly share articles
- Use **Open Archive** to view clean, archived versions without tracking

### Find & Replace Examples

- Simple text replacement: Find "color", replace with "colour"
- Case-sensitive: Enable checkbox to match exact case
- Regex patterns: Find `\d+px`, replace with `1rem` (converts pixels to rem)

## Technical Details

### Browser Compatibility

- Works in all modern browsers (Chrome, Firefox, Safari, Edge)
- Uses standard web APIs: FileReader, Blob, contentEditable
- No external dependencies

### Architecture

- **Single-file application**: Everything in one HTML file
- **Offline-first**: No internet connection required
- **No server needed**: Runs entirely in the browser
- **Sandboxed preview**: Uses iframe with `sandbox="allow-same-origin"` for security

### Smart HTML Processing

The editor includes sophisticated text processing:

- Inline element preservation (doesn't break spacing in links, spans, etc.)
- Intelligent whitespace normalization
- Noise pattern detection for common CTA phrases
- Reuters ticker code removal
- Automatic paragraph wrapping for plain text

## Privacy & Security

- **100% Local**: All processing happens in your browser
- **No tracking**: No analytics or external requests
- **No uploads**: Your content never leaves your computer
- **Safe preview**: Sandboxed iframe prevents script execution

## Use Cases

- Cleaning up copied web content
- Preparing content for CMS systems
- Removing formatting from pasted text
- Quick HTML prototyping
- Article preparation and editing
- Stripping tracking parameters from shared links
- Batch text transformations with Find & Replace

## Advanced Features

### Acronym Capitalization

Includes an extensive list of common acronyms across multiple categories:

- Organizations (NATO, FBI, CIA, UN, EU)
- Media (CNN, BBC, NPR, HBO)
- Technology (HTML, CSS, API, JSON, HTTP)
- Business (CEO, CFO, CTO, ROI, KPI)
- Medical (AIDS, HIV, PTSD, ADHD)
- And many more...

### Content Cleaning Patterns

Automatically removes:

- "Sign up for newsletter" prompts
- "Opens in new tab" annotations
- Social media share prompts
- Divider lines (----, ====, etc.)
- Short CTA phrases under 120 characters
- External link icons

## Tips & Tricks

1. **Paste directly into preview**: The preview pane is focused on load for quick pasting
2. **Use Clean HTML liberally**: It's designed to be safe and won't damage your content
3. **Regex power user**: Enable regex in Find & Replace for advanced pattern matching
4. **Font size adjustment**: Use +/- buttons if source text is too small/large
5. **Copy all text**: Quickly extract just the text content without HTML tags

## Contributing

This is a standalone HTML file. To modify:

1. Open in any text editor
2. Edit the HTML, CSS, or JavaScript sections
3. Save and refresh in browser to test

## License

Free to use and modify for any purpose.

## Credits

A comprehensive offline HTML editor designed for content creators, writers, and developers who need a powerful, privacy-focused tool for HTML editing and content cleaning.
