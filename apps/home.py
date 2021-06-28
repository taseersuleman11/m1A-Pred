import streamlit as st
from PIL import Image

def app():
    st.balloons()
    st.subheader("""
    The process of nucleotides modification or the addition of one or more methyl groups to nucleotides is termed post transcriptional modification (PTM). 1-methyadenosine (m1A)  is also formed by the addition of methyl (-CH3) group to the nitrogen at the 1st position of adenosine base. m1A is abundantly found in ribosomal RNA (rRNA) and transfer RNA (tRNA) which is linked with many human diseases. Systematic identification of modified sites from RNA sequences is gaining much attention nowadays. For this purpose, an extreme gradient boost (XGBoost) based predictor, m1A-Pred is developed in this study for the prediction of modified m1A sites.""")
    image = Image.open('home_image.jpg')
    st.image(image)
    st.subheader("""
    A novel method for the extraction of position and composition-based properties in nucleotide sequences was adopted for features vectors generation.  Statistical moments were endorsed for dimensionality reduction in the obtained features. Through a series of experiments using different computational models and evaluation methods, it was revealed that XGBoost-based predictor m1A-Pred proved to be the most robust and accurate model for the identification of modified sites. To enhance the research on m1A sites, a friendly server was also developed which was the final phase of this research.""")


