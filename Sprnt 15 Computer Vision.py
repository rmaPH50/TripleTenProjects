#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid blue 2px; padding: 20px">
# 
# **Overall Summary of the Project**
# 
# Dear Robert,
# 
# Thank you for submitting your project on age estimation using the provided faces dataset. Your work shows a clear understanding of data preparation, exploration, and modeling strategies. Below is a summarized review based on the assessment criteria.
# 
# ---
# 
# ***Strengths:***
# - **Data Exploration and Understanding:**  
#   - The dataset’s size (7.6k images) and properties were examined.  
#   - The age distribution was visualized, providing insight into potential imbalances.  
#   - Sample images across various age groups were displayed, offering a qualitative check on image quality and diversity.
# 
# - **Model Architecture and Training:**  
#   - A ResNet50 backbone was employed, leveraging transfer learning effectively.  
#   - Data augmentation (e.g., flips, rotations, shifts) was introduced to increase training robustness.  
#   - A proper train-validation split was used to monitor performance during training.
# 
# - **Performance Metrics and Analysis:**  
#   - The model’s training MAE decreased substantially, indicating effective learning on the training set.  
#   - The final validation MAE remained under 8, meeting the project’s success criterion.  
#   - Detailed conclusions connected model behavior to dataset characteristics, addressing potential overfitting.
# 
# - **Clarity and Organization:**  
#   - The code is neatly arranged and well-structured, following a logical sequence from EDA to modeling.  
#   - Results (training output) were included, ensuring reproducibility and transparency.
# 
# ---
# 
# ***Areas of Improvement (Optional):***
# - **Overfitting Mitigation:**  
#   - While the model improved during training, the validation metrics fluctuated, suggesting mild overfitting. Consider employing early stopping, L2 regularization, or additional dropout layers to enhance generalization.
# 
# - **Augmentation and Fine-Tuning:**  
#   - Expand augmentation strategies (e.g., brightness/contrast adjustments) or attempt partial fine-tuning of the ResNet50 layers. This could help the model better generalize across diverse facial images and age ranges.
# 
# - **Evaluation Techniques:**
#   - Visualizing predicted vs. actual ages (e.g., scatter plots) or analyzing error distributions could provide deeper insights into the model’s strengths and weaknesses.
#   - Experimenting with different metrics or segmenting MAE by age groups could clarify where the model excels or needs improvement.
# 
# - **Commentary and Documentation:**  
#   - Adding brief markdown explanations at key steps would help future readers understand the rationale behind certain transformations, parameter choices, or architectural decisions.
# 
# ---
# 
# ***Critical Changes:***
# None. The main objectives have been met, and the model shows satisfactory performance with further room for optimization.
# 
# ---
# 
# ***Final Thoughts***
# 
# Your project successfully leverages computer vision techniques to estimate real age from facial images, showing promising initial results. With minor adjustments to regularization, augmentation, and evaluation strategies, you could further improve performance and gain deeper insights. Overall, this is a solid effort demonstrating both technical proficiency and an understanding of the model’s practical applications.
# 
# **Status:** **Approved**
# 
# </div>

# ## Initialization

# In[ ]:


import pandas as pd
import numpy as np
import os
import inspect
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import accuracy_score, mean_absolute_error


# ## Load Data

# The dataset is stored in the `/datasets/faces/` folder, there you can find
# - The `final_files` folder with 7.6k photos
# - The `labels.csv` file with labels, with two columns: `file_name` and `real_age`
# 
# Given the fact that the number of image files is rather high, it is advisable to avoid reading them all at once, which would greatly consume computational resources. We recommend you build a generator with the ImageDataGenerator generator. This method was explained in Chapter 3, Lesson 7 of this course.
# 
# The label file can be loaded as an usual CSV file.

# In[ ]:


# Load labels
labels_df = pd.read_csv('/datasets/faces/labels.csv')

# Get the list of image filenames and corresponding labels
file_names = labels_df['file_name'].values
real_ages = labels_df['real_age'].values

print(labels_df.head())


# ## EDA

# In[ ]:


# Load labels
labels_df = pd.read_csv('/datasets/faces/labels.csv')

# Display basic information about the dataset
print(f"Dataset size: {len(labels_df)} images")
print(labels_df.head())

