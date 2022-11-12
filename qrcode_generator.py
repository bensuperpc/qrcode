import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer

from loguru import logger
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("--verbose", action="store_true",
                        help="increase output verbosity")
    parser.add_argument("--image", default=None,
                        help="image to be used as logo")
    parser.add_argument("--data", default=None,
                        help="data to be encoded")
    parser.add_argument("--error_correction", default="H", nargs="?",
                        help="QRcode error correct levels: L: 7%, M: 15%, Q: 25%, H: 30%")
    parser.add_argument(
        "-o", "--output", default="qrcode.png", help="output file, default is qrcode.png")

    parser.add_argument("--box_size", default=15, type=int,
                        help="box size of each module, default is 15")

    parser.add_argument("--border", default=4, type=int,
                        help="border size, default is 4")

    parser.add_argument("--version", default=None, type=int,
                        help="QRcode version (int), default is None")

    parser.add_argument("--color", default="black", nargs="?",
                        help="QRcode color, default is black")

    parser.add_argument("--background", default="white", nargs="?",
                        help="QRcode background color, default is white")

    parser.add_argument("--fit", default=True, type=bool,
                        help="fit image into QRcode, default is True")

    args = parser.parse_args()

    # Map error correction levels to qrcode constants
    error_correction_levels = {
        "L": "ERROR_CORRECT_L",
        "M": "ERROR_CORRECT_M",
        "Q": "ERROR_CORRECT_Q",
        "H": "ERROR_CORRECT_H"
    }

    if args.data is None:
        logger.error("No data provided")
        return

    if args.image is None:
        logger.debug("No image provided, no logo will be embedded")
    else:
        logger.debug(f"Image provided, logo will be embedded: {args.image}")

    logger.debug(
        f"QRcode error correct level: {args.error_correction} : {getattr(qrcode.constants, error_correction_levels[args.error_correction])}")
    logger.debug(f"QRcode output file: {args.output}")

    logger.debug(f"QRcode box size: {args.box_size}")
    logger.debug(f"QRcode border: {args.border}")
    logger.debug(f"QRcode version: {args.version}")
    logger.debug(f"QRcode color: {args.color}")
    logger.debug(f"QRcode background: {args.background}")
    logger.debug(f"QRcode fit: {args.fit}")

    qr = qrcode.QRCode(
        version=args.version,
        error_correction=getattr(
            qrcode.constants, error_correction_levels[args.error_correction]),
        box_size=args.box_size,
        border=args.border,
    )

    qr.add_data(args.data)

    qr.make(fit=args.fit)

    img = None

    if args.image is None:
        img = qr.make_image(fill_color=args.color, back_color=args.background)
    else:
        img = qr.make_image(fill_color=args.color, back_color=args.background, image_factory=StyledPilImage,
                            module_drawer=SquareModuleDrawer(), embeded_image_path=args.image)

    img.save(args.output)

    logger.success(f"QRcode saved to {args.output}")


if __name__ == "__main__":
    main()
