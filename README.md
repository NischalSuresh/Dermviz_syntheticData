# Dermviz_syntheticData
Create synthetic skin lesion images 

1. Use script take_crops.py to extract snippets of lesions from full body images
2. Use script create_PC.py to create Point-clouds of lesion snippets where the z-axis represents the brightness of the pixels. This is useful to analyze the lesions.
3. Train a GAN on these snippets to generate synthetic images (https://arxiv.org/pdf/2006.10738.pdf). 
