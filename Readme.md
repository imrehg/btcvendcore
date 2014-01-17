# Bitcoin vending machine controller

Control code for a bitcoin vending machine: taking fiat,
and sending bitcoin.

## Hardware

* [ICT XBA bill acceptor][xba]
* [ICT GP-58IV thermal printer][thermal], though any other ESC/POS compatible printer should work

## Requirements

* Python 2.7.x
* [python-escpos][escpos], library to manipulate ESC/POS Printers.
* [zbar][zbar], barcode reader

## License

TL;DR: BSD 3-clause license

Copyright (c) 2014, Gergely Imreh <gergely@imreh.net>
All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are 
met:

1. Redistributions of source code must retain the above copyright 
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright 
notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution.

3. The names of its contributors may be used to endorse or promote
products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS 
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED 
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[xba]: http://www.ictgroup.com.tw/index.php?option=com_content&view=article&id=480&catid=35&Itemid=325
[thermal]: http://www.ictgroup.com.tw/index.php?option=com_content&view=article&id=56&Itemid=63
[escpos]: https://code.google.com/p/python-escpos/
[zbar]: http://zbar.sourceforge.net/
