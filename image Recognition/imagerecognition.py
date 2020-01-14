import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
i=Image.open('chessboard.png')
iar=np.array(i)
print(iar)

plt.imshow(iar)
plt.show()
















