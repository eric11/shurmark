# SHURMark Slide Etcher / Labeler Library
A very basic (and incomplete) implementation of the command set for the SHURMark slide labeler as a python library. This is enough for my needs, as it allows us to printer centered lines of text of varying sizes and to increment a serial number, however I've included the full specification in this repository so that the capabilities can be expanded if needed. 

## Requirements
Python 2 with serial library.

## Use Example

```python
import serial
from ShurmarkLib import Shurmark

ser = serial.Serial(
    port='COM9',
    baudrate=9600,
    parity="O",
    xonxoff=True
)

printer = Shurmark(ser)
printer.line("Company", fontsize = 2)
printer.line("Name", fontsize = 2)
printer.line("Product", fontsize=4)
printer.dateline(fontsize = 4)
printer.line("Number 001", fontsize = 4, increment = True)
printer.writeslide(numslides = 10)
ser.close()
```

## License
MIT License

Copyright (c) 2016 Eric H.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