# Check for missing values and other summary statistics
print(labels_df.info())


# In[ ]:


import matplotlib.pyplot as plt

# Plot the distribution of ages
plt.figure(figsize=(10, 6))
plt.hist(labels_df['real_age'], bins=30, color='skyblue', edgecolor='black')
plt.title("Age Distribution in the Dataset")
plt.xlabel("Age")
plt.ylabel("Number of Images")
plt.show()


# In[ ]:


# Load a few sample images from different age groups
def load_sample_images(age_groups, num_samples=15):
    sample_images = []
    for age in age_groups:
        # Get file names of images corresponding to the given age
        age_files = labels_df[labels_df['real_age'] == age]['file_name'].values
        sample_files = np.random.choice(age_files, num_samples, replace=False)
        
        for file_name in sample_files:
            img_path = os.path.join('/datasets/faces/final_files/', file_name)
            img = image.load_img(img_path, target_size=(150, 150))
            img_array = image.img_to_array(img) / 255.0  # Normalize pixel values
            sample_images.append(img_array)
    
    return sample_images

# Choose some representative ages to display (e.g., young, middle-aged, old)
age_groups = [5, 20, 40, 60, 80]
sample_images = load_sample_images(age_groups)

# Display the sample images
fig = plt.figure(figsize=(10, 10))
for i, img in enumerate(sample_images[:15]):  # Display only 15 images
    ax = fig.add_subplot(3, 5, i+1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

plt.show()


# ### Findings

# Dataset Size: The dataset contains 7.6k images. The exact number of samples is important for deciding the training/validation split.
# 
# Age Distribution: If the age distribution is skewed (e.g., more younger faces than older ones), it may lead to model bias toward predicting younger ages.
# 
# If the distribution is relatively balanced, this is a good sign for training the model.
# 
# Diversity of Faces: By displaying images across different age groups, we can visually confirm whether the dataset includes a diverse set of faces in terms of appearance and lighting conditions. If the dataset has more variability (e.g., different lighting conditions, facial expressions), the model might need data augmentation strategies to generalize well.
# 
# Potential Implications for Model Training:
# 
# Imbalanced Age Distribution:
# 
# If the dataset is imbalanced (e.g., more young people than older ones), the model might have trouble predicting ages for underrepresented age groups.
# 
# This could be addressed with techniques like oversampling, undersampling, or adjusting class weights.
# 
# Age Group Variability:
# 
# The variability within each age group (e.g., different skin tones, lighting, or facial expressions) may require more robust data augmentation during training.
# 
# Image Quality: The quality of the images (e.g., blurry, low-resolution, or poorly lit images) may affect model performance. Preprocessing steps like normalization, contrast adjustment, or noise reduction may be needed.

# ## Modelling

# Define the necessary functions to train your model on the GPU platform and build a single script containing all of them along with the initialization section.
# 
# To make this task easier, you can define them in this notebook and run a ready code in the next section to automatically compose the script.
# 
# The definitions below will be checked by project reviewers as well, so that they can understand how you built the model.

# In[ ]:


import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


# In[ ]:


def load_train(path):
    """
    It loads the train part of dataset from path
    """
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.25,
        horizontal_flip=True,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2
    )

    train_gen_flow = datagen.flow_from_dataframe(
        dataframe=pd.read_csv(f"{path}/labels.csv"),
        directory=f"{path}/final_files",
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='training',
        seed=42
    )
    
    return train_gen_flow


# In[ ]:


def load_test(path):
    """
    It loads the validation/test part of dataset from path
    """
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.25)

    test_gen_flow = datagen.flow_from_dataframe(
        dataframe=pd.read_csv(f"{path}/labels.csv"),
        directory=f"{path}/final_files",
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='validation',
        seed=42
    )
    
    return test_gen_flow


# In[ ]:


def create_model(input_shape):
    """
    It defines the model
    """
    backbone = ResNet50(
        input_shape=input_shape,
        include_top=False,
        weights='imagenet'
    )
    
    model = Sequential([
        backbone,
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='linear')
    ])
    
    model.compile(
        optimizer=Adam(learning_rate=0.0001),
        loss='mean_squared_error',
        metrics=['mae']
    )
    
    return model


# In[ ]:


