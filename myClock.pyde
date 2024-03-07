# Assuming you have the images named as 1.png, 2.png, ..., 9.png
# in the 'data' folder

def setup():
    size(1000, 500)  # Set the canvas size
    
    global image_filenames
    
    # Create a list of image filenames
    image_filenames = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]

def draw():
    global h_image1, h_image2, m_image1, m_image2, s_image1, s_image2
    global h1, h2, m1, m2, s1, s2
    
    background(255)  # Clear the canvas

    # Obtain the current time
    h1 = hour() / 10
    h2 = hour() % 10
    m1 = minute() / 10
    m2 = minute() % 10
    s1 = minute() / 10
    s2 = second() % 10

    # Load the images
    h_image1 = loadImage(image_filenames[h1])
    h_image2 = loadImage(image_filenames[h2])
    
    m_image1 = loadImage(image_filenames[m1])
    m_image2 = loadImage(image_filenames[m2])
    
    s_image1 = loadImage(image_filenames[s1])
    s_image2 = loadImage(image_filenames[s2])

    # Display the current time using images
    image(h_image1, 50, 50, 100, 300)  # Hour
    image(h_image2, 200, 50, 100, 300)
    
    image(m_image1, 350, 50, 100, 300)  # Minute
    image(m_image2, 500, 50, 100, 300)
    
    image(s_image1, 650, 50, 100, 300)  # Second
    image(s_image2, 800, 50, 100, 300)
    
