import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Load data
# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
# # Normalize (fixed axis=1 for both)
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)  # axis=1 is correct

# # Build model
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Flatten(input_shape=(28,28)),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])
#
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# # Train
# model.fit(x_train, y_train, epochs=3)
#
# # Save in new format
# model.save('handwritten.keras')  # Use .keras extension

# Load the model (now compatible)
model = tf.keras.models.load_model('handwritten.keras')

# # Evaluate
# loss, accuracy = model.evaluate(x_test, y_test)
# print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('handwritten.keras')

image_number = 1
image_folder = r"C:\Users\HP\Python_Practice\Python_Projects\Handwritten_Digit_Recognition_Neural_Network_Project\Text_Image"

# Check if folder exists
if not os.path.exists(image_folder):
    print("Error: Image folder does not exist!")
else:
    while os.path.isfile(f"{image_folder}/{image_number}.png"):
        img_path = f"{image_folder}/{image_number}.png"

        # Debug print
        print(f"Processing: {img_path}")

        try:
            # Load image in grayscale
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                print(f"Error: Could not read image at {img_path}")
                break

            # Resize the image to 28x28 without distortion
            img = cv2.resize(img, (28, 28))

            # Invert colors (black digits on white background)
            img = np.invert(img)

            # Normalize the image (scale pixel values to range [0, 1])
            img = img.astype("float32") / 255.0

            # Ensure correct shape for model input (1, 28, 28, 1)
            img = img.reshape(1, 28, 28, 1)

            # Model prediction
            prediction = model.predict(img)
            predicted_digit = np.argmax(prediction)

            print(f"This Digit is probably a {predicted_digit}")
            print("Raw model prediction:", prediction)  # Debugging output

            # Display the image
            plt.imshow(img[0, :, :, 0], cmap=plt.cm.binary)
            plt.show()

        except Exception as e:
            print(f"Error processing {img_path}: {e}")

        finally:
            image_number += 1
