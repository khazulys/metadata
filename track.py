import os
from PIL import Image
from PIL.ExifTags import TAGS
import random, time, sys

def tik(s):
	for k in  s + '\n':
		sys.stdout.write(k)
		sys.stdout.flush()
		time.sleep(random.random()*0.2)

try:
	os.system('clear')
	print("	    \033[31;5m\033[4mMETADARA AND OSIF VIEWER\033[0m\n")
	print("\033[31;5m\033[4m\t	Developer khazul\033[0m\n")
	img_file=input("Image file: ")
	tik("Waiting ...")
	time.sleep(3)
	image=Image.open(img_file)

	exif={}

	for tag, value in image._getexif().items():
		if tag in TAGS:
			exif[TAGS[tag]] = value
	print("")
	print("\033[33;5m\tImage informasi\033[0m")
	print("\t================")
	print("\033[35;5m\tCamera\033[0m : \033[36;5m{}\033[0m".format(exif['Make']))
	print("\033[35;5m\tDevice\033[0m : \033[36;5m{}\033[0m".format(exif['Model']))
	print("\033[35;5m\tTime \033[0m  : \033[36;5m{}\033[0m".format(exif['DateTime']))
	print("\033[35;5m\tWidth\033[0m  : \033[36;5m{}cm\033[0m".format(str(exif['ImageWidth'])))
	print("\033[35;5m\tLength\033[0m : \033[36;5m{}cm\033[0m".format(str(exif['ImageLength'])))

	if 'GPSInfo' in exif:
		geo_coordinate='{0} {1} {2:.2f} {3}, {4} {5} {6:.2f} {7}'.format(
			exif['GPSInfo'][2][0][0],
			exif['GPSInfo'][2][1][0],
			exif['GPSInfo'][2][2][0] / exif['GPSInfo'][2][2][1],
			exif['GPSInfo'][1],
			exif['GPSInfo'][4][0][0],
			exif['GPSInfo'][4][1][0],
			exif['GPSInfo'][4][2][0] / exif['GPSInfo'][4][2][1],
			exif['GPSInfo'][3]

			)


		print("\033[32;5m\nlokasi : {}\033[0m".format(geo_coordinate))
		input("\nEnter for exit ")
		exit()

	else:
		print("Information not found!")

except AttributeError:
	print("File is not valid")
