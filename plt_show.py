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

plt.figure(figsize=(6,6))
plt.imshow(sketch, cmap='gray')
plt.axis('off') 
plt.tight_layout()
plt.show()

#################################

plt.figure(figsize=(6,6))
plt.imshow(image)
plt.axis('off') 
plt.show()

plt.figure(figsize=(6,6))
plt.imshow(sketch, cmap='gray')
plt.axis('off') 
plt.show()

fig, axs = plt.subplots(figsize=(6,6))
axs.imshow(image) 
axs.imshow(sketch, cmap='gray', alpha=0.6) #0.1--0.9
axs.axis('off')
plt.show()
fig.savefig('save.png', bbox_inches='tight')

#################################

plt.axvspan(pd.Timestamp('2020-01-01'), pd.Timestamp('2021-01-01'), color='green', alpha=0.1)
plt.axvline(pd.Timestamp('2020-01-01'), linestyle = "--", color='green')
plt.axvline(pd.Timestamp('2021-01-01'), linestyle = "--", color='green')
plt.text(pd.Timestamp('2020-05-22'), 62000, "No virus", size = 17)
plt.title('Emission by date', size=15, pad=10)
plt.show()

#################################
