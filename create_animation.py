---------------------------------------------

from PIL import Image

# 画像を読み込み
frames = [Image.open(path) for path in opaths]

# 最大サイズを決定
max_width = max(frame.width for frame in frames)
max_height = max(frame.height for frame in frames)

# すべてのフレームを最大サイズにリサイズ
resized_frames = []
for frame in frames:
    new_frame = Image.new("RGBA", (max_width, max_height), (255, 255, 255, 255))  # 白背景の新しい画像
    new_frame.paste(frame, ((max_width - frame.width) // 2, (max_height - frame.height) // 2))  # 中央に配置
    resized_frames.append(new_frame)

# GIFとして保存
resized_frames[0].save(
    "animation.gif",
    save_all=True,
    append_images=resized_frames[1:],  
    duration=1000,              
    loop=0             
)
output_path = "animation.gif"

---------------------------------------------

from matplotlib import animation, rc
rc('animation', html='jshtml')

def create_animation(ims):
    fig=plt.figure(figsize=(7,7))
    plt.axis('off')
    im=plt.imshow(cv2.cvtColor(ims[0],cv2.COLOR_BGR2RGB))
    plt.close()
    
    def animate_func(i):
        im.set_array(cv2.cvtColor(ims[i],cv2.COLOR_BGR2RGB))
        return [im]

    return animation.FuncAnimation(fig, animate_func, frames=len(ims), interval=1000/10)

---------------------------------------------

def create_animation_with_text(ims):
    fig = plt.figure(figsize=(4, 4))
    plt.axis('off')
    im = plt.imshow(ims[0])
    text = plt.text(0.05, 0.05, f'Slide {0}', transform=fig.transFigure, fontsize=14)
    plt.close()

    def animate_func(i):
        im.set_array(ims[i])
        text.set_text(f'Slide {i}')
        return [im, text]

    return animation.FuncAnimation(fig, animate_func, frames=len(ims), interval=1000/10)
    
---------------------------------------------

def create_animation(ims):
    fig=plt.figure(figsize=(12,8))
    im=plt.imshow(cv2.cvtColor(ims[0],cv2.COLOR_BGR2RGB))
    text = plt.text(0.05, 0.05, f'Slide {0}', transform=fig.transFigure, fontsize=14, color='blue')
    plt.axis('off')
    plt.close()

    def animate_func(i):
        im.set_array(cv2.cvtColor(ims[i],cv2.COLOR_BGR2RGB))
        text.set_text(f'Slide {20+i}')        
        return [im]    
    
    return animation.FuncAnimation(fig, animate_func, frames=len(ims), interval=1000//10)

create_animation(np.array(images0)[20:])

---------------------------------------------