from sklearn.metrics import mean_absolute_error

def train_model(model, train_data, test_data, batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):
    """
    Trains the model given the parameters and calculates the MAE score on the test data
    """
    # Train the model
    history = model.fit(
        train_data,
        validation_data=test_data,
        batch_size=batch_size,
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2
    )
    
    # Get predictions on the test data
    predictions = model.predict(test_data, batch_size=batch_size)

    # Get the true labels from the test data (you may need to extract these from your test_data object)
    true_values = test_data.labels  # Adjust based on how your test_data is structured

    # Calculate MAE
    mae = mean_absolute_error(true_values, predictions)
    
    print(f'Mean Absolute Error (MAE): {mae}')
    
    return model, mae


# ## Prepare the Script to Run on the GPU Platform

# Given you've defined the necessary functions you can compose a script for the GPU platform, download it via the "File|Open..." menu, and to upload it later for running on the GPU platform.
# 
# N.B.: The script should include the initialization section as well. An example of this is shown below.

# In[ ]:


# prepare a script to run on the GPU platform

init_str = """
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
"""

# Write the script to a file
with open('run_model_on_gpu.py', 'w') as f:
    
    f.write(init_str)
    f.write('\n\n')
    
    for fn_name in [load_train, load_test, create_model, train_model]:
        src = inspect.getsource(fn_name)
        f.write(src)
        f.write('\n\n')


# ### Output

# Place the output from the GPU platform as an Markdown cell here.

# Epoch 1/20
# 356/356 - 35s - loss: 95.3532 - mae: 7.4339 - val_loss: 124.3362 - val_mae: 8.4921
# Epoch 2/20
# 356/356 - 35s - loss: 76.8372 - mae: 6.6707 - val_loss: 127.6357 - val_mae: 8.6035
# Epoch 3/20
# 356/356 - 35s - loss: 69.9428 - mae: 6.3992 - val_loss: 91.1531 - val_mae: 7.4454
# Epoch 4/20
# 356/356 - 35s - loss: 64.4249 - mae: 6.1407 - val_loss: 124.0287 - val_mae: 8.3481
# Epoch 5/20
# 356/356 - 35s - loss: 52.8486 - mae: 5.5913 - val_loss: 109.1004 - val_mae: 8.2192
# Epoch 6/20
# 356/356 - 35s - loss: 46.3094 - mae: 5.2223 - val_loss: 85.1038 - val_mae: 7.0332
# Epoch 7/20
# 356/356 - 35s - loss: 38.2617 - mae: 4.7951 - val_loss: 92.0900 - val_mae: 7.3359
# Epoch 8/20
# 356/356 - 35s - loss: 37.4804 - mae: 4.7402 - val_loss: 80.0016 - val_mae: 6.7239
# Epoch 9/20
# 356/356 - 35s - loss: 33.5237 - mae: 4.4271 - val_loss: 83.2579 - val_mae: 6.8529
# Epoch 10/20
# 356/356 - 35s - loss: 28.5170 - mae: 4.1411 - val_loss: 83.5056 - val_mae: 6.9629
# Epoch 11/20
# 356/356 - 35s - loss: 27.0142 - mae: 3.9700 - val_loss: 92.1290 - val_mae: 7.1866
# Epoch 12/20
# 356/356 - 35s - loss: 27.4564 - mae: 4.0428 - val_loss: 185.6307 - val_mae: 11.4591
# Epoch 13/20
# 356/356 - 35s - loss: 23.7961 - mae: 3.7407 - val_loss: 92.3429 - val_mae: 7.2467
# Epoch 14/20
# 356/356 - 35s - loss: 24.6167 - mae: 3.8116 - val_loss: 92.4542 - val_mae: 7.1401
# Epoch 15/20
# 356/356 - 35s - loss: 22.2604 - mae: 3.6746 - val_loss: 82.5822 - val_mae: 6.7841
# Epoch 16/20
# 356/356 - 35s - loss: 20.1899 - mae: 3.4430 - val_loss: 86.3830 - val_mae: 6.8304
# Epoch 17/20
# 356/356 - 35s - loss: 17.3425 - mae: 3.2205 - val_loss: 78.4369 - val_mae: 6.6419
# Epoch 18/20
# 356/356 - 35s - loss: 16.5249 - mae: 3.1295 - val_loss: 81.7731 - val_mae: 6.7226
# Epoch 19/20
# 356/356 - 35s - loss: 16.6140 - mae: 3.1421 - val_loss: 80.9727 - val_mae: 6.9908
# Epoch 20/20
# 356/356 - 35s - loss: 17.0187 - mae: 3.1785 - val_loss: 93.4115 - val_mae: 7.6512

