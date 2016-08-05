import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Get the MNIST data
df = pd.read_csv('/Users/amitkaps/Dropbox/github/modelvis/mnist_test.csv', header=None)
df.head()
df.rename(columns={0:'num'}, inplace=True)
df['num'] = df['num'].astype('category')
df.dtypes

# Plot a particular MNIST data
def plotDigit(arr1D, label):
    pixels = np.array(arr1D, dtype='uint8')
    # Reshape the array into 28 x 28 array (2-dimensional array)
    pixels = pixels.reshape((28, 28))
    # Plot
    plt.title('Label is {label}'.format(label=label))
    plt.imshow(pixels, cmap='gray')
    
    
def plotSymmetry(arr1D, label):
    pixels = np.array(arr1D, dtype='uint8')
    pixels = pixels.reshape((28, 28))
    plotDigit(pixels, label)
    plt.show()
    pixelslr = np.fliplr(pixels)
    plotDigit(pixelslr, label)
    plt.show()
    plotDigit(np.abs(pixelslr - pixels), label)
    plt.show()
    pixelsud = np.flipud(pixels)
    plotDigit(pixelsud, label)
    plt.show()
    plotDigit(np.abs(pixelsud - pixels), label)
    plt.show()


label = df.ix[14,0]
arr1D = df.ix[14,1:785]
plotDigit(arr1D, label)
plotSymmetry(arr1D, label)

# Calculate Intensity Features
df['intensity'] = df.ix[:,1:785].mean(axis = 1)/255
df.head()

intensity_avg = df.groupby('num')['intensity'].mean()
intensity_avg.head()
intensity_avg.plot(kind = 'bar')

# Calculate Symmetry Features
def symmetry(arr1D):
    pixels = np.array(arr1D, dtype = 'uint8')
    pixels = pixels.reshape(28,28)
    # Flip Left to Right
    pixelslr = np.fliplr(pixels)
    # Flip Up to Down
    pixelsud = np.flipud(pixels)
    sym_matrix = (np.abs(pixels - pixelslr) + np.abs(pixels - pixelsud))/2
    sym = np.mean(sym_matrix) / 255
    return sym
    
    
df['symmetry'] = df.ix[:,1:785].apply(symmetry, axis = 1)
df.head()
symmetry_avg = df.groupby('num')['symmetry'].mean()
symmetry_avg.head()
symmetry_avg.plot(kind = 'bar')


# Plot Intensity vs. Symmetry for 1 and 2 digits
df12 = df[(df.num == 1) | (df.num == 2)]
df12.head()
df12.shape
df12.plot(kind="scatter", x = 'intensity', y = 'symmetry', 
          c = df12.num, alpha = 0.5, s = 50,  cmap=plt.cm.viridis)

