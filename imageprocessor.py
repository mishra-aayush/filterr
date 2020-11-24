from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2 
import numpy as np

def select_image():
	# grab a reference to the image panels
	global panelA, panelB, image_path
	# open a file chooser dialog and allow the user to select an input
	# image
	path = filedialog.askopenfilename()
	image_path = path

    # ensure a file path was selected
	if len(path) > 0:
		image = cv2.imread(path)
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		# convert the images to PIL format
		ip_image = Image.fromarray(image)
		ip_image = ip_image.resize((150, 150),Image.ANTIALIAS)
		op_image = Image.fromarray(image)
		op_image = op_image.resize((500, 500),Image.ANTIALIAS)
		# and then to ImageTk format
		ip_image = ImageTk.PhotoImage(ip_image)
		op_image = ImageTk.PhotoImage(op_image)
        # if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store the input image
			panelA = Label(left_frame, image=ip_image, bg='black')
			panelA.image = ip_image
			panelA.grid(row=2, column=0, padx=10, pady=10)
			# while the second panel will store the output image
			panelB = Label(right_frame, image=op_image, bg='black')
			panelB.image = op_image
			panelB.grid(row=0, column=0, padx=10, pady=10)
		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=ip_image)
			panelB.configure(image=op_image)
			panelA.image = ip_image
			panelB.image = op_image

def original():
	try:
		if len(image_path) > 0:
			image = cv2.imread(image_path)
			inv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			# convert the images to PIL format
			inv = Image.fromarray(inv)
			inv = inv.resize((500, 500),Image.ANTIALIAS)
			# and then to ImageTk format
			inv = ImageTk.PhotoImage(inv)
			panelB.configure(image=inv)
			panelB.image = inv
			print("Color Inversion Performed")
	except:
		print('Couldn\'t perform action')

def grayscale():
	try:
		if len(image_path) > 0:
			image = cv2.imread(image_path)
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			# convert the images to PIL format
			gray = Image.fromarray(gray)
			gray = gray.resize((500, 500),Image.ANTIALIAS)
			# and then to ImageTk format
			gray = ImageTk.PhotoImage(gray)
			panelB.configure(image=gray)
			panelB.image = gray
			print("Grayscale Performed")
	except:
		print('Couldn\'t perform action')

def gaussian():
	try:
		if len(image_path) > 0:
			image = cv2.imread(image_path)
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			blur = cv2.GaussianBlur(image, (7, 7), 0)
			# convert the images to PIL format
			blur = Image.fromarray(blur)
			blur = blur.resize((500, 500),Image.ANTIALIAS)
			# and then to ImageTk format
			blur = ImageTk.PhotoImage(blur)
			panelB.configure(image=blur)
			panelB.image = blur
			print("Gaussian Blur Performed")
	except:
		print('Couldn\'t perform action')

def negative():
	try:
		if len(image_path) > 0:
			image = cv2.imread(image_path)
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			neg = cv2.bitwise_not(image)
			# convert the images to PIL format
			neg = Image.fromarray(neg)
			neg = neg.resize((500, 500),Image.ANTIALIAS)
			# and then to ImageTk format
			neg = ImageTk.PhotoImage(neg)
			panelB.configure(image=neg)
			panelB.image = neg
			print("Negative Performed")
	except:
		print('Couldn\'t perform action')

def sepia():
	try:
		if len(image_path) > 0:
			image = cv2.imread(image_path)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			normalized_gray = np.array(gray, np.float32)/255
			sepia = np.ones(image.shape)
			sepia[:, :, 0] = 153 * normalized_gray # B
			sepia[:, :, 1] = 204 * normalized_gray # G
			sepia[:, :, 2] = 255 * normalized_gray # R
			image = np.array(sepia, np.uint8)
			# convert the images to PIL format
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			image = Image.fromarray(image)
			image = image.resize((500, 500),Image.ANTIALIAS)
			# and then to ImageTk format
			image = ImageTk.PhotoImage(image)
			panelB.configure(image=image)
			panelB.image = image
			print("Sepia Performed")
	except:
		print('Couldn\'t perform action')

def edged():
	try:
		if len(image_path) > 0:
			image = cv2.imread(image_path)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			edged = cv2.Canny(gray, 50, 100)
			# convert the images to PIL format
			edged = Image.fromarray(edged)
			edged = edged.resize((500, 500),Image.ANTIALIAS)
			# and then to ImageTk format
			edged = ImageTk.PhotoImage(edged)
			panelB.configure(image=edged)
			panelB.image = edged
			print("Edge Performed")
	except:
		print('Couldn\'t perform action')

def clahe():
	try:
		if len(image_path) > 0:
			image = cv2.imread(image_path)
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			clahe = cv2.createCLAHE(clipLimit=5)
			img_out = clahe.apply(gray) + 30
			# convert the images to PIL format
			img_out = Image.fromarray(img_out)
			img_out = img_out.resize((500, 500),Image.ANTIALIAS)
			# and then to ImageTk format
			img_out = ImageTk.PhotoImage(img_out)
			panelB.configure(image=img_out)
			panelB.image = img_out
			print("Contrast Limited Adaptive Histogram Equalization Performed")
	except:
		print('Couldn\'t perform action')

master = Tk()
master.title('Image Processor')
master.maxsize(1600, 900)
master.config(bg="#FF4136")

panelA = None
panelB = None

left_frame = Frame(master, width=200, height= 400, bg='white')
left_frame.grid(row=0, column=0, padx=100, pady=50)

right_frame = Frame(master, width=650, height=400, bg='white')
right_frame.grid(row=0, column=1, padx=100, pady=50)

Button(left_frame, text="Select Image", command=select_image, bg='#555555', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
Button(left_frame, text="View Original Image", command=original, bg='#555555', fg='white').grid(row=1, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

image1=Image.open('ip.jpg')
ip=ImageTk.PhotoImage(image1)

image2=Image.open('op.jpg')
op=ImageTk.PhotoImage(image2)

Label(left_frame, image=ip, bg='black').grid(row=2, column=0, padx=10, pady=10)
Label(right_frame, image=op, bg='black').grid(row=0, column=0, padx=10, pady=10)

tool_bar = Frame(left_frame, width=180, height=185, bg='white')
tool_bar.grid(row=3, column=0, padx=5, pady=5)

Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=0, padx=5, pady=5)

Button(tool_bar, text="GrayScale", command=grayscale, bg='#555555', fg='white').grid(row=1, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
Button(tool_bar, text="Gaussian Blur", command=gaussian, bg='#555555', fg='white').grid(row=2, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
Button(tool_bar, text="Negative Image", command=negative, bg='#555555', fg='white').grid(row=3, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
Button(tool_bar, text="Sepia Effect", command=sepia, bg='#555555', fg='white').grid(row=4, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
Button(tool_bar, text="Edged", command=edged, bg='#555555', fg='white').grid(row=5, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
Button(tool_bar, text="CLAHE", command=clahe, bg='#555555', fg='white').grid(row=6, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

mainloop()