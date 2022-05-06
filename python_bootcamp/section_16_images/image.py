from PIL import Image

mac = Image.open('python_bootcamp/section_16_images/example.jpeg')

mac.show()

print(mac.size)
print(mac.filename)
print(mac.format_description)

mac.crop((0,0,100,100)).show()
mac.rotate(90).show()
mac.resize((500, 500)).show()
