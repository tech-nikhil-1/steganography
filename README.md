# steganography
A Tkinter-based image steganography tool for hiding and retrieving messages inside images.
It ensures secure communication by embedding messages into image pixels and retrieving them using a password.

Technologies Used
  Programming Language: Python
  GUI Framework: Tkinter
  Image Processing: OpenCV (cv2), PIL (Pillow), NumPy


How It Works?

  Encryption:
    The message (along with the password) is converted into ASCII values.
    These values are embedded into the RGB channels of image pixels.
    The modified image is saved as encryptedImage.png.

  Decryption:
    The program reads ASCII values from pixels.
    Extracts and verifies the password.
    If correct, the hidden message is displayed.

Use Cases

  Secure communication.
  Hiding sensitive information inside images.
  Protecting data from unauthorized access.



    
Future Scope
  Support for Video & Audio Steganography
  Stronger Encryption Algorithms
  AI-Based Steganalysis Protection
  Mobile App Implementation


**Steganography Process**

sample image for steganography:
        ![my_sample_image](https://github.com/user-attachments/assets/7b0b7409-2248-45f1-b835-eb4903c06b4a)



Encryption process at sender side :
       ![Screenshot 2025-02-25 130831](https://github.com/user-attachments/assets/20839813-f8c2-44a0-9aa2-30fe96347940)

  ![Screenshot 2025-02-25 130842](https://github.com/user-attachments/assets/8cf2a013-c078-47e3-ae20-5bcbd06e9004)




**sent the encrypted image to reciever !**
    Encrypted image : ![encryptedImage](https://github.com/user-attachments/assets/e3899191-1045-4820-a966-126f992f909f)




Decryption process at reciever side :
      ![Screenshot 2025-02-25 130917](https://github.com/user-attachments/assets/8ac600fd-e599-472f-8e67-474bc31ee17c)

      
  ![Screenshot 2025-02-25 130937](https://github.com/user-attachments/assets/7e76a21d-3c94-4982-b163-ec3f09ed9002)



For queries or suggestions, reach out at:
  andhavarapu.nikhil21@gmail.com
