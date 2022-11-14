# QRcode

## _Generate QRcode_

[![qrcode](https://github.com/bensuperpc/qrcode/actions/workflows/base.yml/badge.svg)](https://github.com/bensuperpc/qrcode/actions/workflows/base.yml)

![GitHub top language](https://img.shields.io/github/languages/top/bensuperpc/qrcode) ![GitHub](https://img.shields.io/github/license/bensuperpc/qrcode)

## Features

- Generate QRcode from text
- Image in center of QRcode
- Change error correction level

## Usage

Usage of qrcode:

```sh
python3 qrcode_generator.py --data <Text or URL> --image <Image path> --error_correction <error correction level> --box_size <box size> --border <border size> ...
```

Or with double quote (Recommended if you have space in your text)

```sh
python3 qrcode_generator.py --data "<Text or URL>" --image "<Image path>" --error_correction "<error correction level>"
```

## Example

Generate QRcode from URL (eg: wikipedia.org)

```sh
python3 qrcode_generator.py --data https://www.wikipedia.org/
```

Generate QRcode from text with image in center

```sh
python3 qrcode_generator.py --data "Hello World" --image image.png
```

Generate QRcode from text with max error correction level

```sh
python3 qrcode_generator.py --data "Hello World" --error_correction H
```

Generate QRcode from text with box size 10 and border 4

```sh
python3 qrcode_generator.py --data "Hello World" --box_size 10 --border 4
```

Generate QRcode from text with blue color and white background

```sh
python3 qrcode_generator.py --data "Hello World" --color "blue" --background "white"
```

## Error correction level

- L: 7% of codewords can be restored.
- M: 15% of codewords can be restored.
- Q: 25% of codewords can be restored.
- H: 30% of codewords can be restored.

## Open source projects used

- [python-qrcode](https://github.com/lincolnloop/python-qrcode)
- [Pillow](https://github.com/python-pillow/Pillow)
- [python](https://www.python.org/)

## Licensing

[MIT License](LICENSE)
