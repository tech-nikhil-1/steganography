# steganography

This project implements *image steganography* using Python and Tkinter, allowing users to hide secret messages inside images and later retrieve them using a password. 
It ensures secure communication by embedding messages into image pixels and retrieving them using a password.

**Technologies Used**

- Programming Language: Python
- GUI Framework: Tkinter
- Image Processing: OpenCV (cv2), PIL (Pillow), NumPy

**Prerequisites for Image Steganography Project**
- Software Requirements: Python 3.x or any IDE
- Required Python Libraries:
  - 1.OpenCV (cv2) – Image processing
  - 2.NumPy (numpy) – Handling image arrays
  - 3.Pillow (PIL) – Image manipulation
  - 4.Tkinter (tkinter) – GUI for user interaction
  
        pip install opencv-python numpy pillow tkinter

**Use Cases**
- Secure communication.
- Hiding sensitive information inside images.
- Protecting data from unauthorized access.

**How It Works**

  Encryption:
  - The message (along with the password) is converted into ASCII values.
  - These values are embedded into the RGB channels of image pixels.
  - The modified image is saved as encryptedImage.png.

  Decryption:
  - The program reads ASCII values from pixels.
  - Extracts and verifies the password.
  - If correct, the hidden message is displayed.

  
**Steganography Process**

sample image for steganography:

  ![my_sample_image](https://github.com/user-attachments/assets/7b0b7409-2248-45f1-b835-eb4903c06b4a)


Encryption process at sender side :

  ![Screenshot 2025-02-25 130831](https://github.com/user-attachments/assets/20839813-f8c2-44a0-9aa2-30fe96347940)




**send the encrypted image to Reciever !**

  Encrypted image : 
  
  ![encryptedImage](https://github.com/user-attachments/assets/e3899191-1045-4820-a966-126f992f909f)


Decryption process at reciever side :

  ![Screenshot 2025-02-25 130937](https://github.com/user-attachments/assets/7e76a21d-3c94-4982-b163-ec3f09ed9002)

**Conclusion**

This project demonstrates how steganography can be used to securely hide messages inside images.  
Future improvements could include better encryption techniques and support for different file formats.

Thank you for checking out this project!
Feel free to contribute, report issues, or suggest improvements.  


For queries or suggestions, reach out at:
  andhavarapu.nikhil21@gmail.com
