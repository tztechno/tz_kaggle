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
