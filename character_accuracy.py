# command usage for mac
# python3 character_accuracy.py --image images/1.png --langs ja --kana 1 --g 1

from easyocr import Reader
import argparse
import cv2

def clean_text(text):
    # strip non-ASCII text to draw text on image
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-l", "--langs", type=str, default="ja",
                help="comma separated list of languages to OCR")
ap.add_argument("-g", "--gpu", type=int, default=-1,
                help="whether or not GPU should be used")
ap.add_argument("-k", "--kana", type=str, default="1",
                help="whether or not only kana should be read")
args = vars(ap.parse_args())

# break the input languages into a comma separated list
langs = args["langs"].split(",")
print("[INFO] OCR'ing with the following languages: {}".format(langs))

# load the input image from disk
image = cv2.imread(args["image"])

# OCR the input image using EasyOCR
print("[INFO] OCR'ing input image...")

# hiragana and katakana lists
higragana = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"  
katakana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"

# specify use of japanese_g2
reader = Reader(langs, gpu=args["gpu"] > 0, recog_network='japanese_g2')
# only read kana if specified
if args["kana"] == "1":
    results = reader.readtext(image,slope_ths=0,ycenter_ths=0,height_ths=0,width_ths=0,allowlist=higragana+katakana)
else:
    results = reader.readtext(image,slope_ths=0,ycenter_ths=0,height_ths=0,width_ths=0)


# loop over the results
for (bbox, text, prob) in results:
    # display the OCR'd text and associated probability
    print("[INFO] {:.4f}: {}".format(prob, text))
    
    # unpack the bounding box
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    
    # cleanup the text and draw the box surrounding the text along
    # with the OCR'd text itself
    text = clean_text(text)
    cv2.rectangle(image, tl, br, (0, 255, 0), 2)
    cv2.putText(image, text+str(round(prob,2)), (bl[0], bl[1]-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
# show output image
cv2.imshow("Image", image)
cv2.waitKey(0)
