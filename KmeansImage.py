import matplotlib.pyplot
import numpy
from sklearn.cluster import KMeans

img = matplotlib.pyplot.imread("image.jpg")
width = img.shape[0]
height = img.shape[1]
print(img.shape)

img = img.reshape(width*height,3)
print(img.shape)

kmeans = KMeans(n_clusters=14).fit(img)
labels = kmeans.predict(img)
cluster = kmeans.cluster_centers_

imgCopy = numpy.zeros_like(img)
for i in range(len(imgCopy)):
	imgCopy[i] = cluster[labels[i]]

imgCopy = imgCopy.reshape(width,height,3)

matplotlib.pyplot.imshow(imgCopy)
matplotlib.pyplot.show()

