!pip install pyvpx

import vpx

input_file = 'input.webm'
reader = vpx.WebmReader(input_file)

output_dir = 'frames/'
frame_index = 1

while True:
    frame = reader.get_frame()
    if frame is None:
        break
    output_file = f'{output_dir}/frame_{frame_index:04d}.png'
    frame.save(output_file)
    frame_index += 1
