import glob
import imageio

with imageio.get_writer('moistureanimation.gif', mode='I') as writer:
    for filename in sorted(glob.glob('*.jpg'), key=len):
        image = imageio.v2.imread(filename)
        writer.append_data(image)
##############################
### RAVESHE DOVOM

# from PIL import Image
#
# frames = []
# imgs = glob.glob("*.jpg")
# for i in imgs:
#     new_frame = Image.open(i)
#     frames.append(new_frame)
#
# # Save into a GIF file that loops forever
# frames[0].save('png_to_gif.gif', format='GIF',append_images=frames,save_all=True)