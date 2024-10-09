import streamlit as st 
import warnings
warnings.filterwarnings("ignore")

# UI configurations
st.set_page_config(page_title="ambideXtrous",
                   page_icon=":bridge_at_night:",
                   layout="centered")



st.write("""
    ### 🚀 **Exploring Image Classification Models with Transfer Learning!**
    - 🆕 **Models Evaluated**: We've assessed the following state-of-the-art models using the Flick27 dataset:
        - **Xception** 🤖
        - **InceptionV3** 🌈
        - **MobileNetV2** 📱
        - **EfficientNet** ⚡

    ### 🔍 **Performance Aspects Compared**
    - **⚡ Inference Time**: How quickly each model makes predictions.
    - **📦 Model Size**: The storage requirements of each model.
    - **🔢 Number of Parameters**: The complexity and capacity of each model.
    - **📈 Accuracy**: How well each model performs in classifying images.
    - **🏷️ Predicted Class**: The class each model predicts for the input images.

    - 📚 **Understanding Trade-Offs**: These comparisons will help us understand the trade-offs between speed, efficiency, and accuracy for each model.

    💡 **You can train your own model on any dataset following the link below:**
    [Train Your Model](https://github.com/ambideXtrous9/Brand-Logo-Classification-using-TransferLearning-Flickr27/tree/main/Final%20Model)
    
    🚀 **To see How it works..**
    """)