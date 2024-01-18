# handwriting-rating

## Description
 Rate Japanese handwriting using a custom EasyOCR model. 

 Currently using default japanese_g2, which has very poor results for the example images.
 
 Code based off tutorial from <a href="https://talcgames.itch.io/](https://www.youtube.com/watch?v=fGP_sSo-usc" target="_blank" rel="noopener noreferrer">PyImageSearch</a>

## Dataset/Model
 <a href="[https://github.com/Nexdata-AI/101-People-4538-Images-Japanese-Handwriting-OCR-Data](https://jaided.ai/easyocr/modelhub/)" target="_blank" rel="noopener noreferrer">Default EasyOCR japanese_g2 model</a>

## Usage
 python3 character_accuracy.py --image images/1.png --g 1 --langs ja --kana 1 

 --image specify image
 
 --g if gpu should be used 1 or -1
 
 --langs specify languages, normally just use ja
 
 --kana if kana should be used, 1 or -1
 

