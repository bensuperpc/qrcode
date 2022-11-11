import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer

from loguru import logger
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    parser.add_argument("-i", "--image", default=None,
                        help="image to be used as logo")
    parser.add_argument("-url", "--url", default=None,
                        help="url to be encoded")
    parser.add_argument("--error_correction", default="H", nargs="?",
                        help="QRcode error correct levels: L: 7%, M: 15%, Q: 25%, H: 30%")
    parser.add_argument(
        "-o", "--output", default="qrcode.png", help="output file, default is qrcode.png")

    args = parser.parse_args()
    
    # Map error correction levels to qrcode constants
    error_correction_levels = {
        "L": "ERROR_CORRECT_L",
        "M": "ERROR_CORRECT_M",
        "Q": "ERROR_CORRECT_Q",
        "H": "ERROR_CORRECT_H"
    }

    if args.url is None:
        logger.error("No url provided")
        return

    if args.image is None:
        logger.debug("No image provided, no logo will be embedded")
    else:
        logger.debug(f"Image provided, logo will be embedded: {args.image}")
    
    logger.debug(f"QRcode error correct level: {args.error_correction} : {getattr(qrcode.constants, error_correction_levels[args.error_correction])}")
    logger.debug(f"QRcode output file: {args.output}")

    qr = qrcode.QRCode(
        version=None,
        error_correction=getattr(qrcode.constants, error_correction_levels[args.error_correction]),
        box_size=15,
        border=4,
    )

    qr.add_data(args.url)
    qr.make(fit=True)

    img = None

    if args.image is None:
        img = qr.make_image(fill_color="black", back_color="white")
    else:
        img = qr.make_image(fill_color="black", back_color="white", image_factory=StyledPilImage,
                            module_drawer=SquareModuleDrawer(), embeded_image_path=args.image)

    img.save(args.output)

    logger.success(f"QRcode saved to {args.output}")


if __name__ == "__main__":
    main()
