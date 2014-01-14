#Sublime Transmit DockSend

*supports OS X only*

Altered version of the Transmit Docksend plugin. For the general idea see:
[https://github.com/jeffturcotte/sublime_transmit_docksend](https://github.com/jeffturcotte/sublime_transmit_docksend)

Transmit Docksend Extras builds on Transmit Docksend by adding new commands for uploading CSS files along with their SCSS counterparts. 

## Installation

Clone this repository into a "Transmit Docksend Extras" folder in the ST2 Packages directory.

	git clone git://github.com/inspyre/sublime_transmit_docksend_extras.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Transmit\ Docksend\ Extras

## Usage

### DockSend Compiled Style
Use "super+k", "ctrl+u" or `Transmit DockSend Compiled Style` (Command Pallete) to DockSend the current open file. If the file extension is .scss then a .css file with the same file (base) name, if located in the same directory, will also be uploaded.

### DockSend Compiled Style File
Use "super+k", "super+ctrl+u" or `Transmit DockSend Compiled Style File` (Command Pallete) to DockSend the current open file. If the file extension is .scss then a style.css file, if located in the same directory, will also be uploaded.

## License

  Copyright (c) 2011 Jeff Turcotte <jeff.turcotte@gmail.com>

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
