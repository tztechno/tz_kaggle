#################################

plt.figure(figsize = (15,10))
plt.imshow(image)
plt.axis('off')
plt.show()


#################################

fig, ax = plt.subplots(figsize=(10, 8))  # 幅10インチ、高さ8インチ
ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#################################
