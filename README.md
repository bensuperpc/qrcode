# QRcode

## _Generate QRcode_

[![qrcode](https://github.com/bensuperpc/qrcode/actions/workflows/base.yml/badge.svg)](https://github.com/bensuperpc/qrcode/actions/workflows/base.yml)

![GitHub top language](https://img.shields.io/github/languages/top/bensuperpc/qrcode) ![GitHub](https://img.shields.io/github/license/bensuperpc/qrcode)

[![Twitter](https://img.shields.io/twitter/follow/Bensuperpc?style=social)](https://img.shields.io/twitter/follow/Bensuperpc?style=social) [![Youtube](https://img.shields.io/youtube/channel/subscribers/UCJsQFFL7QW4LSX9eskq-9Yg?style=social)](https://img.shields.io/youtube/channel/subscribers/UCJsQFFL7QW4LSX9eskq-9Yg?style=social)

## Features

- Generate QRcode from text
- Image in center of QRcode
- Change error correction level

## Usage

Usage of qrcode:

```sh
python3 qrcode_generator.py -url <Text or URL> -i <Image path> -e <error correction level>
```

or with double quote

```sh
python3 qrcode_generator.py -url "<Text or URL>" -i "<Image path>" -e "<error correction level>"
```

## Example

Generate QRcode from URL (eg: wikipedia.org)

```sh
python3 qrcode_generator.py -url https://www.wikipedia.org/
```

Generate QRcode from text (eg: Hello World) with image in center

```sh
python3 qrcode_generator.py -url "Hello World" -i image.png
```

Generate QRcode from text (eg: Hello World) with max error correction level

```sh
python3 qrcode_generator.py -url "Hello World" -e H
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
