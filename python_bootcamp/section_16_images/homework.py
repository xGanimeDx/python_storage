from PIL import Image

word_matrix = Image.open('python_bootcamp/section_16_images/word_matrix.png')
mask = Image.open('python_bootcamp/section_16_images/mask.png')

mask = mask.resize(word_matrix.size)
mask.putalpha(200)

word_matrix.paste(mask, (0, 0), mask)

word_matrix.show()