# ## Conclusions

# Model Training Analysis
# Based on the training output, the model was trained over 20 epochs, and the performance metrics we’re most interested in are the loss and mean absolute error (MAE) on both the training set and validation set. Here's a summary of the results:
# 
# Key Observations:
# Training Loss & MAE:
# 
# The training loss decreased steadily from 95.35 at the beginning to 17.02 by the 20th epoch, which shows that the model is learning and the error is reducing.
# The training MAE improved as well, reducing from 7.43 in the first epoch to 3.18 at the end.
# Validation Loss & MAE:
# 
# The validation loss fluctuated somewhat. It started at 124.34 and reduced initially but then increased towards the end, peaking at 185.63 during epoch 12 before stabilizing and ending at 93.41 in the last epoch.
# The validation MAE also followed a similar pattern, improving initially but then showing some oscillation, with a final value of 7.65.
# Overfitting Potential:
# 
# The gap between training and validation MAE indicates a potential overfitting issue, where the model is performing better on the training data than on unseen data (validation set). This is evident in the fluctuation of validation loss and MAE in later epochs. Regularization techniques such as dropout, data augmentation, or early stopping could help mitigate this.
# Can Computer Vision Help the Customer?
# Yes, computer vision can be very helpful in this case, given the task of predicting real age from images. It can be applied to a wide range of practical scenarios:
# 
# Age Prediction:
# 
# If the customer is in the healthcare or social services industry, computer vision could help predict the age of individuals based on images, aiding in demographic research or age-based service recommendations.
# Personalization of Services:
# 
# By predicting age, the model could enable targeted marketing strategies or personalized experiences based on the user’s age group.
# Automated Facial Recognition for Verification:
# 
# The model could be extended for facial verification or to authenticate individuals for age-restricted services (e.g., age-based product recommendations or access to age-sensitive areas).
# Other Practical Tasks the Customer Could Solve with the Model:
# Age Group Classification:
# 
# Rather than predicting exact ages, the model could be modified to classify individuals into specific age groups (e.g., children, teens, adults, elderly). This could be useful for applications in education, healthcare, and entertainment, where age-based categories are important.
# Monitoring and Profiling:
# 
# In industries like retail or marketing, age prediction can help understand the demographic distribution of visitors to websites or stores. This could improve inventory management, promotions, and product placements.
# Emotion Recognition:
# 
# Extending the model to recognize emotions (e.g., happy, sad, angry, neutral) from facial expressions could be valuable in applications such as customer service, mental health analysis, or security systems.
# Security and Surveillance:
# 
# In security systems, knowing the approximate age of individuals captured in surveillance footage can aid in identifying persons of interest or matching faces with known databases.
# Healthcare Diagnostics:
# 
# In the healthcare sector, knowing the patient's approximate age based on facial recognition could help in pre-screening processes or assist medical professionals in assessing a patient's health based on age-related factors.
# Conclusion:
# While the model shows good improvement in terms of training loss and MAE, there’s a need to address overfitting and fine-tune the model for better generalization. Regularization techniques like dropout, more data augmentation, or even exploring more advanced models could help reduce the validation loss fluctuation. Nonetheless, the model’s potential for age prediction in computer vision applications is promising and could be utilized in various industries ranging from healthcare to marketing and security.

# # Checklist

# - [ ]  Notebook was opened
# - [ ]  The code is error free
# - [ ]  The cells with code have been arranged by order of execution
# - [ ]  The exploratory data analysis has been performed
# - [ ]  The results of the exploratory data analysis are presented in the final notebook
# - [ ]  The model's MAE score is not higher than 8
# - [ ]  The model training code has been copied to the final notebook
# - [ ]  The model training output has been copied to the final notebook
# - [ ]  The findings have been provided based on the results of the model training

# In[ ]:




