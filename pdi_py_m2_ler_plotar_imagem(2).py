# -*- coding: utf-8 -*-
"""PDI_Py_M2_Ler_plotar_imagem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xOzA6ShOEJbvdQE5-AhveXitnDg-n4UF
"""

!pip install gdal
!pip install rasterio

!pip install spectral

# TIFFFILE
import tifffile as tif #não representa as coordenadas geográficas
import matplotlib.pyplot as plt
from spectral import imshow

img = tif.imread("/content/L71221071_07120010720_DN.tif")

img.shape
# número de linhas, colunas e bandas

plt.imshow(img[:,:,0], cmap = 'Greys_r') #banda 1

plt.imshow(img[:,:,3], cmap = 'Greys_r') #banda 4

imshow(img)

imshow(img, bands=(2,3,0)) #R,G,B

# GDAL
from osgeo import gdal
import numpy as np

img2 = gdal.Open("/content/L71221071_07120010720_DN.tif")

print(img2)

img3 = img2.ReadAsArray()

img3.shape #bandas, linhas, colunas

img3 = img3.swapaxes(0,2)

img3.shape #colunas, linhas, bandas

img3 = img3.swapaxes(0,1)

img3.shape

imshow(img3[:,:,3])

imshow(img3, (2,3,1))

b1 = img2.GetRasterBand(1).ReadAsArray()

imshow(b1)

b2 = img2.GetRasterBand(2).ReadAsArray()
b4 = img2.GetRasterBand(4).ReadAsArray()

stack = np.dstack([b1,b2,b4])

stack.shape

imshow(stack, (1,2,0))

# Rasterio
import rasterio
from rasterio.plot import show

rst = rasterio.open("/content/L71221071_07120010720_DN.tif")

print(rst)

show(rst, cmap='Greys_r') #coordenadas utm

b1 = rst.read(1)
b2 = rst.read(2)
b4 = rst.read(4)

stack = np.dstack([b1,b2,b4])

imshow(stack, (1,2,0))

with rasterio.open('/content/L71221071_07120010720_DN.tif') as rst:
  b1 = rst.read(1)
  b2 = rst.read(2)
  b4 = rst.read(4)

stack2 = np.dstack([b1,b2,b4])

imshow(stack2, (1,2,0))